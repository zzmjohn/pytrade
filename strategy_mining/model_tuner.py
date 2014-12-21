#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import math
from math import log
from sklearn import metrics,preprocessing,cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.linear_model as lm
import pandas as p
from time import gmtime, strftime
import scipy
import sys
import sklearn.decomposition
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from string import punctuation
from sklearn.neighbors import RadiusNeighborsRegressor, KNeighborsRegressor
import time
from scipy import sparse
from itertools import combinations
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier
import operator
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import svm
from sklearn import tree
from sklearn import linear_model, metrics
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
# parse the command paramaters
from optparse import OptionParser
from model_base import get_date_str

def main(options, args):
    if options.utildate == None:
        options.utildate = get_date_str()
    fsampleY = open(options.input + "/" + options.utildate + "/train.csv", "r")
    l_X = []
    l_y = []

    for line in fsampleY:
        tokens = line.split(",")
        features = []
        for i in range(len(tokens)):
            if i < len(tokens)-1:
                features.append(float(tokens[i]))
            else:
                l_y.append(int(tokens[i]))
        l_X.append(features)
    X = np.array(l_X)
    y = np.array(l_y)
    assert(X.shape[0] == y.shape[0])
    if int(options.short) > 0:
        print "using short data for test purpose"
        X = X[0:int(options.short)]
        y = y[0:int(options.short)]
    
    print "preparing models"
    if options.isregress == True:
        model_predictor = GradientBoostingRegressor(max_features=0.6, learning_rate = 0.05, max_depth=5, n_estimators=300)
    else :
        model_predictor = GradientBoostingClassifier(max_features=0.6, learning_rate=0.05, max_depth=5, n_estimators=300)
    #model_predictor = GradientBoostingClassifier()
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)
    # print cross_validation.cross_val_score(model_predictor, X, y)
    clf = model_predictor.fit(X_train, y_train)

    if options.isregress:
        pred = model_predictor.predict(X_test)
    else:
        pred = model_predictor.predict_proba(X_test)
    # calculate the R2score
    r2 = r2_score(y_test, pred)
    print "the r2 score is ", r2
#    tpred = model_predictor.predict(X_test)
 #   score = model_predictor.score(X_test, tpred)
 #   print "score=", score
    assert(len(pred) == X_test.shape[0])
    dpred = {}
    for i in range(len(pred)):
        if options.isregress:
            dpred[i] = pred[i]
        else:
            dpred[i] = pred[i,1]
    dpred = sorted(dpred.iteritems(),key=operator.itemgetter(1), reverse = 1)
    stop_index = 0
    for i in range(len(dpred)):
        if dpred[i][1] < 10000:
            break
        else:
            stop_index = i
    m=0
    n=(stop_index) / 10
    for i in range(n+1):
        if y_test[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

    m=0
    n=(stop_index) / 50
    for i in range(n+1):
        if y_test[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

        
    m=0
    n=(stop_index) 
    for i in range(n+1):
        if y_test[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

    if options.isregress :
        pred = model_predictor.predict(X_train)
    else:
        pred = model_predictor.predict_proba(X_train)
    dpred = {}
    for i in range(len(pred)):
        if options.isregress:
            dpred[i] = pred[i]
        else:
            dpred[i] = pred[i,1]
    # dpred = [(3, 9781.0001), (2, 9811.0000), (0, 9873.06), (6, 10111.999), (1, 10289.999), (5, 10343.9), (4, 10387.999)]
    dpred = sorted(dpred.iteritems(),key=operator.itemgetter(1),reverse=1)
    stop_index = 0
    for i in range(len(dpred)):
        if dpred[i][1] < 10000:
            break
        else :
            stop_index = i
    m=0
    n=(stop_index) / 10
    for i in range(n+1):
        if y_train[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

    m=0
    n=(stop_index) / 50
    for i in range(n+1):
        if y_train[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

        
    m=0
    n=(stop_index) 
    for i in range(n+1):
        if y_train[dpred[i][0]] > 10000:
            m += 1
    print "%d %f %f %f" % (n, dpred[0][1], dpred[n][1], m * 1.0 / (n+1))

    #{{{ prediction
    print "prediction ..."
    stock_predict_out = file(options.input + "/" + options.utildate + "/predict.csv", "w")
    for line in file(options.input + "/" + options.utildate + "/last.csv", "r"):
        tokens = line.split(",")
        l_features = []
        for i in range(len(tokens)):
            if 0 == i:
                print >> stock_predict_out, "%s," % tokens[i],
            elif 1 == i:
                print >> stock_predict_out, "%s," % tokens[i],
            else:
                l_features.append(float(tokens[i].strip()))
        l_features2 = []
        l_features2.append(l_features)
        np_features = np.array(l_features2)
        if np_features.shape[1] != X.shape[1] :
            assert(false)
        if options.isregress:
            pred = model_predictor.predict(np_features)
            print >> stock_predict_out, "%f" % pred
        else:
            pred = model_predictor.predict_proba(np_features)
            print >> stock_predict_out, "%f" % pred[0,1]
    stock_predict_out.close()

    #}}}

def parse_options(paraser): # {{{
    """
    parser command line
    """
    parser.add_option("--input", dest="input",action = "store", default="data/prices_series/", help = "the input filename dir")
    parser.add_option("--short", dest="short",action = "store", default=-1, help = "using short data")
    parser.add_option("--utildate", dest="utildate",action = "store", default=None, help = "the last date to train")
    parser.add_option("--isregress", dest="isregress",action = "store_true", default=True, help = "using repgress model or classify?")
    return parser.parse_args()
#}}} 

# execute start here
if __name__ == "__main__": #{{{
    parser = OptionParser()
    (options, args) = parse_options(parser)
    main(options, args)
# }}}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

import model.model_param_set as param_set

"""
## 研究目的
## 结论
"""
ta =  param_set.d_dir_ta

l_params = [
        #("ta1s1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1s1"], "label5", ("2010-01-01", '2016-12-31'),  100),


        #("ta1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  1000),
        #("ta1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  -1),

        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-01-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-01-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-02-01", '2013-02-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-02-01", '2013-02-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-03-01", '2013-03-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-03-01", '2013-03-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-04-01", '2013-04-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-04-01", '2013-04-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-05-01", '2013-05-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-05-01", '2013-05-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-06-01", '2013-06-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-06-01", '2013-06-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-07-01", '2013-07-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-07-01", '2013-07-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-08-01", '2013-08-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-08-01", '2013-08-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-09-01", '2013-09-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-09-01", '2013-09-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-10-01", '2013-10-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-10-01", '2013-10-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-11-01", '2013-11-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-11-01", '2013-11-31'),  -1),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-12-01", '2013-12-31'),  100),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-12-01", '2013-12-31'),  -1),

        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-01-01", '2016-01-31'),  100),
        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-01-01", '2016-01-31'),  -1),
        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-02-01", '2016-02-31'),  100),
        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-02-01", '2016-02-31'),  -1),
        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-03-01", '2016-03-31'),  100),
        #("ta1s4_GBCv1n320md3lr001_l5_s2002e2011" , ta["ta1s4"], "label5", ("2016-03-01", '2016-03-31'),  -1),

        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-01-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-01-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-02-01", '2016-02-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-02-01", '2016-02-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-03-01", '2016-03-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-03-01", '2016-03-31'),  -1),

        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label3", ("2016-04-01", '2016-04-31'),  100),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label3", ("2016-04-01", '2016-04-31'),  -1),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label3", ("2016-05-01", '2016-05-31'),  100),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label3", ("2016-05-01", '2016-05-31'),  -1),

        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2010-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2010-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2011-01-01", '2011-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2011-01-01", '2011-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2012-01-01", '2012-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2012-01-01", '2012-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2014-01-01", '2014-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2014-01-01", '2014-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2015-01-01", '2015-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2015-01-01", '2015-12-31'),  -1),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2010-01-01", '2010-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2010-01-01", '2010-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2011-01-01", '2011-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2011-01-01", '2011-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2012-01-01", '2012-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2012-01-01", '2012-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2013-01-01", '2013-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2014-01-01", '2014-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2014-01-01", '2014-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2015-01-01", '2015-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2015-01-01", '2015-12-31'),  -1),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2016-01-01", '2016-12-31'),  -1),

        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label5", ("2010-01-01", '2016-12-31'),  100),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label5", ("2010-01-01", '2016-12-31'),  300),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label5", ("2010-01-01", '2016-12-31'),  1000),
        #("ta1s5_GBCv1n320md3lr001_l5_s2000e2009" , ta["ta1s5"], "label5", ("2010-01-01", '2016-12-31'),  -1),

        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-01-31'),  100),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-01-31'),  300),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-03-31'),  1000),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-12-31'),  2000),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-12-31'),  2300),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-12-31'),  2500),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-12-31'),  2600),
        #("ta1s4_GBCv1n500md3lr001_l5_s2000e2009" , ta["ta1s4"], "label5", ("2016-01-01", '2016-12-31'),  -1),

        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  100),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  300),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  1000),
        ("ta1_GBCv1n1000md3lr001_l5_s1700e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  1000),
        #("ta1_GBCv1n400md3lr001_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2016-12-31'),  -1),

        ]


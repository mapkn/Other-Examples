# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:46:55 2019

@author: patemi
"""


#http://docs.scipy.org/doc/scipy-0.7.x/reference/generated/scipy.stats.kstest.html

# Kolmogorov Smirnov test


from scipy.stats import kstest
from scipy.stats import ks_2samp

import numpy as np

x = np.random.normal(0,1,1000)
test_stat = kstest(x, 'norm')







np.random.seed(12345678)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
z = np.random.normal(1.1, 0.9, 1000)

test_stat1= ks_2samp(x, y)

test_stat2=ks_2samp(x, z)
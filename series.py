# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:09:22 2018

@author: patemi
"""

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])



def SeriestoList(s):    
    return s.values.tolist()
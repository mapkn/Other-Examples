# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:56:12 2018

@author: patemi
"""

import pandas as pd

import os.path
import numpy as np

from datetime import datetime, timedelta


path = '\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\StressedVaR Period Change'
file = 'MarketArchiveSt.2018-03-13_PRD.csv'




(a,b)=os.path.split(path)
(c,d)=os.path.splitdrive(path)




print(os.path.join(path,file))

df_input=pd.read_csv(os.path.join(path,file), encoding='latin-1', low_memory=False)
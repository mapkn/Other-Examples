# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:49:40 2017

@author: patemi
"""

from pandas_datareader import data
#import pandas_datareader.data as web
from datetime import date
import numpy as np
import pandas as pd

# Grab time series data for 5-year history for the stock (here AAPL)
# and for S&P-500 Index
sdate = date(2008,12,31)
edate = date(2013,12,31)
df = DataReader('WFM','yahoo',sdate,edate)
dfb = DataReader('^GSPC','yahoo',sdate,edate)

# create a time-series of monthly data points
rts = df.resample('M',how='last')
rbts = dfb.resample('M',how='last')
dfsm = pd.DataFrame({'s_adjclose' : rts['Adj Close'],
                        'b_adjclose' : rbts['Adj Close']},
                        index=rts.index)

# compute returns
dfsm[['s_returns','b_returns']] = dfsm[['s_adjclose','b_adjclose']]/\
    dfsm[['s_adjclose','b_adjclose']].shift(1) -1
dfsm = dfsm.dropna()
covmat = np.cov(dfsm["s_returns"],dfsm["b_returns"])

# calculate measures now
beta = covmat[0,1]/covmat[1,1]
alpha= np.mean(dfsm["s_returns"])-beta*np.mean(dfsm["b_returns"])

# r_squared     = 1. - SS_res/SS_tot
ypred = alpha + beta * dfsm["b_returns"]
SS_res = np.sum(np.power(ypred-dfsm["s_returns"],2))
SS_tot = covmat[0,0]*(len(dfsm)-1) # SS_tot is sample_variance*(n-1)
r_squared = 1. - SS_res/SS_tot
# 5- year volatiity and 1-year momentum
volatility = np.sqrt(covmat[0,0])
momentum = np.prod(1+dfsm["s_returns"].tail(12).values) -1

# annualize the numbers
prd = 12. # used monthly returns; 12 periods to annualize
alpha = alpha*prd
volatility = volatility*np.sqrt(prd)

print (beta,alpha, r_squared, volatility, momentum)
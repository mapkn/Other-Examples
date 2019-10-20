# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:40:50 2017

@author: patemi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:12:54 2016

@author: Mitul
"""

import numpy as np
import pandas as pd
#import quandl
#import pandas.io.data as web
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import math

#stocks=['^GSPC','^FTSE']
stocks=['ORCL','IBM']

""" Get SP500 data from Yahoo, add it to a new DataFrame and plot it"""
sp500=web.DataReader('^GSPC', data_source='google',start='1/1/2000', end='4/14/2014')

stcks=web.DataReader(stocks, data_source='google',start='1/1/2000', end='4/14/2014')

#indices=web.get_data_yahoo(stocks,start='1/1/2000', end='4/14/2014')
""" Outputs information about the sp500 DataFrame """
sp500.info()


""" Plot the Close only from the DataFrame """
sp500['Close'].plot(grid=True, figsize=(8,5))



""" Add the MAs to the same Data Object """
sp500['42d']=np.round(pd.rolling_mean(sp500['Close'], window=42),2)
sp500['252d']=np.round(pd.rolling_mean(sp500['Close'], window=252),2)


""" Calculate the log returns without using a loop """
sp500['Return']=np.log(sp500['Close']/sp500['Close'].shift(1))


""" Calculate the moving volatility"""
sp500['Mov_Vol']=pd.rolling_std(sp500['Return'], window=252)*math.sqrt(252)

"""sp500[['Close','42d','252d']].tail()"""

""" Plot the Close with Moving averages"""
sp500[['Close','42d','252d']].plot(grid=True, figsize=(8,5))

sp500[['Close','Mov_Vol','Return']].plot(subplots=True, style='b',figsize=(8,5))






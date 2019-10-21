# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:12:54 2016

@author: Mitul
"""

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
import math

#stocks=['^GSPC','^FTSE']
stocks=['ORCL','IBM']

""" Get SP500 data from Yahoo, add it to a new DataFrame and plot it"""
sp500=web.DataReader('^GSPC', data_source='yahoo',start='1/1/2000', end='4/14/2014')

stcks=web.DataReader(stocks, data_source='yahoo',start='1/1/2000', end='4/14/2014')

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



""" Define a new dataframe """

df=pd.DataFrame([10,20,30,40], columns=['numbers'], index=['a', 'b', 'c', 'd'])



""" New Columns """

""" enlarging the Dataframe object, new column generates """
df['floats']=(1.5,2.5,3.5,4.5)

""" selection of a column"""
x=df['floats']

""" using a whole Dataframe object to define the column """
df['names']=pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'], 
                index=['d', 'a', 'b', 'c'])



csv_file = open('Data.csv','r') # open file for reading

content=csv_file.readlines()

content1=pd.read_csv('Data.csv', index_col='Date', parse_dates=True)

"""for line in content[:7]:
    print (line)"""

"""for i in range(4):
    print (csv_file.readline())"""

""" get the FTSE"""
ftse=content1['FTSE']

""" get last 4 days data"""
ftse=ftse.tail(4)

"""ftse.plot(label='FTSE')"""

""" plot the content1 DataFrame items """
content1.plot(subplots=True, grid=True, style='b', figsize=(8,6))

""" Correlation matrix from all elements of the content1 DataFrame """
content1corr=content1.corr()

plt.legend()
plt.show()





csv_file.close()
    



"""data=np.random.standard_normal((1000000,5)).round(5)    #sample data set"""



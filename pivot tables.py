# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:15:28 2017

@author: patemi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:59:13 2017

@author: patemi
"""
import pandas as pd
import os.path
import numpy as np

from datetime import datetime, timedelta
from functools import reduce 





#path = '\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\StressedVaR Period Change'

path='G:\\\Market Risk Management\\Mitul\\Murex Curve Changes May 2018'
file1 = 'SR_Bonds_GPSREC.xlsx'
#file2 = 'SR_OTC_REC_GPS_posshifts.xlsx'
sheet='Sheet1'



df_input1=pd.read_excel(os.path.join(path,file1), sheetname = sheet, encoding='latin-1')
#df_input2=pd.read_excel(os.path.join(path,file2), sheetname = sheet, encoding='latin-1')
#df_input=df_input.set_index('DATE')
#df_input.index=from_excelordinal(df_input.index)


df=df_input1.loc[df_input1['MARKETDATA_NAME']=='EUR SOVEREIGN GERMANY']
#df_USD2=df_input2.loc[df_input2['MARKET_DATA_NAME']=='USD LIBOR 3M']

#df_USD=pd.concat([df_USD1, df_USD2])

df_Pivot=df.pivot_table(index='SHIFT__VALUE', columns='GRID__POINT', values='PV_CHANGE_UAT', aggfunc='sum')







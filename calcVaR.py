# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:17:27 2018

@author: patemi
"""

import pandas as pd
import datetime as dt
import os.path
from scipy.interpolate import interp1d

import sys
sys.path.insert(0, '\\FS002\patemi$\Python\Examples\GRDB')

import grdb_shockrecords as gsr


path = '\\\\FS002\\patemi$\\Python'
file = 'PLVectors.csv'



df_input=pd.read_csv(os.path.join(path,file), encoding='latin-1', low_memory=False, parse_dates=[0])
df_input=df_input.set_index('DATE')


## Create some sample shock records and market data scenarios
SR = {'X': [-0.01,0,0.01], 
        'Y': [-50,0,50]}

Scen={'Date':[dt.date(2018,1,1),dt.date(2018,1,2),dt.date(2018,1,3)],
      'Change':[-0.005,0,0.005]}
        
# Create corrseponding dataframes
df_SR=pd.DataFrame(SR)
df_Scen=pd.DataFrame(Scen)
df_Scen=df_Scen.set_index('Date')


def PVChanges(SR,Scen):
    # Given input SRs and Scenarios, compute the PV Changes
    
    df_PVC=Scen.copy()
    df_PVC.drop(['Change'], axis=1, inplace=True)
    
    f=interp1d(SR.X,SR.Y)
    PVC=[f(v) for i,v in enumerate(Scen.Change)]
    
    df_PVC['PV Change']=PVC
    
    return df_PVC


def calcVaRQuantile(PL,CL):    
    VaR_CL=PL.quantile((100-CL)/100)
    return VaR_CL


def calcESQuantile(PL,CL):    
    ES_Vectors=PL.copy()
    VaR_CL=calcVaRQuantile(PL,CL)
    ES_CL=ES_Vectors[PL<=VaR_CL].mean()
    return ES_CL

x=PVChanges(df_SR,df_Scen)

#print(x)
#print(calcVaRQuantile(df_input,95))
#print(calcESQuantile(df_input,95))


f=gsr.getshockrecords('108-EQ-TW0112-TWD','2018-05-31','MHSC')

# Exposure ID=57577228




    
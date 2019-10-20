# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:18:01 2018

@author: patemi
"""


import numpy as np




shockpoints=[-10,0,10]
GPS=[12,10, 12]


#list50=[x for x in list1 if x > 6700]
upside_shock_points=[sp for sp in shockpoints if sp>=0]
upside_gps=[gps for sp,gps in zip(shockpoints,GPS) if sp>=0]

downside_shock_points=[sp for sp in shockpoints if sp<=0]
downside_gps=[gps for sp,gps in zip(shockpoints,GPS) if sp<=0]


PVChanges={}
PVChanges[0]=[0,0,0]

PVChanges[10]=[0,0,0]
#PVChanges[]=


#p=[x + y for x,y in zip(l1,l2)]



def pv_change(gps1,gps2,x1,x2,pv1):    
# Function to return the PV change at shock point x2 given
    #   - gps1: gps at shock point x1
    #   - gps2: gps at shock point x2
    #   - pv1 : the PV change from 0 to x1
    return pv1+(gps1+gps2)/2*(x2-x1)


#pv_change() for sp,gps in zip(shockpoints, GPS)

    
y=pv_change(GPS[0],GPS[2],0,-10,0)

upside_pv_changes=[]
upside_pv_changes[0]=0
upside_pv_changes[1]=pv_change(upside_gps[0],upside_gps[1], upside_shock_points[0],upside_shock_points[1],upside_pv_changes[0])
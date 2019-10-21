# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:09:39 2018

@author: patemi
"""

from scipy import interpolate
import numpy as np

# COB zero rates/dates 
t=np.array([0.019,
   0.08,
   0.16,
   0.25,
   0.5,
   0.75,
   1,
   2,
   3,
   5,
   7,
   10,
   12,
   15,
   20,
   25,
   30,
   40,
   50])

r_t=np.array([-0.0002800029527515,
     -0.0004856563830162,
     -0.0002762791491439,
     -0.0002225180594358,
     0.0001078854790429,
     -0.0005402575490319,
     -0.0006185014868999,
     -0.0012877269241908,
     -0.001442353259086,
     -0.0009762044111943,
     -0.0002052263824118,
     0.000887719287534,
     0.0016312478638066,
     0.0026397849800655,
     0.0039426941672609,
     0.0046303422809827,
     0.005089338207415,
     0.0055573027965191,
     0.0058379066984311])



parallelzeroweights=np.array([0.00038,
     0.00122,
     0.0016,
     0.0018,
     0.005,
     0.005,
     0.005,
     0.02,
     0.02,
     0.04,
     0.04,
     0.06,
     0.04,
     0.06,
     0.1,
     0.1,
     0.1,
     0.2,
     0.2])





dr_i = np.random.standard_normal((19, 3))


#T=2;
T=[0.019,
   0.08,
   0.16,
   0.25,
   0.5,
   0.75,
   1,
   2,
   3,
   5,
   7,
   10,
   12,
   15,
   20,
   25,
   30,
   40,
   50];



def getcurveuppergridpoints(T):
    # all items in t which are above T
    t_up=[x for x in t if x >= T]
    if not t_up:
        t_up=t[-1]
    else:
        t_up=min([x for x in t if x >= T])
    return t_up

def getcurvelowergridpoints(T):
    # all items in t which are below T
    t_dn=[x for x in t if x <= T]
    if not t_dn:
        t_dn=t[0]
    else:
        t_dn=max([x for x in t if x <= T])
    return t_dn

def S_N(R_i,T_i):        
    ''' Par Swap rates from zero rates '''
#    Inputs:     R_i: Zero rates interpolated to the swap payment times
#                T_i: Zero rate grids    

    if len(T_i)>1:    
        d_i=[0.25]*len(T_i)
    else:
        d_i=T_i
        
    P_i=np.exp(-R_i*T_i)    
    S_R=(1-P_i[-1])/np.dot(d_i,P_i)
    return S_R

# Return the weights given input shock point tenor and zero rates/times
def getshockpointweights(T,t,r_t):
# Inputs:   T: shock point tenor i.e the swap rate tenor for which we want to have the partial derivative
#           t: zero rate grid times
#           r_t: input zero rates 

    w=[]
        
    # Generate swap payment times, assuming all swaps pay quarterly fixed and floating
    if T>=0.25:
        T_i=list(np.arange(0.25,T+0.25,0.25))
    else:
        T_i=[T]
    
    index=0
    
    for r in r_t:
     #  for each input zero rate
        
        Bumps=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], np.float)   
        #Add the bump size for each zero rate tenor
        Bumps[index]=0.00005
       
        # Shifted up/down input zero rates
        r_t_up=r_t+Bumps
        r_t_dn=r_t-Bumps
        
       # print(r_t, r_t_up, r_t_dn)
        
        # Interpolated , shifted zero rates
        r_up=interpolate.interp1d(t,r_t_up, kind='linear')
        r_dn=interpolate.interp1d(t,r_t_dn, kind='linear')
        
        # Interpolated zero rates (to the swap payment times), shifted up and down
        R_i_up=r_up(T_i)
        R_i_dn=r_dn(T_i)
        
        # central difference for the partial derivative / weight
        v=(S_N(R_i_up,T_i)-S_N(R_i_dn,T_i))/(2*0.00005)
    
        #print(v)
    
        w.append(v)
        
        index+=1
    
    return w


def getweights(T,t,r_t):
# Inputs:   T: tenor point for which weights are required
#           t: year fractions for the zero rates grid points
#           r_t: zero rates
# Output    wgts: list of weights with respect to each of the zero rates r_t
    
    # Get neigbouring grid points from that which is required
    T1T2=[getcurvelowergridpoints(T),getcurveuppergridpoints(T)]

    # Neighbouring grid points to T on the zero curve, T1 and T2
    T1=T1T2[0]
    T2=T1T2[1]

    print(T1,T2)

    # dS_T1/dr_t i.e the weights of the T1 Swap rate with respect to each of the zero rates r_t
    w1=getshockpointweights(T1,t,r_t)
    
    # dS_T2/dr_t i.e the weights of the T2 Swap rate with respect to each of the zero rates r_t
    w2=getshockpointweights(T2,t,r_t)

    w=interpolate.interp2d(t,np.array([T1,T2]),np.array([w1,w2]), kind='linear')

    if T1==T2:
        wgts=w1
    else:
        wgts=w(t,T)
    return wgts



wgts=[getweights(T_i,t,r_t) for T_i in T]


# function to return the parallel swap rate weights
def getparallelswapweights(t,r_t):
#Inputs:    t: year fractions for the zero rates grid points
#           r_t: zero rates
    
    w=[]
    
    
    w=[getweights(t[i], t,r_t) for i,v in enumerate(list(t))]
    
    #print(w)
    v=np.array(w)
    return v
    





def getparratechange(dr_i,w_i):
# Inputs:   dr_i: the change in zero rates for a particular date
#           w_i: the weights (for the input swap rate SR) to be applied to each zero rate
# Outputs:  dS: the corresponding change in par/swap rate
    dS=np.dot(np.array(dr_i),np.array(w_i))
    return dS
  
def getparratechangeseries(dr_i_t,w_i):
# Inputs:   dr_i_t: the change in zero rates for a particular date
#           w_i: the weights (for the input swap rate SR) to be applied to each zero rate
# Outputs:  dS_t: the corresponding change in par/swap rate
    
    dS_t=[getparratechange(column,w_i) for column in dr_i_t.T]
    return dS_t







# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:36:09 2018

@author: patemi
"""

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt



t=[-0.02,-0.01,-0.005, -0.001,0,0.001,0.005,0.01,0.02]
#v_t=[-773134.07,-692980.15, -656143.00,-628027.14, -554547.59, -74385.13,0,0,0]

v_t=[138630066.2,65324355.05, 31596276.37, 5912873.627, 0, -3144663.565, -4632366.093, -4632366.093
, -4632366.093]


v=interpolate.interp1d(t,v_t, kind='quadratic')

#t_new=np.arange(5,12,0.1)
t_new=[-0.015,-0.0075,-0.003,-0.0005,0.0005,0.003,0.0075,0.015,0.01]
v_new=v(t_new)

plt.plot(t,v_t,'o',t_new, v_new,'-')
plt.show()


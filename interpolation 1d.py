# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:31:48 2018

@author: patemi
"""

from scipy.interpolate import interp1d, interp2d
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,num=9, endpoint=True)
y=np.cos(-x**2/9.0)


f=interp1d(x,y)
f2=interp1d(x,y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew),'--')

plt.legend(['data', 'linear', 'cubic'], loc='best')

plt.show()





# 2d interpolation

x = np.arange(-5.01, 5.01, 0.25)
y = np.arange(-5.01, 5.01, 0.25)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2+yy**2)
f = interp2d(x, y, z, kind='cubic')

xnew = np.arange(-5.01, 5.01, 1e-2)
ynew = np.arange(-5.01, 5.01, 1e-2)
znew = f(xnew, ynew)

plt.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
plt.show()
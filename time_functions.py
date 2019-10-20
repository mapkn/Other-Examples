# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:18:05 2018

@author: patemi
"""

import numpy as np
import timeit
import pandas as pd



df = pd.DataFrame(np.arange(12).reshape(4,3))



print(df.shape)
#timeit.timeit(df.shape)



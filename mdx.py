# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:35:13 2019

@author: patemi
"""

from olapy.core.mdx.executor import MdxEngine


executor = MdxEngine() # instantiate the MdxEngine
executor.load_cube('sales') # load sales cube
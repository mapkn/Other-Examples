# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:01:39 2017

@author: patemi
"""

import pandas as pd





df = pd.DataFrame([["2014", "q1"], ["2015", "q3"]],columns=('Year', 'Quarter'))

print(df)
print(df.dtypes)
print(df.Year.dtype)

# cast dataframe elements to boolean
dfb=df.astype(bool)


#to_string for a dataframe
df['Year2']=df.Year.to_string
#df['Year3']=df.Year.str


df['Period'] = df.Year.str.cat(df.Quarter)

print(df)



df2 = pd.DataFrame([[2014, 1],[2015, 3]],columns=('Year', 'Quarter'))

print(df2)


print(df2.dtypes)

print(df2.Year.dtype)

df2['Year2']=df2.Year.astype(str)


df2['Period'] = df2.Year.astype(str).str.cat(df2.Quarter.astype(str), sep='q')

print(df2)
print(df2.dtypes)


# Casting a string to a float
a="542.3"
print(float(a))

# and to an int
print(int(float(a)))


# Casting anything to a string
print(str(df['Year'].iloc[0]))
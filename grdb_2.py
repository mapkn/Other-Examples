# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:53:47 2018

@author: patemi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:05:07 2018

@author: patemi
"""

import pyodbc

import datetime

import pandas as pd


svr='APW-GRSKDB03\DB_PRD_01'
dvr='{SQL Server}'

con = pyodbc.connect('Trusted_Connection=yes', driver = dvr,server = svr)

# Create a cursor from the connection
cur = con.cursor()

#querystring = """SELECT * FROM [GlobalRisk].[MktExposure].[tbl_ShockRecord] sr WHERE sr.Date = ?"""

querystring = """SELECT * FROM [GlobalRisk].[MktRFMapping].[tbl_CountryG] cg WHERE cg.CountryG=? """


# Execute SQL statement using cursor execute
#cur.execute(querystring, [datetime.date(2018,6,25)])
#cur.execute(querystring, '2018-06-25')
#cur.execute(querystring)

df=pd.read_sql(querystring,con, params=['FR'])
# Retrieve row(s) using cursor fetch functions
#row = cur.fetchone() 

#f=getshockrecords('3140FEYC2M008',datetime.date(2018,6,25),'MSUSA')


#while row: 
#    print (row[0]) 
#    row = cur.fetchone()

    
#cur.execute(querystring)
    
# Retrieve row(s) using cursor fetch functions
#rows = cur.fetchall() 

#for row in rows:
#    print(row[0])

con.close()

  
  
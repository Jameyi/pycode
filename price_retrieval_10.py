#! usr/bin/env python
#! coding:utf-8

import pandas as pd
import pandas_datareader.data as web
import time
import datetime
import MYSQLdb as mdb
import tushare as ts

def getdatafromyahoo(startdate,enddate):
  sh = web.DataReader('000001.SS','yahoo',startdate,enddate)
  print(sh.tail(2))

def getdatafromyh(startdate,enddate):
  sh = web.get_data_yahoo('000001.SS',startdate,enddate)
  print(sh.tail(2))

def getdatafromts(startdate,enddate):
  dt = ts.get_hist_data('000001','2017-11-01','2017-11-22')
  print(dt.tail(2))
  
if __name__ == "__main__":
  startdate = datetime.datetime(2017,11,1)
  enddate = datetime.datetime.today())
  getdatafromts(startdate,enddate)
  


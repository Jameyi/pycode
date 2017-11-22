import pandas as pd
import numpy as np
from pandas_datareader import data, wb # 需要安装 pip install pandas_datareader
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
%matplotlib inline

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016,5,20)
sh = data.DataReader("000001.SS", 'yahoo', start, end)
sh.to_csv('sh.csv',header=None)
sh1 = pd.read_csv('sh.csv',names=names,index_col='Date')
sh1.tail(2)

##################################### tushare #####################

import tushare as ts

dt = ts.get_hist_data('600848') #一次性获取全部日k线数据
dt = ts.get_today_all()

############################### pandas.io ##############################
from pandas_datareader import data
import pandas.io.data as web 
web.get_data_yahoo('300481.sz','1/1/2015','20/8/2015')  

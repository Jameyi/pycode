from __future__ import print_function

import datetime
import pandas_datareader.data as web

if __name__ == "__main__":
	spy = web.DataReader("SPY","yahoo",datetime.datetime(2017,1,1),datetime.datetime.today())
	print(spy.tail())

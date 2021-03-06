#! /usr/bin/env python
#! coding:utf-8

import datetime
import requests
import MySQLdb

def get_daily_historic_data_yahoo(tiker,start_date=(2000,1,1),end_date=datetime.date.today().timetuple()[0:3]):
	
	# Obtains data from Yahoo Finance returns and a list of tuples.
	# ticker:Yahoo Finance ticker symbol,e.g. "GOOG" for Google,Inc.
	# start_date: Start date in (YYYY,M,D) format
	# end_date: End date in (YYYY,M,D) format
	
	# Construct the Yahoo URL with the correct integer query parameters
	# for start and end dates.Note that some parameters are zero_based!
	ticker_tup = (ticker,start_date[1]-1,start_date[2],start_date[0],end_date[1]-1,end_date[2],end_date[0])
	yahoo_url = "http://ichart.finance.yahoo.com/table.csv"
	yahoo_url += "?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s"
	yahoo_url = yahoo_url % ticker_tup
	
	# Try connectiong to Yahoo Finance and obtaining the data
	# On failure,print an error message.
	try:
		yf_data = requests.get(yahoo_url).text.split("\n")[1:-1]
		prices = []
		for y in yf_data:
			p = y.strip().split(',')
			prices.append((datetime.datetime.strptime(p[0],'%Y-%m-%d'),p[1],p[2],p[3],p[4],p[5],p[6]))
	except Exception as e:
		print("Could not download Yahoo data: %s" % e)
	return prices
	
	
def insert_daily_data_into_db(data_vendor_id,symbol_id,daily_data):
	# Takes a list of tuples of daily data and adds it to the
	# MySQL database. Appends the vendor ID and symbol ID to the data
	
	# daily_data:List of tuples of the OHLC data(with adj_close and volume)
	# Create the time now
	now = datetime.datetime.utcnow()
	
	# Amend the data to include the vendor ID and symbol ID
	daily_data = [(data_vendor_id,symbol_id,d[0],now,now,d[1],d[2],d[3],d[4],d[5],d[6]) for d in daily_data]
	
	# Create the insert strings
	column_str = """data_vendor_id,symbol_id,price_date,created_date,last_updated_date,open_price,high_price,low_price,close_price,volume,adj_close_price"""
	insert_str = ("%s, " * 11)[:-2]
	final_str = "INSERT INTO daily_price (%s) VALUES (%s)" % (column_str,insert_str)
	
	# Using the MySQL connection,carry out an INSERT INTO for every symbol
	with con:
		cur = con.cursor()
		cur.executemany(final_str,daily_data)

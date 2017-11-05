import re
import urllib2
import json

urlstr = 'http://fundgz.1234567.com.cn/js/001186.js?rt=1463558676006'
urlstr2 = 'http://fund.eastmoney.com/js/fundcode_search.js'
 
def jsonp2json(jsonp_str):
	try:
		return re.search('^[^(]*?\((.*)\)[^)]*$',jsonp_str).group(1)
	except:
		raise ValueError('Invalid JSONP')

html = urllib2.urlopen(urlstr)
htmlr = html.read()
hjson = jsonp2json(htmlr)
#hjson = eval(hjson)

hjson = json.loads(hjson)
print(hjson['name'])
print(hjson['fundcode'],hjson['name'],hjson['jzrq'],hjson['dwjz'],hjson['gsz'],hjson['gszzl'],hjson['gztime'])


############################################################################################################
import re
import urllib2
import json
from bs4 import BeautifulSoup as bs

urlstr = 'http://fund.eastmoney.com/allfund.html'

def jsonp2json(jsonp_str):
	try:
		return re.search('^[^(]*?\((.*)\)[^)]*$',jsonp_str).group(1)
	except:
		raise ValueError('Invalid JSONP')

def url2json(urlstr):
	html = urllib2.urlopen(urlstr)
	htmlr = html.read()
	hjson = jsonp2json(htmlr)
	hjson = json.loads(hjson)
	return hjson

if __name__ == "__main__":
	html = urllib2.urlopen(urlstr)
	bsobj = bs(html)
	divs = bsobj.findAll('div')
	for div in divs:
		for ass in div.children:
			astr = str(ass.string)
			print(type(astr))
	

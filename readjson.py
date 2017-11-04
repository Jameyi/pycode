import re
import urllib2
import json

def jsonp2json(jsonp_str):
	try:
		return re.search('^[^(]*?\((.*)\)[^)]*$',jsonp_str).group(1)
	except:
		raise ValueError('Invalid JSONP')


html = urllib2.urlopen('http://fundgz.1234567.com.cn/js/001186.js?rt=1463558676006')

htmlr = html.read()
hjson = jsonp2json(htmlr)

#hjson = eval(hjson)

hjson = json.loads(hjson)
print(hjson)

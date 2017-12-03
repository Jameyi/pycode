from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

pages = set()

def getLinks(pageUrl):
	global pages
	html = urlopen("")
	bsobj = bs(html)
	for link in bsobj.findAll("a",hreef=re.compile("")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				pages.add(newPage)
				getLinks(newPage)
	

###################################################################################
#! usr/bin/env python
#! coding:utf-8

from bs4 import BeautifulSoup as bs
import urllib2
import re

urlstr = "http://fund.eastmoney.com/"
fundcode = '161725'
position_list = []
uprise_list = []

if __name__ == "__main__":
	# 访问网页
	html = urllib2.urlopen(urlstr+fundcode+'.html?spm=search')
	# beautifulsoup 解析网页
	bsobj = bs(html)
	# itm = bsobj.find("dl",{"class":"dataItem03"}).find("span")
	# itml = bsobj.find("dl",{"class":"dataItem03"}).find("dd").find("span").get_text()
	# print(itm)
	# print(itml)
	######################找出基金的十大股票持仓并保存到列表################
	trs = bsobj.find("table",{"class":"ui-table-hover"}).findAll("tr")
	for i in range(len(trs)-1):
		position = trs[i+1].find('td').get_text()
		position_list.append(position)
	# ths = trs.findAll("th")
	# print(ths[1].get_text())
	######################找出历来涨幅并保存到列表#########################
	trs = bsobj.find("li",{"id":"increaseAmount_stage"}).findAll("tr")
	tds = trs[1].findAll("td")
	for td in tds:
		div = td.find("div",attrs={"class":re.compile("(Rdata)[a-z]*")})
		if div != None:
			uprise = div.get_text()
			uprise_num = uprise.decode('unicode-escape').encode('utf-8').replace('%','0').replace('--','0')
			uprise_list.append(float(uprise_num))
		
 












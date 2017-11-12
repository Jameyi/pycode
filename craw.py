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
	

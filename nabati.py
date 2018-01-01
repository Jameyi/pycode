#! usr/bin/env python
#! coding:utf-8

from __future__ import print_function
from bs4 import BeautifulSoup as bs
import urllib2
import re

import datetime
import MySQLdb as mdb

main_index_page = "http://fund.eastmoney.com/"
allfund_page = "http://fund.eastmoney.com/allfund.html"
htmlstr = "http://fund.eastmoney.com/f10/jbgk_"
fundcode = '000051'

def get_holdings(bsobj):
    positionlist = []
    trs = bsobj.find("table",{"class":"ui-table-hover"}).findAll("tr")
    for i in range(len(trs)-1):
        position = trs[i+1].find('td').get_text()
        positionlist.append(position)
    return (positionlist)

def get_fund_uprise(bsobj):
    uprise_list = []
    trs = bsobj.find("li",{"id":"increaseAmount_stage"}).findAll("tr")
    tds = trs[1].findAll("td")
    for td in tds:
        div = td.find("div",attrs={"class":re.compile("(Rdata)[a-z]*")})
        if div != None:
            uprise = div.get_text()
            uprise_num = uprise.decode('unicode-escape').encode('utf-8').replace('%','0').replace('--','0')
            uprise_list.append(float(uprise_num))
    return (uprise_list)

def get_info_fund(bsobj):
    manager_list = []
    manager_link = []
    trs = bsobj.find("div",{"class":"bs_gl"}).findAll("span")
    manager = bsobj.find("div",{"class":"bs_gl"}).findAll("a")
    fundnametd = bsobj.find("table",{"class":"info w790"}).findAll("td")
    fundname = fundnametd[0].get_text()
    fundsymbol = fundnametd[1].get_text()

    for i in range(len(manager)-1):
        manager_list.append(manager[i].get_text())
        manager_link.append(manager[i].attrs['href'])
    fund_begin_date = trs[0].get_text()
    fund_type = trs[1].get_text()
    fund_size = trs[2].get_text()
    return (fundname,fundsymbol,manager_list,manager_link,fund_begin_date,fund_type,fund_size)


def get_fund_code(bsobj):
    fundlinks = []
    fundcodes = []

    for lnk in bsobj.findAll("a",href=re.compile("^(http://fund.eastmoney.com/)[0-9]*\.(html)")):
        if 'href' in lnk.attrs:
            if lnk.attrs['href'] not in fundlinks:
                newfund = lnk.attrs['href']
                fundlinks.append(newfund)
                newfund = newfund.strip(' ').split('.')[2]
                newfund = newfund.strip(' ').split('/')[1]
                fundcodes.append(newfund)
    return (fundcodes)

def insert_data_into_db(daily_data):
    column_str = """fundcode,fundname,fund_type,fund_begin_date,created_date,last_update_date,accumulate_net_value,unit_net_value"""
    insert_str = ("%s," * 8)[:-2]
    final_str = "INSERT INTO fundinfo (%s) VALUES (%s)" % (columnstr,insert_str)
    with con:
        cur = con.cursor()
        cur.executemany(final_str,daily_data)



if __name__ == "__main__":

    #db_host = 'localhost'
    #db_user = 'root'
    #db_pass = 'jameyi'
    #db_name = 'fund'

    #con = mdb.connect(db_host,db_user,db_pass,db_name)
    listofposition = []
    uprise_list = []
    fundcodelist = []
    manager_list = []
    manager_link= []
    
    html = urllib2.urlopen(allfund_page)
    bsobj = bs(html,"html.parser")
    fundcodelist = get_fund_code(bsobj)
    fundcode_1 = fundcodelist[0]
    
    ################# 获取基金基本面资料 #############################
    #html_fundinfo_1 = urllib2.urlopen(htmlstr+fundcode_1+'.html')
    #bsobj_info = bs(html_fundinfo_1)
    #fundname,fundsymbol,manager_list_1,manager_link_1,fund_begin_date_1,fundtype_1,fund_size = get_info_fund(bsobj_info)

   # print(fundcode_1)
   # print(fundname)
   # print(fundsymbol)
   # print(fundtype_1)
   # print(fund_begin_date_1)
   ###################################################################

   #################### 获取基金持仓 ################################
    html_pos = urllib2.urlopen(main_index_page+fundcode_1+'.html?spm=search')
    bsobj_pos = bs(html_pos)
    listofposition = get_holdings(bsobj_pos)
    print (listofposition)
   ##################################################################

    
    #html_uprise = urllib2.urlopen(main_index_page+fundcode+'.html?spm=search')



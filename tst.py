#! usr/bin/env python
#! coding:utf-8

rstr = '10'
print(rstr,type(rstr))
res = bin(int(rstr,10))
print(res,type(res))




mysql -u root -p jameyi

CREATE DATABASE stock;
USE stock

CREATE TABLE stockinfo(
id int NOT NULL AUTO_INCREMENT,
stockcode varchar(6) NOT NULL,
stockname varchar(255) NULL,
ticker varchar(32) NULL,
instrument varchar(32) NULL,
sector varchar(128) NULL,
currency NULL,
created_date datetime NOT NULL,
last_update_date datetime NOT NULL,
PRIMARY KEY(id)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

###########################################################################
fundinfo
(
row:eachfund;
column:
id int not null, found  (1)
fundcode varchar(6) not null, found (000001)
fundname varchar(255) null,  (基金久嘉）[nabati.get_info_fund()]
fundtype varchar(6) null, found （指数联接）[nabati.get_info_fund()]
listed_date datetime null, found （2009-07-10）[nabati.get_info_fund()]
created_date datetime not null,（now）
last_update_date datetime null,（now）
accumulate_net_value decimal(6,4) null, （3.17）
unit_net_value decimal(6,4) null, （1.17）
stock_position_1_code varchar(6) null, found  [五粮液 nabati.getholdings()]
stock_position_percentage_1 decimal(5,4) null, 7%
stock_position_2_code varchar(6) null, found [nabati.getholdings()]
stock_position_percentage_2 decimal(5,4) null,
stock_position_3, found   [nabati.getholdings()]
stock_position_percentage_3,
stock_position_4, found   [nabati.getholdings()]
stock_position_percentage_4,
stock_position_5, found   [nabati.getholdings()]
stock_position_percentage_5,
stock_position_6, found   [nabati.getholdings()]
stock_position_percentage_6,
stock_position_7, found   [nabati.getholdings()]
stock_position_percentage_7,
stock_position_8, found   [nabati.getholdings()]
stock_position_percentage_8,
stock_position_9, found   [nabati.getholdings()]
stock_position_percentage_9,
stock_position_10, found  [nabati.getholdings()]
stock_position_percentage_10,
last_week_uplift decimal(5,4) null, found  [1% nabati.getfund_uprise()] 
last_month_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
last_threemonth_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
last_sixmonth_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
this_year_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
last_year_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
last_twoyear_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
last_threeyear_uplift decimal(5,4) null, found [1% nabati.getfund_uprise()] 
period_profit_1
period_profit_2
period_profit_3
period_profit_4
period_return_1
period_return_2
period_return_3
period_return_4
period_unit_uplift_1
period_unit_uplift_2
period_unit_uplift_3
period_unit_uplift_4
final_return_for_distribution_1
final_return_for_distribution_2
final_return_for_distribution_3
final_return_for_distribution_4
final_returnfund_for_distribution_1
final_returnfund_for_distribution_2
final_returnfund_for_distribution_3
final_returnfund_for_distribution_4
final_accumulated_upliftpercentage_fund_1
final_accumulated_upliftpercentage_fund_2
final_accumulated_upliftpercentage_fund_3
final_accumulated_upliftpercentage_fund_4

61 rows

########################################################################################################################
symbol table(row:eachstock; column:id,exchang_id,ticker,instrument,name,sector,currency,created_date,last_update_date)

info_in_day table(row:eachstock;column:open,high,low,close,limit_up,limit_down,volume,total_turnover)

stock_timestamp table(row:eachtimestamp,column:price,volume,turnover,buy1,sell1,buy2,sell2,buy3,sell3,buy4,sell4,buy5,sell5)

stock_day table(row:eachday,column:open,high,low,close,limit_up,limit_down,volume,turnover)

open table(row:date; cloumn:eachticker)
high table(row:date; cloumn:eachticker)
low table(row:date; cloumn:eachticker)
limit_up table(row:date; cloumn:eachticker)
limit_down table(row:date; cloumn:eachticker)
volume table(row:date; cloumn:eachticker)
total_tunover table(row:date; cloumn:eachticker)
                              
                              

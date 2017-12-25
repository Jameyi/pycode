#! usr/bin/env python
#! coding:utf-8

rstr = '10'
print(rstr,type(rstr))
res = bin(int(rstr,10))
print(res,type(res))

mysql -u root -p jameyi

CREATE DATABASE fund;
USE fund

CREATE TABLE fundinfo(
id int NOT NULL AUTO_INCREMENT,
fundcode varchar(6) NOT NULL,
fundname varchar(255) NULL,
fundtype varchar(6) NULL,
listed_date datetime NULL,
created_date datetime NOT NULL,
last_update_date datetime NULL,
accumulate_net_value decimal(6,4) NULL,
unit_net_value decimal(6,4) NULL,
stock_position_1_code varchar(6) NULL,
PRIMARY KEY(id)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

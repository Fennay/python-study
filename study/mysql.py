#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb

connect = MySQLdb.connect(host='127.0.0.1', user='root', password='Tgrnf', db='test',charset="utf8mb4")
cursor = connect.cursor()
sql = "insert into `article` (`title`,`url`,`author`,`tags`,`view`,`answer`) values ('dvajs Model几个疑问🤔️','1werwasdf','rrrr','123123','4555','66666')"
rs = cursor.execute(sql)
connect.commit()
print(rs)

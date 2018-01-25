# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
import MySQLdb


class SfPipeline(object):
    def process_item(self, item, spider):
        save(item)
        # return item


def save(item):
    # print('----------------看这里------------')
    saveData = []
    tupleData = tuple(item.values())
    saveData.append(tupleData)
    saveData = tuple(saveData)
    mysql = MySqlDBHelper(host='127.0.0.1', user='root', password='Tgrnf', dbname='test')
    mysql.insertAll('article', saveData)


class MySqlDBHelper(object):
    def __init__(self, host, user, password, dbname, port=3306, charset="utf8mb4"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = dbname
        self.charset = charset

    def connect(self):
        try:
            connect = MySQLdb.connect(host=self.host,
                                      user=self.user,
                                      password=self.password,
                                      port=self.port,
                                      db=self.db,
                                      charset=self.charset)
        except MySQLdb.OperationalError:
            raise Exception("数据库连接失败")
        else:
            return connect

    def insertAll(self, table, data):
        # 连接insertAll数据库
        try:
            conn = self.connect()
        except Exception as e:
            raise Exception(e)
        else:
            cursor = conn.cursor()
        # 插入数据
        try:
            sql = 'insert into ' + table + ' (title,url,author,tags,view,answer) values(%s,%s,%s,%s,%s,%s)'
            result = cursor.executemany(sql, data)
            conn.commit()
        except MySQLdb.MySQLError as e:
            raise Exception(e)
        else:
            return result
        finally:
            conn.close()

    def select(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            result = cursor.execute('select * from `article`')
        except MySQLdb.MySQLError as e:
            raise Exception(e)
        else:
            return result
        finally:
            conn.close()

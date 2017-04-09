#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='192.168.*.*', user='admin',
                       passwd='*',
                       db='xiaoming')
cur = conn.cursor()
# cur.execute(
#     "insert into student (name, age, register_date) VALUES ('Tom', 20, '2016-06-06')")
# cur.execute(
#     "insert into student (name, age, register_date) VALUES ('Lucy', 18, '2016-06-07')")

cur.execute("SELECT * FROM student")

for r in cur.fetchall():
    print(r)

conn.close()

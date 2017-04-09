#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

data = [
    ('Jim', 12, '2017-01-01'),
    ('Harry', 13, '2017-01-01'),
    ('Oliver', 14, '2017-01-01'),
    ('kate', 15, '2017-01-01'),
]

conn = pymysql.connect(host='192.168.*.*', user='admin', passwd='*',
                       db='xiaoming')
cursor = conn.cursor()

cursor.executemany(
    'insert into student (name, age, register_date) VALUES (%s, %s, %s)', data)

conn.close()

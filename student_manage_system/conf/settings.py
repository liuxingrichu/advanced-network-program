#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://admin:123@192.168.31.100/testdb",
                       encoding='utf-8',
                       # echo=True
                       )

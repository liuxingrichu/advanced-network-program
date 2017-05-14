#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://admin:*@192.168.*.*/testdb",
                       encoding='utf-8',
                       # echo=True
                       )

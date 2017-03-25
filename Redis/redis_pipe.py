#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import time

'''
    使用pipeline实现一次请求,执行多条命令
'''

# db的选择范围为0-15
pool = redis.ConnectionPool(host='localhost', port=6379, db=12)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'Tom')
time.sleep(30)
pipe.set('role', 'teacher')

pipe.execute()

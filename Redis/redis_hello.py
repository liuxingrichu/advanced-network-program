#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

res = redis.Redis(host='localhost', port=6379)
res.set('foo', 'Bar')
print(res.get('foo'))

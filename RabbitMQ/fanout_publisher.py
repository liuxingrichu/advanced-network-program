#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika
import sys

'''
    广播模式fanout: 所有bind到此exchange的queue都可以接收消息
'''

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

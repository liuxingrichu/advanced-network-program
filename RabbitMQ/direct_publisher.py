#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika
import sys

'''
    广播模式direct，通过routingKey和exchange决定的那个唯一的queue可以接收消息
    有选择的接收消息(exchange type=direct)　
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()

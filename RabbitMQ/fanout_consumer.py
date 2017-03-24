#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika

'''
    广播模式fanout: 所有bind到此exchange的queue都可以接收消息
'''

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

# 不指定queue名字,rabbit会随机分配一个名字,
# exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

print('queue_name : ', queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. ')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

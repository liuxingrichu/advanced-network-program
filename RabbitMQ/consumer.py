#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# You may ask why we declare the queue again?
#  we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists.
# For example if send.py program was run before.
# But we're not yet sure which program to run first.
# In such cases it's a good practice to repeat declaring the queue in both programs.
# durable=True服务器和客户端都需要写，此处durable=True仅能保证, 服务器宕机后，队列持久化
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    print('--->', ch, method, properties)
    # time.sleep(30)
    print(" [x] Received %r" % body)
    # 消息确认
    ch.basic_ack(delivery_tag=method.delivery_tag)

#消息处理完成后再接收，仅需要添加在客户端即可
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='hello',
                      # no_ack=True #无反馈
                      )

print(' [*] Waiting for messages.')
channel.start_consuming()

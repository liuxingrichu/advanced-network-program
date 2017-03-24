#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明queue
# durable=True服务器和客户端都需要写此处durable=True仅能保证, 服务器宕机后，队列持久化
channel.queue_declare(queue='hello', durable=True)

# n RabbitMQ a message can never be sent directly to the queue,
# it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      # 消息持久化，即保证服务器宕机后，消息还存在
                      # 仅服务器端写即可，
                      properties=pika.BasicProperties(delivery_mode=2, ),
                      )
print(" [x] Sent 'Hello World!'")
connection.close()

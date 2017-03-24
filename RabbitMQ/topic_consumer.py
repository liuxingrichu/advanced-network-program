#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika
import sys

'''
    广播模式topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
    更细致的消息过滤

　　 表达式符号说明：#代表一个或多个字符，*代表任何字符
      例：
        # 可收所有信息
        #.a会匹配a.a，aa.a，aaa.a等
        *.a会匹配a.a，b.a，c.a等
     注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout　
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

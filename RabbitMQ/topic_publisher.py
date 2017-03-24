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

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

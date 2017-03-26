#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key='127.0.0.1')


def request(ch, method, props, body):
    response = """--------------- %s ----------------------------
        %s---------------------------------------------------
    """ % (method.routing_key, os.popen(body.decode()).read())

    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=response)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(request,
                      queue=queue_name,
                      no_ack=True)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

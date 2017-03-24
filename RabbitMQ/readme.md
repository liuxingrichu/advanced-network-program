
线程queue
【应用场景】多线程之间数据交互
进程Queue
【应用场景】
（1）父子进程间数据交互
（2）同一父进程下，多个子进程间数据交互

实现不同进程间通信的方式：
（1）socket
（2）硬盘
（3）第三方代理，例如
    RabbitMQ
    ZeroMQ
    ActiveMQ


RabbitMQ
【应用场景】多进程间数据交互


RabbitMQ学习环境：
（1）安装erlang，下载网址http://www.erlang.org/downloads
（2）安装RabbitMQ，下载网址http://www.rabbitmq.com/download.html
（3）安装python的pika模块

dos中查看消息情况：
    RabbitMQ Server\rabbitmq_server-3.6.8\sbin
    rabbitmqctl.bat list_queues

windows services.msc

参看https://www.cnblogs.com/alex3714/articles/5248247.html







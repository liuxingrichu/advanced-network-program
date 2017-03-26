
可以对指定机器异步的执行多个命令
例子：
>>:run "df -h" --hosts 192.168.3.55 10.4.3.4
task id: 45334
>>: check_task 45334
>>:
注意，每执行一条命令，即立刻生成一个任务ID,不需等待结果返回，
通过命令check_task TASK_ID来得到任务结果


远程主机（linux设备）作为RabbitMQ服务的配置要求：
（一）远程主机的rabbitMQ添加账号并赋予权限：
    (1)rabbitmqctl add_user admin admin
    (2)rabbitmqctl set_user_tags admin administrator
    (3)rabbitmqctl set_permissions -p "/" admin ".*" ".*" ".*"

（二）在远程主机上开启端口
    （1）使用该执行打开端口文件
        vi /etc/sysconfig/iptables
    （2）随便复制一行现有内容，将你要打开的端口设置上就行了，这里是打开5672端口
        -A INPUT -m state --state NEW -m tcp -p tcp --dport 5672 -j ACCEPT
    （3）输入:wq保存退出
    （4）service iptables restart，使设置生效

（三）配置外部访问配置文件
    /etc/rabbitmq/rabbitmq.config
    [
    {rabbit, [{tcp_listeners, [5672]}, {loopback_users, ["admin"]}]}
    ].

（四）重启rabbitMQ
    #service rabbitmq-server restart


参看http://www.cnblogs.com/dwf07223/p/3991591.html

http://www.open-open.com/lib/view/open1432468144338.html


通过广播模式通知运行主机

形式：
    执行命令
        run 命令 --hosts 主机
        例如run "df -h" --hosts 192.168.3.55 10.4.3.4
        注：主机数量至少一个
    查看运行结果
        check_task xx-id


运行环境：
    管理机和运行机都安装并启动rabbitMQ
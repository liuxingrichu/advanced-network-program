
常用数据库：
Oracle      甲骨文     收费
mysql       甲骨文     免费、开源
SQL server  微软
DB2         IBM
postgresql            免费
sqlite                轻量级、免费
access                轻量级

CentOS安装mysql
    查询与卸载
        #rpm -qa | grep mysql　　查看操作系统，是否安装mysql数据库
        #rpm -e mysql　　普通删除模式
        强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，
        则用该命令可以对其进行强力删除
        #rpm -e --nodeps mysql　
    查看与安装
        #yum list | grep mysql 查看提供的mysql数据库，可下载的版本
        #yum install -y mysql-server mysql mysql-devel 安装
        #rpm -qi mysql-server 查看版本
    初始化及相关配置
        #service mysqld start
        #chkconfig --list | grep mysqld 查看是否开机自启动
        #chkconfig mysqld on 设置开机启动


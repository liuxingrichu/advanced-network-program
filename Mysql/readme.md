
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
		
	添加账号和登陆
		#/usr/bin/mysqladmin -u root password root123　　设置mysql的root账号密码
		#mysql -u root -p 登录数据库
		#exit	退出数据库

	主要配置文件
		/etc/my.cnf 主配置文件
		/var/lib/mysql   数据库文件存放位置
		/var/log 日志存放位置
		
	数据库端口
		#netstat -anp| grep 3306 
		
	基本操作
		mysql> show databases;
		mysql> create database [name];	创建数据库
		mysql> use [databasename];
		mysql> show tables;
		mysql> INSERT INTO user
				  (host, user, password,
				   select_priv, insert_priv, update_priv)
				   VALUES ('localhost', 'guest',
				   PASSWORD('guest123'), 'Y', 'Y', 'Y');
		 FLUSH PRIVILEGES;
		mysql> SELECT host, user, password FROM user WHERE user = 'guest';

			选择要操作的Mysql数据库，使用该命令后所有Mysql命令都只针对该数据库。
		mysql>USE 数据库名;
			列出 MySQL 数据库管理系统的数据库列表。
		mysql>SHOW DATABASES;
			显示指定数据库的所有表，使用该命令前需要使用 use命令来选择要操作的数据库。
		mysql>SHOW TABLES;
			显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息。
		mysql>SHOW COLUMNS FROM 数据表;
			创建一个叫testdb的数据库，且让其支持中文
		mysql>create database testdb charset "utf8";
			删除数据库
		mysql>drop database testdb;
			显示数据表的详细索引信息，包括PRIMARY KEY（主键)
		mysql>SHOW INDEX FROM 数据表;


python安装mysql
	pip install pymysql
	
		
		
		

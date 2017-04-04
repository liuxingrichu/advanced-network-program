
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
		mysql> exit	退出数据库

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
		mysql> FLUSH PRIVILEGES;
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
		
		查看表结构
		mysql> desc table_name;
		查看表结构的创建记录
		mysql> show create table table_name;
		
		插入数据表
			语法
			CREATE TABLE table_name (column_name column_type);
			举例
			mysql> create table student(
			   stu_id INT NOT NULL AUTO_INCREMENT,
			   name CHAR(32) NOT NULL,
			   age  INT NOT NULL,
			   register_date DATE,
			   PRIMARY KEY ( stu_id )
			);
			
		语法
		select column_name from table_name [where (column_name condition)] [order by column_name desc] [group by column_name]
		

		查询
			显示全部表信息	
			mysql> select * from student;	*代表全部
			从第2个位置，开始显示3条表信息
			mysql> select * from student limit 3 offset 2;	
			指定满足条件的表信息显示	
			mysql> select * from student where register_date > '2016-03-05';	
			模糊查询		
			mysql> select * from student where name like "%Li";	 %代表任意字符，%Li表示name已Li结尾的全部满足条件

		更新
			更新满足条件的表信息
			mysql> update student set age=20, name='Tom' where stu_id > 4;	
			修改字段类型
			mysql> alter table student modify age int(2);
			修改字段名及类型
			mysql> alter table student change age new_age int;
			修改表名
			mysql> alter table student rename to student_new;

		添加
			添加一列（数据元素）
			mysql> alter table student add age int(3) not null;
		
		
		删除
			删除满足条件的表信息
			mysql> delete from student where stu_id=6;	
			删除一列（数据元素）
			mysql> alter table student drop age;
		
		排序
			对满足条件的表信息进行降序排序		
			mysql> select * from student where name like "%Li" order by stu_id desc;	

		分组统计
			按照指定条件进行表信息统计
			mysql> select name, count(*) from student group by name;	
			按照指定条件进行表信息统计，同时统计整个数据
			mysql> select coalesce(name,'total') as name, count(*)  as count from student group by name with rollup;		


		外键
			实现主键自增
			mysql> alter table student2 modify id int auto_increment;


python安装mysql
	pip install pymysql
	
		
		
		

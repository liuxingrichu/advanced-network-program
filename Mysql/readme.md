
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
			删除表
		mysql> drop table student;
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


		外键（暂时验证无效）
				实现主键自增
			mysql> alter table student modify id int auto_increment;
				创建student表
			mysql> 
				create table student(
				id int(11) not null auto_increment,
				name char(32) not null,
				age int not null,
				register_date date not null,
				primary key (id));
				创建study_record表
			mysql> 
				create table `study_record` (
				`id` int(11) not null auto_increment,
				`day` int not null,
				`status` char(32) not null,
				`stu_id` int(11) not null,
				primary key (`id`),
				key `fk_student_key` (`stu_id`),
				constraint `fk_student_key` foreign key (`stu_id`) REFERENCES `student` (`id`)
				);
				向student表中插入信息
			mysql> insert into student (name, age, register_date) values('Lucy', 19, '2017-04-02');
				向study_record表中插入信息
			mysql> insert into study_record (day, status, stu_id) values (1, 'Yes', 2);
			
		跨表查询
			创建两表
				mysql> create table A (a int not null);
				mysql> create table B (b int not null);
			插入数据
				mysql> insert into A (a) values (1);
				mysql> insert into A (a) values (2);
				mysql> insert into A (a) values (3);
				mysql> insert into A (a) values (4);
				mysql> insert into B (b) values (3);
				mysql> insert into B (b) values (4);
				mysql> insert into B (b) values (5);
				mysql> insert into B (b) values (6);
			交集（两表中取两列相同的内容）
				mysql> select * from A inner join B on A.a = B.b;
				mysql> select A.*, B.* from A, B where A.a = B.b;
			差集（先将A.a的内容全部打印，再找B.b中内容，存在NULL的表示两种的差集（A.a-B.b））
				mysql> select * from A left join B on A.a = B.b;
			差集（先将B.b的内容全部打印，再找A.a中内容，存在NULL的表示两种的差集（B.b-A.a））
				mysql> select * from A right join B on A.a = B.b;
			并集
				mysql> select * from A right join B on A.a = B.b union select * from A left join B on A.a = B.b;
				mysql> select * from A full join B on A.a = B.b;（mysql不支持）
				
		事务（暂时验证无效）
			一般来说，事务是必须满足4个条件（ACID）： Atomicity（原子性）、Consistency（稳定性）、Isolation（隔离性）、Durability（可靠性）。
			1、事务的原子性：一组事务，要么成功；要么撤回。
			2、稳定性 ： 有非法数据（外键约束之类），事务撤回。
			3、隔离性：事务独立运行。一个事务处理后的结果，影响了其他事务，那么其他事务会撤回。事务的100%隔离，需要牺牲速度。
			4、可靠性：软、硬件崩溃后，InnoDB数据表驱动会利用日志文件重构修改。可靠性和高速度不可兼得， innodb_flush_log_at_trx_commit选项 决定什么时候吧事务保存到日志里。
			mysql> begin;	开启事务
			mysql> insert into student (name, age, register_date) values ('David', 12, '2017-04-6');
			mysql> rollback;	撤回
			mysql> commit;	确认提交，无法再撤回
		
		索引
			查看索引
				mysql> show index from student;
			创建索引
				CREATE INDEX indexName ON mytable(username(length)); 
				mysql> create index index_name on student(name(32));
			删除索引
				mysql> drop index index_name on student;
			
python安装mysql
	pip install pymysql
	
		
参见https://www.cnblogs.com/alex3714/articles/5950372.html
		
授权Mysql远程访问
	mysql> grant all on *.* to admin@'localhost' identified by 'password';
	mysql> grant all on *.* to admin@'%' identified by 'password';
	mysql> flush privileges;

查看数据使用端口情况
mysql> show global variables like 'port';

	
问题：pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.***.***' (timed out)")	
解决方法：
	（1）关闭防火墙
	（2）配置3306端口可以通过防火墙


CentOS关闭防火墙
	1、重启后永久性生效：
	开启：chkconfig iptables on
	关闭：chkconfig iptables off
	2、即时生效，重启后失效：
	开启：service iptables start
	关闭：service iptables stop
	3 查看防火墙状态
	# service iptables status
		
Centos配置3306通过防火墙
	#vim /etc/sysconfig/iptables
	-A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT
	注：添加在22的下面
	
参看http://www.centoscn.com/CentOS/help/2014/1030/4021.html
	

查看用户清单
	mysql> use mysql
	mysql> select user, password, host from user;


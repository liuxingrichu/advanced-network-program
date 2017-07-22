创建数据库
mysql> create database JPdb charset utf8;

删除表
mysql> drop table remote_user;

删除数据库
mysql> drop database JPdb;

查看表结构
mysql> desc remote_user;

安装yaml包
pip install pyyaml

pycharm运行参数
    无
    syncdb
    create_hosts -f ..\share\examples\new_hosts.yml
    create_remoteusers -f ..\share\examples\new_remoteusers.yml
    create_fortressusers -f ..\share\examples\new_fortressusers.yml
    create_groups -f ..\share\examples\new_groups.yml


查看数据
mysql> select * from host;

删除指定数据
mysql> delete from remote_user where auth_type like 'ssh-passwd';


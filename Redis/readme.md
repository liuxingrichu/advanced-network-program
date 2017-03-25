需求：
    多进程间缓存共享
实现方式：
 （1）mongodb
 （2）redis
 （3）memcache 轻量级


 windows7 64位系统下，配置redis环境：
    下载地址https://github.com/ServiceStack/redis-windows/tree/master/downloads
    参看http://www.cnblogs.com/koal/p/5484916.html

redis的服务器和客户端互动：
（1）将下载好的压缩包，解压
（2）dos窗口（cmd）进入到redis目录下
（3）启动服务器：运行redis-server.exe 或 redis-server.exe redis.windows.conf
（4）启动客户端：运行redis-cli.exe
（5）若有密码，执行auth 密码
（6）set name Jack
（7）set name Jack ex 2 #存活2秒
（8）get name
（9）keys *
（10）help set #获取帮助信息
（11）select db_number # db_number范围为0-15

python与redis互动：
（1）python安装redis模块
（2）参见http://www.cnblogs.com/alex3714/articles/6217453.html

应用举例：
    统计多用户（上亿人）场景下，在线用户数量及用户名
    #setbit num user_id 1
    #bitcount num
    #getbit num user_id

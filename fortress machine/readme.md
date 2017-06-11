paramiko源代码
https://github.com/paramiko/paramiko


<1> paramiko支持python3，修改代码如下
运行程序
D:paramiko-master\demos>python demo.py
Hostname: 192.168.*.*
*** Unable to open host keys file
*** WARNING: Unknown host key!
Username [Administrator]: root
Auth by (p)assword, (r)sa key, or (d)ss key? [p]
Password for root@192.168.*.*:
*** Here we go!

Line-buffered terminal emulation. Press F6 or ^Z to send EOF.

Exception in thread Thread-3:
Traceback (most recent call last):
  File "D:\Program Files (x86)\Python35\lib\threading.py", line 914, in _bootstr
ap_inner
    self.run()
  File "D:\Program Files (x86)\Python35\lib\threading.py", line 862, in run
    self._target(*self._args, **self._kwargs)
  File "D:\Program Files (x86)\GitHub\advanced-network-program\paramiko-master\d
emos\interactive.py", line 84, in writeall
    sys.stdout.write(data)
TypeError: write() argument must be str, not bytes


【原因】
python3的标准输出默认是字节形式，而python2为字符串形式。
【方法】
修改File "D:\Program Files (x86)\GitHub\advanced-network-program\paramiko-master\d
emos\interactive.py", line 84为
    sys.stdout.write(data.decode())


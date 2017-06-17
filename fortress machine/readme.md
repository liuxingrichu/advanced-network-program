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

<2>异常定位
import traceback
traceback.print_exc()


<3>python在linux环境上，缩进错误
环境：CentOS 6.7
操作：在python代码中，添加代码，运行python程序，报错。
错误：TabError: inconsistent use of tabs and spaces in indentation
原因：python的缩进要求，tab键不能用于缩进。
方法：将tab键转换成空格键，或者直接用空格进行缩进

<4>ssh连接后，自动运行程序
$ vim ~/.bashrc
python3 /home/testf/paramiko-master/demos/demo.py
$ . .bashrc 

<5>【功能】记录用户行为
# vim /home/paramiko-master/demos/interactive.py

def posix_shell(chan):
    import select

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
		---------------------------------
		cmd = []
		---------------------------------
		while True:
			r, w, e = select.select([chan, sys.stdin], [], [])
			if chan in r:
				try:
					x = u(chan.recv(1024))
					if len(x) == 0:
						sys.stdout.write('\r\n*** EOF\r\n')
						break
					sys.stdout.write(x)
					sys.stdout.flush()
				except socket.timeout:
					pass
			if sys.stdin in r:
				x = sys.stdin.read(1)
				if len(x) == 0:
					break
		------------------------------------			
				if x == '\r':
				   cmd_str = "".join(cmd)
				   print('--->', cmd_str)
				   cmd = []
				else:
				   cmd.append(x)
		------------------------------------		   
				chan.send(x)
	finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

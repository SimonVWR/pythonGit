import psutil
print(psutil.cpu_count())       #超线程
print(psutil.cpu_count(logical=False))  #核心

print(psutil.cpu_times())       #cpu使用
print(psutil.virtual_memory())  #物理内存

print(psutil.disk_partitions())     #磁盘分区
print(psutil.disk_usage('/'))   #磁盘使用率， 貌似只有第一个硬盘

print(psutil.net_io_counters()) # 获取网络读写字节／包的个数

print(psutil.net_connections()) #获取当前网络连接信息
print(psutil.pids()) # 所有进程ID
print(psutil.Process(1068).status() ) #进程1068的状态



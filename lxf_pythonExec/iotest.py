# -*- encoding: utf-8 -*-
# fpath = r'C:\Windows\system.ini'
# with open(fpath, 'r') as f:
#     print(f.read())

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
def printdir(inputpath):
    rawpath = inputpath
    subdir = [x for x in os.listdir(rawpath) if
              os.path.isdir(os.path.join(rawpath, x))]  # listdir仅返回名称，不带原路径
    for perdir in subdir:
        print(perdir)
        printdir(os.path.join(rawpath,perdir))


printdir(r'g:\迅雷下载')

# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    def char2num(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]

    def fn(x, y):
        return x * 10 + y

    st = s.partition('.')
    print(st)
    if s.index('.')==-1:
        return reduce(fn, map(char2num, st[0]))
    else:
        prestr = reduce(fn, map(char2num, st[0]))
        poststr = reduce(fn, map(char2num, st[2]))
        for i in range(0, len(st[2])):
            poststr /= 10
        return prestr+poststr

print('str2float(\'123.456\') =', str2float('123456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

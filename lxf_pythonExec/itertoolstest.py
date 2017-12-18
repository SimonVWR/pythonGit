# -*- coding: utf-8 -*-
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:

    # 方法1： count（1）
    # natuals = itertools.count(1)
    # ns = itertools.takewhile(lambda x: x <= N, natuals)
    # return sum(map(lambda x: ((-1) ** (x - 1)) * 4 / (2 * x - 1), ns))

    #方法2： count(2)
    odd_list = list(itertools.takewhile(lambda x: x < N*2+1, itertools.count(1, 2)))
    trans_seq = map(lambda x: -4.0/x if odd_list.index(x) % 2 != 0 else 4.0/x, odd_list)
    return sum(trans_seq)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
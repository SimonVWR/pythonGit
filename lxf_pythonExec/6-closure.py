# -*- coding: utf-8 -*-
#利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
   n=0
   def counter():
       nonlocal n
       n +=1
       return n
   return counter

   # #定义一个迭代器 无限
   # def _itr_n():
   #     n=0
   #     while True:
   #         n+=1
   #         yield n
   # #定义函数获取迭代器的值，闭包
   # g = _itr_n()
   #
   # def getn():
   #     return next(g)
   # return getn

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

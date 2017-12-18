# -*- encoding: utf-8 -*-
# iterator 奇数
def _odd_itr():
    n=1
    while True:
        n=n+2
        yield n

# x不能被n整除，则返回True，否则返回False；lambda函数引入了另一个参数x
def _not_divison(n):
    return lambda x:x%n>0

def prime():
    n = 2
    yield n
    it = _odd_itr()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divison(n), it)

# for n in range(100):
#     print(next(prime()))

itprime = prime()
for n in range(100):
    print(next(itprime))






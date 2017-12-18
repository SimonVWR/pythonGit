def _itr_n():
    n = 0
    while True:
        n += 1
        yield n


# 定义函数获取迭代器的值，闭包
g = _itr_n()
print(next(g))
print(next(g))


#枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name, '   ', member.value)


#元类
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
# Hello, world.
print(type(Hello))
# <class 'type'>
print(type(h))
# <class '__main__.Hello'>

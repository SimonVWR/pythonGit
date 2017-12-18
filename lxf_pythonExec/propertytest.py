# -*- encoding: utf-8 -*-
from types import MethodType
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        self._width=val

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val):
        self._height = val

    @property
    def resolution(self):
        return self._width*self._height
#绑定方法
def set_name(self, name):
    self.__name = name

# 测试:
#Screen.set_name=set_name  #类绑定方法  #放置在这里和s生成后没有影响，只要在调用s.set_name之前就可以
s = Screen()
Screen.set_name=set_name  #类绑定方法
#s.set_name = MethodType(set_name, s)   #实例绑定方法

print('width = ', s.width)  # 异常 AttributeError: 'Screen' object has no attribute '_width'

s.width = 1024
s.height = 768

s.set_name('name_1')
print(s.__name)

print(hasattr(s, 'resolution'))
print(getattr(s, 'resolution'))

print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
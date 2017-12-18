# -*- encoding: utf-8 -*-
import time,functools
#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# 在函数调用的前后打印出'begin call'和'end call'的日志。
def metric(msg):
    print('metric begin call')
    def decorator(fn):
        print('decorator begin call')
        @functools.wraps(fn)  # @functools.wraps(func)
        def owpper(*args, **kw):
            print('owpper begin call')
            def wrapper():
                print('wrapper begin call')
                print('%s %s executed in %s ms' % (msg, fn.__name__, 10.24))
                print('wrapper end call')
                return fn(*args, **kw)
            print('owpper end call')
            return wrapper
        print('decorator end call')
        return owpper
    print('metric end call')
    return decorator

# 测试
print('def start...')
@metric('fast')
def fast(x, y):
    time.sleep(0.0012)
    return x + y

print('exec start...')
f = fast(11, 22)()
print('f= ',f)
if f != 33:
    print('测试失败!')


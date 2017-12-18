#请写一个能处理去掉=的base64解码函数：
# -*- coding: utf-8 -*-
import base64
def safe_base64_decode(s):
    inba = s
    if not len(inba) %4 == 0:
        lendelta = 4 - len(inba)%4
        for i in range(0,lendelta):
            inba = inba+b'='
    return base64.b64decode(inba)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。#
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

# -*- coding: utf-8 -*-
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    def calc_md5(password):
        md5pwd = hashlib.md5()
        md5pwd.update(password.encode('utf-8'))
        return md5pwd.hexdigest()
    if db[user] == calc_md5(password):
        return  True
    return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
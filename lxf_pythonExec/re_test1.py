# -*- coding: utf-8 -*-
import re
# 测试:
def name_of_email(emaltxt):
    pattern = re.compile(r'^\<?([\w\s\.]+)\>?\s?([a-zA-Z\.]*)@([\w0-9]+)\.([\w]{3})$')
    res = pattern.match(emaltxt)
    if res:
        print(res.groups())
        if len(res.groups())>1:
            return  res.group(1)
    return None

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
name_of_email('bill.gates@microsoft1.com')
name_of_email('bob#example.com')
name_of_email('mr-bob@example.com')

print('ok')


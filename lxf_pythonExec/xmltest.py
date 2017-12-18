# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
# 参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request
import json
class xmlhandler(object):
    def __init__(self):
        pass
        self.dictRslt = dict()  #{}

    def startElement(self, name, attrs):
        print('name=', name, 'attrs=', str(attrs))
        self.dictRslt[name] = str(attrs)
        for k,v in attrs.items():  #实际attrs已经是dict了
            self.dictRslt[k]=attrs[k]
        pass

    def endElement(self, name):
        pass

    def charElement(self, text):
        pass

def parseXml(xml_str):
    print(xml_str)
    xmlpas = xmlhandler()
    parserr = ParserCreate()
    parserr.StartElementHandler = xmlpas.startElement
    parserr.EndElementHandler = xmlpas.endElement
    parserr.CharacterDataHandler  = xmlpas.charElement
    parserr.Parse(xml_str)

    return xmlpas.dictRslt

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
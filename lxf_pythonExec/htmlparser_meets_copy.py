from html.parser import HTMLParser
from urllib import request

class Meet(object):
    def __init__(self, name, location, time):
        self._name = name
        self._loc = location
        self._time = time
        
    @property
    def mname(self):
        return self._name
    
    @mname.setter
    def mname(self, name):
        self._name = name

    @property
    def mloc(self):
        return self._loc

    @mloc.setter
    def mloc(self, loc):
        self._loc = loc

    @property
    def mtime(self):
        return self._time

    @mtime.setter
    def mtime(self, time):
        self._time = time

    def __str__(self):
        return 'Meet=%s %s %s'%(self._name, self._loc, self._time)

    __repr__ = __str__

#空置的meet list,等待填充
meets = []

class MyHtmlParser(HTMLParser):
    title_w = False
    location_w = False
    time_w = False
    title, time, location = "", "", ""

    def handle_starttag(self, tag, attrs):
        if tag == "h3" and len(attrs) and 'event-title' in attrs[0]:  # 可以写入title
            self.title_w = True
            self.time_w = True
        if tag == 'time' and self.time_w:
            print('time:%s' % attrs[0][1])
            self.time = str(attrs[0][1])
            self.time_w = False
        if tag == 'span' and len(attrs) and 'event-location' in attrs[0]:
            self.location_w = True

    def handle_data(self, data):
        # print("data:%s" % data)
        if self.title_w:
            print("title:%s" % data)
            self.title = data
            self.title_w = False
        if self.location_w:
            print("location:%s" % data)
            self.location = data
            meets.append(Meet(self.title, self.time, self.location))
            self.location_w = False

myparser = MyHtmlParser()
with request.urlopen('https://www.python.org/events/python-events/') as f:
    scont = f.read()
    print(scont)

myparser.feed(str(scont, encoding='utf-8'))
print(meets)

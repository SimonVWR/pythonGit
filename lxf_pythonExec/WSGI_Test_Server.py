from wsgiref.simple_server import make_server
def application(environ, start_reponse):
    start_reponse('200 OK', [('Context-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

## 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving on port 8000 ...')
httpd.serve_forever()


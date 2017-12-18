import socket
import threading

def tcpConn(sock, addr):
    print('Accept connnection from %s:%s'%addr)  #addr 为tuple
    sock.send(b'Welcome')       # utf-8 coding
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello, %s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connetion form %s:%s has closed'%addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9000))
s.listen(5)
print('Server listen on port 9000...')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcpConn, args=(sock, addr))
    t.start()








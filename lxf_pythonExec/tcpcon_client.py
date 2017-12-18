import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = ('127.0.0.1', 9000)
s.connect(dest)

print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()

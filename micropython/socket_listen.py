import socket
import sys

def recv(data):
    sys.stdout.write(data)

s = socket.socket()
#sock.connect(lambda s: s.onrecv(recv))
s.bind(('0.0.0.0', 2525))
s.listen(1)
while True:
    data = s.recv(100)
    if data:
        print(str(data, 'utf8'), end='')
    else:
        break

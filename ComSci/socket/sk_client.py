import socket

HOST = '172.20.10.5'
PORT = 8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'dry')
    data = s.recv(1024)
print('received', repr(data))
s.close()

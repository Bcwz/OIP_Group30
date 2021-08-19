import socket

#NEED CHANGE IP ADDRESS
HOST = '172.20.10.5'
PORT = 8080

def ping_rpi(text):
    command = '{0}'.format(text).encode()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(command)
        data = s.recv(1024)
    print('Sending command {0} to raspberry PI'.format(text))

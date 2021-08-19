import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn , addr = s.accept()
    with conn:
        print("Connect by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

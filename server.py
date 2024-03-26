import socket

#SOCK_STREAM = TCP
#SOCK_DGRAM = UDP
#AF_INET = IP E PORTA. MODELO INET

HOST = 'localhost'
PORT = 5007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('conectado a', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data) 
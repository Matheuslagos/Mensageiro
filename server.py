import socket
import threading

HOST = '26.197.241.123'
PORT = 5007

# Lista para armazenar todas as conexões ativas
connections = []

def handle_client(conn, addr):
    print('Conectado a', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Recebido de', addr, ':', data.decode())
        # Repassar a mensagem recebida para todos os clientes, exceto o remetente
        for connection in connections:
            if connection != conn:
                connection.sendall(data)
    conn.close()
    connections.remove(conn)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        # Adicionar nova conexão à lista de conexões ativas
        connections.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

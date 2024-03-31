import socket
import threading

HOST = '26.197.241.123'
PORT = 5007

def send_message(s):
    while True:
        mensagem = input('escreva sua mensagem: ')
        mensagem_em_byte = str.encode(mensagem)
        s.sendall(mensagem_em_byte)

def receive_messages(s):
    while True:
        data = s.recv(1024)
        print('Received', repr(data))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

send_thread = threading.Thread(target=send_message, args=(s,))
receive_thread = threading.Thread(target=receive_messages, args=(s,))

send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()

s.close()

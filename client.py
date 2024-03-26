import socket

#SOCK_STREAM = TCP
#SOCK_DGRAM = UDP
#AF_INET = IP E PORTA. MODELO INET

HOST = 'localhost'
PORT = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while(True):

    mensagem = input('escreva sua mensagem: ')
    mensagem_em_byte = str.encode(mensagem)
    s.sendall(mensagem_em_byte)
    
    data = s.recv(1024)
    print('Received', repr(data))

s.close()

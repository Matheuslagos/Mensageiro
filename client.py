import socket

#SOCK_STREAM = TCP
#SOCK_DGRAM = UDP
#AF_INET = IP E PORTA. MODELO INET

HOST = 'localhost'
PORT = 5007
mensagem = input('escreva sua mensagem: ')
mensagem_em_byte = str.encode(mensagem)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensagem_em_byte)
    data = s.recv(1024)
print('Received', repr(data))


#PRINTAR OS DADOS QUE FORAM RECEBIDOS DO CLIENTE
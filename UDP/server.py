import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5007

def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((SERVER_IP, SERVER_PORT))
        print('Aguardando arquivo...')
        with open('received_file.txt', 'wb') as file:
            while True:
                data, addr = s.recvfrom(1024)
                if data == b'END':
                    break
                file.write(data)
        print('Arquivo recebido com sucesso.')

def main():
    receive_file()

if __name__ == "__main__":
    main()

import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5007

def send_file(file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'START', (SERVER_IP, SERVER_PORT))
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                s.sendto(data, (SERVER_IP, SERVER_PORT))
        s.sendto(b'END', (SERVER_IP, SERVER_PORT))
        print('Arquivo enviado com sucesso.')

def main():
    file_path = input('Digite o caminho do arquivo a ser enviado: ')
    send_file(file_path)

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

HOST = '26.197.241.123'
PORT = 5007

def send_message():
    mensagem = input_field.get()
    input_field.delete(0, tk.END)  # Limpar o campo de entrada
    mensagem_em_byte = str.encode(mensagem)
    s.sendall(mensagem_em_byte)

def receive_messages():
    while True:
        data = s.recv(1024)
        if not data:
            break
        output_field.insert(tk.END, f'Received: {repr(data)}\n')
        output_field.see(tk.END)  # Role a caixa de texto automaticamente

# Configuração da janela
root = tk.Tk()
root.title("Chat Client")

# Campo de entrada
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)
input_field = tk.Entry(input_frame)
input_field.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
send_button = tk.Button(input_frame, text="Enviar", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Caixa de texto para exibir mensagens recebidas
output_field = scrolledtext.ScrolledText(root)
output_field.pack(fill=tk.BOTH, expand=True)

# Conexão com o servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Threads para enviar e receber mensagens
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()

root.mainloop()

# Aguardar que as threads terminem
send_thread.join()
receive_thread.join()

# Fechar a conexão
s.close()

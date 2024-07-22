import tkinter as tk
from tkinter import scrolledtext
import Pyro4
import threading

@Pyro4.expose
class ChatClient:
    def __init__(self, output_field):
        self.output_field = output_field

    def receive_message(self, message):
        self.output_field.insert(tk.END, message + '\n')
        self.output_field.see(tk.END)  # Role a caixa de texto automaticamente

# Função para iniciar o daemon Pyro4
def start_pyro_daemon():
    Pyro4.Daemon.serveSimple(
        {
            client: "example.chatclient" + str(client_id)
        },
        ns=True
    )

# Configuração da janela
root = tk.Tk()
root.title("Chat Client")

# Campo de entrada
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)
input_field = tk.Entry(input_frame)
input_field.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

def send_message():
    message = input_field.get()
    input_field.delete(0, tk.END)  # Limpar o campo de entrada
    chat_server.send_message(message, client_id)

send_button = tk.Button(input_frame, text="Enviar", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Caixa de texto para exibir mensagens recebidas
output_field = scrolledtext.ScrolledText(root)
output_field.pack(fill=tk.BOTH, expand=True)

# Conexão com o servidor
chat_server = Pyro4.Proxy("PYRONAME:example.chatserver")
client = ChatClient(output_field)
client_id = chat_server.connect()

# Iniciar o daemon Pyro4 em um thread separado
daemon_thread = threading.Thread(target=start_pyro_daemon)
daemon_thread.daemon = True
daemon_thread.start()

# Iniciar a interface gráfica
root.mainloop()

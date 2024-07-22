import Pyro4
import threading

@Pyro4.expose
class ChatServer:
    def __init__(self):
        self.connections = []

    def connect(self):
        client = Pyro4.current_context.client
        self.connections.append(client)
        print(f'Conectado a {client}')
        return len(self.connections) - 1

    def send_message(self, message, sender_id):
        sender = self.connections[sender_id]
        for i, connection in enumerate(self.connections):
            if connection != sender:
                try:
                    connection._pyroClaimOwnership()  # Necessário para evitar problemas de threading
                    connection.receive_message(message)
                except Exception as e:
                    print(f'Erro ao enviar mensagem para o cliente {i}: {e}')

# Iniciando o servidor Pyro4
juj= "ip"
daemon = Pyro4.Daemon(host=juj)
uri =daemon.register(ChatServer)
print(uri)

print("Servidor pronto.")
daemon.requestLoop()

import socket

# Cria o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect(("localhost", 5000))

# Envia uma mensagem
cliente.send("Olá servidor! Sou o cliente.".encode())

# Recebe a resposta
resposta = cliente.recv(1024).decode()
print("Resposta do servidor:", resposta)

# Fecha a conexão
cliente.close()

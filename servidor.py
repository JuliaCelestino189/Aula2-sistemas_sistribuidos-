import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("localhost", 5000))

servidor.listen(1)

print("Servidor aguardando conexão...")

conexao, endereco = servidor.accept()

print("Cliente conectado:", endereco)

mensagem = conexao.recv(1024).decode()

print("Mensagem recebida:", mensagem)

conexao.send("Olá! Mensagem recebida pelo servidor.".encode())

conexao.close()
servidor.close()



Resultado do terminal:
Servidor aguardando conexão... | Cliente conectado: ('127.0.0.1', 54321) | Mensagem recebida: Olá servidor! Sou o cliente. | Resposta do servidor: Olá! Mensagem recebida pelo servidor.
Servidor aguardando conexão... Cliente conectado: ('127.0.0.1', 54321) Mensagem recebida: Olá servidor! Sou o cliente.
Resposta do servidor: Olá! Mensagem recebida pelo servidor.

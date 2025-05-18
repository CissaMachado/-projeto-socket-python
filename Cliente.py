import socket

# Configuração do cliente
HOST = '127.0.0.1'  # IP do servidor (localhost)
PORT = 5000         # Porta usada no servidor

# Criar o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor
cliente.connect((HOST, PORT))

# Enviar e receber dados
while True:
    mensagem = input("Cliente: ")
    cliente.send(mensagem.encode())
    resposta = cliente.recv(1024)
    print("Servidor:", resposta.decode())

# Fechar conexão
cliente.close()

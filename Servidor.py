import socket

# Configuração do servidor
HOST = '127.0.0.1'  # IP local
PORT = 5000         # Porta que será usada

# Criar o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associar o socket ao endereço e porta
servidor.bind((HOST, PORT))

# Escutar conexões
servidor.listen()

print(f"Servidor ouvindo em {HOST}:{PORT}...")

# Aceitar conexão de cliente
conexao, endereco = servidor.accept()
print(f"Conectado por {endereco}")

# Receber dados do cliente
while True:
    dados = conexao.recv(1024)
    if not dados:
        break
    print("Cliente:", dados.decode())
    resposta = input("Servidor: ")
    conexao.send(resposta.encode())

# Fechar conexão
conexao.close()
servidor.close()

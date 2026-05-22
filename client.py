import socket

SERVER = "192.168.0.212"
PORT = 5050
FORMAT = "utf-8"

#defini que vai ser ipv4 e tcp
client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#iniciei a conexão com handshake
client.connect((SERVER, PORT))

#enviando mensagem
mensagem = "ney na copa fds"
client.send(mensagem.encode(FORMAT))
#recebendo
resposta = client.recv(1024).decode(FORMAT)
print(resposta)

client.close()

import socket
#defini que vai ser ipv4 e tcp
client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#iniciei a conexão com handshake
client.connect("ip do melo", "mesma porta q ele ta usando")

#enviando mensagem
client.send("ney na copa fds". encode())
#recebendo
resposta = client.recv(1024).decode()
print(resposta)

client.close()


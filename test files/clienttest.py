import socket

SERVER = "192.168.0.212"
PORT = 5050
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    msg = input("Digite uma mensagem: ")

    client.send(msg.encode(FORMAT))

    if msg == "!DISCONNECT!":
        break

    resposta = client.recv(1024).decode(FORMAT)
    print("Servidor:", resposta)

client.close()
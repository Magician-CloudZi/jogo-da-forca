import socket
import os

SERVER = "192.168.0.212"
PORT = 6969
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("hangman game is starting!")

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    server_msg_1 = client.recv(1024).decode(FORMAT)
    letter = input(f"{server_msg_1}")

    if letter == DISCONNECT_MESSAGE:
        break

    client.send(letter.encode(FORMAT))
    clean_screen()

client.close()
#client file
import socket
import os
from time import sleep

SERVER = "192.168.0.212"
PORT = 6969
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!D!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("hangman game is starting!")

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    server_msg_1 = client.recv(1024).decode(FORMAT)
    letter = input(f"{server_msg_1}")

    if letter == DISCONNECT_MESSAGE:
        print("[disconnecting...]")
        sleep(2)
        break

    client.send(letter.encode(FORMAT))
    clean_screen()
    print("\n\n [processing...]")
    sleep(2)
    clean_screen()

client.close()
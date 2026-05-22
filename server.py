import socket
import threading
import time
import os

#---------------------------Conection Logic---------------------------------------

PORT = 6969 #use high port numbers to avoid conflicts with well-known ports
HOST = socket.gethostbyname(socket.gethostname()) #ip address of the server. (My address in this case) #im using 0.0.0.0 to listen all networks interfaces that i have
ADDR = (HOST, PORT) #create the pair that represent socket address on local network
FORMAT = "utf-8" #std format that we gonna use to translate encode messages
DISCONNECT_MESSAGE = "!DISCONNECT!" #default message to end connection


#here we finally create the socket that is gonna handle the server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicates ipv4 and SOCK_STREAM indicates TCP
server.bind(ADDR) #we define the address of the server socket


def handle_client(conn, addr): #conn -> connection and addr -> address. // handle individual connections
    print(f'[NEW CONNECTION || ] {addr}')

    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT) #storage the package sent by client on "msg". This is a blocking line (program will sleep untill recieve it all)
        if not msg or msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] sent -> [{msg}]")
        conn.send("[Server recivied the message]".encode(FORMAT))

    conn.close()
    print(f"[Disconnected] {addr}")


def start(): #handle new connections
    server.listen() #server is now open to new connections
    print(f"Server running on: {HOST}:{PORT}")

    while True:
        conn, addr = server.accept() #when a new connection occur, it will store the address and object(socket) that we can use to send files
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


#------------------------------------Game Logic----------------------------------------

"""def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_painel(conn, hidden_word, attempts):
    clean_screen()
    
    conn.send(f'{attempts} remaining attempts'.encode(FORMAT))

def choose_word(brute_word): #convert the chosen word in traces
    hidden_word = []
    brute_word = brute_word.lower()
    
    for char in brute_word:
        if char == " ":
            hidden_word.append("-")
        else:
            hidden_word.append("_")

    return " ".join(hidden_word)

def ask_letter(conn, ):
    chosen_letter = conn.send("Choose a letter: ".encode(FORMAT))

#main loop
while True:
    brute_word = input("Qual será a palavra a ser adivinhada?: ")
    attempts = 6
    right_letters = []
    wrong_letters = []

    hidden_word = choose_word(brute_word) #here we have the word in the stripes format

    while attempts >= 0 and hidden_word != list(brute_word):
        while True:
            chosen_letter = conn.send("Choose a letter: ".encode(FORMAT))
            if len(chosen_letter) == 1:
                break
            else:"""


start()
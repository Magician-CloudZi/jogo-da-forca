import socket
import threading
from time import sleep
import os

#---------------------------Conection Logic---------------------------------------

PORT = 6969 #use high port numbers to avoid conflicts with well-known ports
HOST = socket.gethostbyname(socket.gethostname()) #ip address of the server. (My address in this case)
ADDR = (HOST, PORT) #create the pair that represent socket address on local network
FORMAT = "utf-8" #std format that we gonna use to translate encode messages
DISCONNECT_MESSAGE = "!DISCONNECT!" #default message to end connection


#here we finally create the socket that is gonna handle the server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicates ipv4 and SOCK_STREAM indicates TCP
server.bind(ADDR) #we define the address of the server socket


def handle_client(conn, addr): #conn -> connection and addr -> address. // handle individual connections
    print(f'[NEW CONNECTION || ] {addr}')

    game_loop(conn) #start the game with this client

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

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_panel(conn, hidden_word, lives):
    conn.send(f'\n {lives} remaining lives \n {hidden_word} \n'.encode(FORMAT))
    #clean_screen()

def encrypt_word(chosen_word): #convert the chosen word in traces
    hidden_word = []
    chosen_word = chosen_word.lower()
    
    for char in chosen_word:
        if char == " ":
            hidden_word.append("-")
        else:
            hidden_word.append("_")

    return hidden_word #return as list so we can update it later

def ask_letter(conn):
    conn.send("\n Choose a letter: ".encode(FORMAT))
    #clean_screen()
    chosen_letter = conn.recv(1024).decode(FORMAT) #wait for client response
    return chosen_letter

def game_loop(conn): #receives conn from handle_client
    #game loop
    while True:
        chosen_word = input("\n What will be the word to guess?: ") #server host types the word
        lives = 6
        right_letters = []
        wrong_letters = []

        hidden_word = encrypt_word(chosen_word) #here we have the word in the list format with underscores

        #main logic loop
        while lives > 0 and hidden_word != list(chosen_word.lower()):

            #make sure that only one letter is chosen on each round
            while True:
                chosen_letter = ask_letter(conn) #send question and receive letter from client
                if len(chosen_letter) == 1:
                    break
                else:
                    conn.send("\n Only one letter at a time!!".encode(FORMAT))
                    #clean_screen()

            #2nd letter try
            if chosen_letter in right_letters or chosen_letter in wrong_letters:
                conn.send("\n You already tried this letter".encode(FORMAT))

            #match cases for the chosen letter
            elif chosen_letter in chosen_word.lower():
                right_letters.append(chosen_letter) #fixed: was appending chosen_word instead of chosen_letter
                #for each position where this chosen letter appears in the chosen word, update hidden_word
                spots = [pos for pos, letter in enumerate(chosen_word.lower()) if letter == chosen_letter]
                for pos in spots:
                    hidden_word[pos] = chosen_letter #reveal the letter in its correct positions
                conn.send("\n Nice try, this letter appears in this word".encode(FORMAT))
            
            #letter 1st try and doesnt belong to chosen_word
            else:
                conn.send("\n This letter doesn't appear in the chosen word".encode(FORMAT))
                lives -= 1
                wrong_letters.append(chosen_letter)

        show_panel()

        if lives == 0:
            conn.send(f"\n You lose. The right word is {chosen_word}".encode(FORMAT)) #fixed: added .encode()
            #clean_screen()
        else:
            conn.send("\n Congrats, you guessed the word!".encode(FORMAT)) #fixed: added .encode()
            #clean_screen()

        conn.send("\n Wanna play again? [yes/no]".encode(FORMAT))
        #clean_screen()
        play_again = conn.recv(1024).decode(FORMAT)

        if play_again == "no":
            conn.send("\n thanks for playing!".encode(FORMAT))
            #clean_screen()
            break

start()
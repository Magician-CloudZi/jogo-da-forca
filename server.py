import socket
import threading
import time

HEADER = 128 #how many bytes are gonna come
PORT = 5050 #use high port numbers to avoid conflicts with well-known ports
SERVER = "::" #socket.gethostbyname(socket.gethostname()) #ip address of the server. (My address in this case) #im using 0.0.0.0 to listen all networks interfaces that i have
ADDR = (SERVER, PORT) #create the pair that represent socket address on local network
FORMAT = "utf-8" #std format that we gonna use to translate encode messages
DISCONNECT_MESSAGE = "!DISCONNECT!" #default message to end connection

#here we finally create the socket that is gonna handle the server connection
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #AF_INET indicates ipv4 and SOCK_STREAM indicates TCP
server.bind(ADDR) #we define the address of the server socket

def handle_client(conn, addr): #conn -> connection and addr -> address. // handle individual connections
    print(f'[NEW CONNECTION || ] {addr} connected')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #find out which is the size on incoming message
        msg_length = int(msg_length) #turns it into a integer, so we can use it
        msg = conn.recv(msg_length).decode(FORMAT) #storage the package sent by client on "msg". This is a blocking line (program will sleep untill recieve it all)
        if msg == DISCONNECT_MESSAGE:
            connected = False
    
        print(f"[{addr}] sent -> {msg}")

    conn.close()    


def start(): #handle new connections
    server.listen() #server is now open to new connections
    print(f"Server address: {SERVER}")
    while True:
        conn, addr = server.accept() #when a new connection occur, it will store the address and object(socket) that we can use to send files
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
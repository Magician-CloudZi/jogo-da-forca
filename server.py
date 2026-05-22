import socket
import threading
import time

PORT = 5050 #use high port numbers to avoid conflicts with well-known ports
HOST = "192.168.0.212" #socket.gethostbyname(socket.gethostname()) #ip address of the server. (My address in this case) #im using 0.0.0.0 to listen all networks interfaces that i have
ADDR = (HOST, PORT) #create the pair that represent socket address on local network
FORMAT = "utf-8" #std format that we gonna use to translate encode messages
DISCONNECT_MESSAGE = "!DISCONNECT!" #default message to end connection

#here we finally create the socket that is gonna handle the server connection
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #AF_INET indicates ipv4 and SOCK_STREAM indicates TCP
server.bind(ADDR) #we define the address of the server socket

def handle_client(conn, addr): #conn -> connection and addr -> address. // handle individual connections
    print(f'[NEW CONNECTION || ] {addr}')

    connected = True
    while connected:
        data = conn.recv(1024).decode(FORMAT) #storage the package sent by client on "msg". This is a blocking line (program will sleep untill recieve it all)
        msg = data.decode(FORMAT)
        if not data or data == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] sent -> {msg}")
        conn.send("[Message recivied]".encode(FORMAT))

    conn.close()
    print(f"[Disconnected] {addr}")


def start(): #handle new connections
    server.listen() #server is now open to new connections
    print(f"Server address: {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept() #when a new connection occur, it will store the address and object(socket) that we can use to send files
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
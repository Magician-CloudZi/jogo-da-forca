import socket

SERVER = "192.168.0.212" #input("[Server IP?:]")
PORT = 6969
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!" #default message to end connection

#define that its gonna be ipv4 and tcp
client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#start the connections
client.connect((SERVER, PORT))
print(f"Client connected to: {SERVER}:{PORT}")

while True:
    message = input("[Write a message:]")
    client.send(message.encode(FORMAT))
    
    if message == DISCONNECT_MESSAGE:
            print(f"[Disconnected]")
            break
    
    awser = client.recv(1024).decode(FORMAT)
    print(awser)

client.close()
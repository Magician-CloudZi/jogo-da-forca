import socket
import threading
import time

PORT = 5050 #use high port numbers to avoid conflicts with well-known ports
SERVER = #ip address of the server
ADDR = (SEREVER, PORT) #create the pair that represent socket address on local network

#here we finally create the socket that is gonna handle the server connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicates ipv4 and SOCK_STREAM indicates TCP
server.bind(ADDR) #we define the address of the server socket

def handle_client(conn, addr): #conn -> connection and addr -> address.
    pass

def start():
    pass

'''
hostname = socket.gethostname() -> ask OS the name of current device
ip = socket.gethostbyname(hostname) -> ask OS which is the ip addres of "hostname" device
'''
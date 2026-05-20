import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"ip: {ip}")
print(f"hostname: {hostname}")
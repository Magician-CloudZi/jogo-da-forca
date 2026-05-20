import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"ip: {ip}")
print(f"hostname: {hostname}")
print("testada pesada")
soma = 10
soma += 5
print(f"soma: {soma}")
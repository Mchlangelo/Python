import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Nome da computadora: " + hostname)
print("Endereço IP: " + ip)


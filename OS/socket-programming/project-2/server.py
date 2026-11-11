import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind(("127.0.0.1", 5000))

message, addr = socket_server.recvfrom(1024)

print(f"{message} recieved from {addr}")

socket_server.sendto(b"Recieved", addr)

socket_server.close()
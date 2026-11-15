import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 5000))

while True:
    username  = input("Enter your username: ")
    client_socket.send(message.encode("utf-8"))
    print(client_socket.recv(1024).decode("utf-8"))
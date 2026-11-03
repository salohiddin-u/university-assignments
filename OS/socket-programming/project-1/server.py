import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 8080))

socket.listen(5)
print("Server is listening on port 8080...")

while True:
    client_socket, address = socket.accept()
    print(f"Connection from {address} has been established.")
    client_socket.close()


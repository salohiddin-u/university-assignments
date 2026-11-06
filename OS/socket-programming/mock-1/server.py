import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 12349))

server_socket.listen(5)
print("Server is listening on port 12349...")

connection, address = server_socket.accept()
print(f"Connection from {address} has been established.")

while True:
    message = connection.recv(9000).decode()

    print(f"Received message: {message}")
    a = input("Enter your message: ")
    connection.send(f"{a}".encode())
    if message == "bye":
        break

connection.close()
server_socket.close()
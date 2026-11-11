import socket

# Correct UDP Client pattern
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)
message = "Hello from client!"

# DO NOT call client_socket.bind(...) here
client_socket.sendto(message.encode("utf-8"), server_address)

data, _ = client_socket.recvfrom(1024)
print(f"Server response: {data.decode('utf-8')}")

client_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("localhost", 7070)

while True:
    message = input("Enter temperature (or '/exit' to quit): ")
    client_socket.sendto(message.encode("utf-8"), server_addr)
    if message == "/exit":
        print("Exiting client")
        break
    data, server_addr = client_socket.recvfrom(1024)

    print(data.decode("utf-8"))

    

client_socket.close()
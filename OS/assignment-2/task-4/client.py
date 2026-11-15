import socket
import threading

def recieve_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            print(data)
            
        except:
            print("Connnection failed")
            break


username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
client_socket.sendall(username.encode("utf-8"))

thread = threading.Thread(target=recieve_message, args=(client_socket,))
thread.start()

while True:
    message = input("")
    if message == "/exit":
        client_socket.sendall(message.encode("utf-8"))
        break
    client_socket.sendall(message.encode("utf-8"))
thread.join()
client_socket.close()
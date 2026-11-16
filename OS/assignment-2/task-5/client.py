import socket
import threading


def receive(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
        except:
            print("Connection lost")
            break


name = input("Username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
client.sendall(name.encode('utf-8'))

thread = threading.Thread(target=receive, args=(client,))
thread.start()

while True:
    msg = input("Choose rock, paper, scissors or /exit: ")
    client.sendall(msg.encode('utf-8'))
    if msg == "/exit":
        break

thread.join()
client.close()
print("bye")
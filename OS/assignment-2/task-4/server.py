import socket
import threading


users = {}

def handle_users(socket_conn, addr):
    username = socket_conn.recv(1024).decode('utf-8')
    users[username] = (socket_conn, addr)

    for username_, (client_socket, address) in users.items():
        client_socket.send(f"{username} joined to the group".encode('utf-8'))

    try:
        while True:
            message = socket_conn.recv(1024).decode('utf-8')
            if not message or message == "/exit":
                for username_, (client_socket, address) in users.items():
                    if username_ != username:
                        client_socket.send(f"[Server] {username} left the group".encode('utf-8'))
                break

            for username_, (client_socket, address) in users.items():
                if username_ != username:
                    client_socket.send(f"[{username}]: {message}".encode('utf-8'))
    finally:
        users.pop(username, None)
        socket_conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))

server_socket.listen()
while True:
    socket_conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_users, args=(socket_conn, addr))
    thread.start()
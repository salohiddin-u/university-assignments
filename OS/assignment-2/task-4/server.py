import socket
import threading


users = {}

def handle_users(socket_conn, addr):
    socket_conn.send("Enter your username: ".encode('utf-8'))
    username = socket_conn.recv(1024).decode('utf-8')
    users[username] = [socket_conn, addr]

    while True:
        try:
            message = socket_conn.recv(1024).decode('utf-8')
            if message:
                for user, (conn, addr) in users.items():
                    if user != username:
                        conn.send(f"{username}: {message}".encode('utf-8'))
                    else:
                        conn.send(f"You: {message}".encode("utf-8"))
        except:
            print("error")
            break


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))

    server_socket.listen(5)
    while True:
        socket_conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_users, args=(socket_conn, addr))
        thread.start()

        
main()
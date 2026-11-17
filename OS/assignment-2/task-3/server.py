import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("localhost", 7070)

print("Server listening")
server_socket.bind(server_addr)

def classification(temp):
    temp = float(temp)
    if temp < 10:
        return "Very Cold"
    elif temp < 25:
        return "Normal"
    elif temp < 35:
        return "Warm"
    elif temp < 45:
        return "High Temperature"
    else:
        return "Critical"

while True:
    data, client_addr = server_socket.recvfrom(1024)
    
    try:
        message = data.decode("utf-8")
        message = float(message)
        answer = classification(message)
    except:
        answer = "Error: message is not valid"
    if message == "/exit":
        print("Exiting server")
        break
    server_socket.sendto(answer.encode("utf-8"), client_addr)

    

server_socket.close()
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(5)

users = {}
choices = {}
scores = {}


def send_all(msg):
    for name in users:
        users[name][0].send(msg.encode('utf-8'))


def check_round():
    if len(users) < 2:
        return

    if len(choices) < len(users):
        return

    picked = set(choices.values())

    if len(picked) != 2:
        send_all("Round result: Draw")
    else:
        if "rock" in picked and "scissors" in picked:
            winner = "rock"
        elif "scissors" in picked and "paper" in picked:
            winner = "scissors"
        else:
            winner = "paper"

        winners = []
        for name in choices:
            if choices[name] == winner:
                winners.append(name)
                scores[name] = scores[name] + 1

        send_all("Round result: " + winner + " wins. Winners: " + ", ".join(winners))

    send_all("Scores: " + str(scores))
    choices.clear()


def handle_client(client, addr):
    name = client.recv(1024).decode('utf-8').strip()
    users[name] = (client, addr)
    scores[name] = 0
    send_all(name + " joined the game")

    while True:
        msg = client.recv(1024).decode('utf-8').strip().lower()

        if not msg or msg == "/exit":
            break

        if msg in ["rock", "paper", "scissors"]:
            choices[name] = msg
            client.send("Choice received. Waiting for others...".encode('utf-8'))
            check_round()
        else:
            client.send("Invalid choice. Enter rock, paper, scissors or /exit".encode('utf-8'))

    del users[name]
    del scores[name]
    choices.pop(name, None)
    send_all(name + " left the game")
    check_round()
    client.close()


while True:
    client, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()
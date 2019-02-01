
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(f"received: {msg}")
            if  msg == "{quit}":
                break
            if  msg == "":
                break
        except:
            break

def send(msg):
    """Handles sending of messages."""
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


HOST = "127.0.0.1"
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

game_id = "coffee"
send(game_id)
while True:
    msg = input()
    send(msg)


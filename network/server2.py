from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import uuid

opponents = {}
clients = {} 

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the network", "utf8"))
        client_id = str(uuid.uuid4())
        clients[client_id] = client
        addresses[client_id] = client_address

        # start a new listener handler in a separate thread
        Thread(target=handle_client, args=(client, client_id,)).start()


def handle_client(client, client_id):
    """thread - handles a single client connection."""

    # client sends game_id to be matched with opponent with the same game_id
    game_id = client.recv(BUFSIZ).decode("utf8")
    #client.send(bytes("", "utf8"))

    opponent = None

    player_id = register_handle(game_id, client_id)
    client.send(bytes(f"Welcome, player {player_id} : {client_id}", "utf8"))

    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf-8")
            if  msg == "{quit}":
                break
            # pass on the message to the opponent
            opponent = get_opponent_handle(game_id, player_id)
            if opponent:
                opponent.send(bytes(msg, "utf8"))
            else:
                client.send(bytes(f"no opponenet yet", "utf8"))
        except:
            # just bail for now
            opponent = get_opponent_handle(game_id, player_id)
            if opponent:
                opponent.send(bytes("{quit}", "utf8"))
            break

        # else:
        #     client.send(bytes("{quit}", "utf8"))
        #     client.close()
        #     #del clients[client]
        #     break

def register_handle(game_id, client_id):
    # TBD - will need to handle when 3rd person joins
    if opponents.get(game_id, None):
        # player 2
        opponents[game_id].append(client_id)
        return 2
    else:
        # player 1
        opponents[game_id] = [client_id]
        return 1


def get_opponent_handle(game_id, player_id):
    if len(opponents[game_id]) > 1:
        if player_id == 1:
            return clients[opponents[game_id][1]]
        else:
            return clients[opponents[game_id][0]]
    return None


def send(client_id, msg):
    """Broadcasts a message to all the clients."""
    clients[client_id].send(bytes(msg, "utf8"))


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

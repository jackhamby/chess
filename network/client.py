from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


ADDR = "127.0.0.1"
PORT = 8001

class Client():

    def __init__(self, server_addr=ADDR, server_port=PORT):
        self.server_addr = server_addr
        self.server_port = server_port
        self.connection = socket(AF_INET, SOCK_STREAM)
        self.connection.connect((self.server_addr, self.server_port))
        self.last_message = None

    def start(self):  
        """ start thread to recieve msgs from server """
        recieving_thread = Thread(target=self.recieve)
        recieving_thread.start()
        recieving_thread.join() # Wait for thread to exit
        self.stop()

    def stop(self):
        """ stop client, close socket """
        self.connection.close()

    def recieve(self):
        """ recieve messages from server """
        while (True):
            try:
                msg = self.connection.recv(32)
                self.last_message = msg.decode("utf-8")
                print(msg)
            except:
                print('connection broken')
                break

    def send(self, msg):
        """ send msg to the server """ 
        try:
            self.connection.send(bytes(msg, "utf-8"))
        except:
            print('connection broken')














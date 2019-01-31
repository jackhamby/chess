import socket

class Client():

    def __init__(self, addr="127.0.0.1", server_port=9009):
        self.port = 8001
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conn.bind(("127.0.0.1", self.port))
        self.addr = addr
        self.server_port = server_port

    def run(self):
        try:
            print(f'sending connect to player1 at {self.addr}:{self.server_port} ' )
            self.conn.sendto(b'c', (self.addr, self.server_port))
            # while (True):
            #     pass
                

        except Exception as e: 
            print(e)
            print('failed to connect')
        # while(True):

                



if __name__ == "__main__":
    client = Client()
    client.run()
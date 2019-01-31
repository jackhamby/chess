import sys, socket, select

class Server():


    def __init__(self, port=9009):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host_ip = "127.0.0.1"
        self.port = port
        self.listener.bind((self.host_ip, self.port))
        print(f'waiting for player2 at {self.host_ip}:{self.port}' )


        
    def run(self):
        
        while(True):
            data = self.listener.recvfrom(32)
            print(data)




if __name__ == "__main__":
    server = Server()
    server.run()

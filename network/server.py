from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import queue

ADDR = "127.0.0.1"
PORT = 8001


class Server():
	def __init__(self, addr=ADDR, port=PORT):
		self.addr = addr
		self.port = port
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((self.addr, self.port))

		self.waiting_client_queue = queue.Queue()
		self.clients = []
		self.sessions = []

	def start(self):
		self.sock.listen(5)
		print('Waiting for players...')
		server = Thread(target=self.handle_incoming_connections)
		server.start()
		server.join() # Wait until thread terminates
		self.stop()

	def stop(self):
		self.sock.close()

	def broadcast(self, msg):
		for client in self.clients:
			client.send(bytes(msg, 'utf-8'))

	def create_client(self, client):
		self.clients.append(client)
		self.waiting_client_queue.put(client)
		if (self.waiting_client_queue.qsize() >= 2):
			client_1 = self.waiting_client_queue.get()
			client_2 = self.waiting_client_queue.get()
			session = Session(self, client_1, client_2)
			session.start()
			self.sessions.append(session)

	def handle_incoming_connections(self):
		while (True):
			client, client_ip = self.sock.accept()
			self.create_client(client)
			
	def handle_client(self, client):
		while(True):
			try:
				msg = client.recv(32)
				print(msg)
			except:
				print('connection broken')
				break

	

class Session():

	def __init__(self, server, client_1, client_2):
		self.server = server
		self.client_1 = client_1
		self.client_2 = client_2


	def start(self):
		
		self.client_1.send(bytes(f's|{1}', 'utf-8'))
		self.client_2.send(bytes(f's|{2}', 'utf-8'))
	
		Thread(target=self.handle_client_1, args=(self.client_1,)).start()
		Thread(target=self.handle_client_2, args=(self.client_2,)).start()

	def handle_client_1(self, client_1):
		while(True):
			try:
				msg = client_1.recv(32)
				print(msg)
				self.client_2.send(msg)
			except:
				print('connection broken')
				break

	def handle_client_2(self, client_2):
		while(True):
			try:
				msg = client_2.recv(32)
				print(msg)
				self.client_1.send(msg)
			except:
				print('connection broken')
				break



if __name__ == "__main__":
	server = Server()
	server.start()











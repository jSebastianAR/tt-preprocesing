import socket
import time

HEADERSIZE = 10

class Servidor():

	def __init__(self):
		self.HOST = ''
		self.PORT = 50000		
		self.sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Creates the tcp socket
			


	def listen(self):

		
		self.sckt.bind((self.HOST,self.PORT)) #makes the link of the socket with the ip address and the port
		self.sckt.listen(5)	#Specifies the number of clients which can listen at the same times
		print('Listen in: {}'.format(socket.gethostbyname(socket.gethostname())))
				

		while True:
			
			print('Waiting for conection')
			conn, addr = self.sckt.accept()
			print('Connected by {}'.format(str(addr)))
			data = conn.recv(1024) #gets the data from the client
			print('Message from client: {}'.format(data))
			
			#full_data = f'The time is: {time.time()}'
			#full_data = f"{len(full_data):<10}"+full_data #adding the header to specify the size of the message
			
			#conn.sendall(bytes(full_data,'utf-8'))
			conn.close()



server = Servidor()
server.listen()



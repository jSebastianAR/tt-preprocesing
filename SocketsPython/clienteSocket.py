import socket 
import sys
import time

HEADERSIZE = 10

class Cliente():

	def __init__(self):

		self.HOST = '127.0.0.1'
		self.PORT = 50000
		self.sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def do_connection(self):
		self.sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sckt.connect((self.HOST,self.PORT))	

	@staticmethod	
	def readHeader(msg):

		tam = ''
		for letter in msg.decode():
			if not letter==' ':
				tam	+= letter	
		
		#print(f"tipo:{type(tam)} valor: {tam} len: {len(tam)}")
		msglen = int(tam) #gets the header from the message
		return msglen


	def sendMessage(self):

		
		#self.sckt.sendall(b'Give me the data')
		done = False

		while True:
			print('Conecting to server')
			self.do_connection()
			full_data = ''
			while True:	

				data = self.sckt.recv(10)

				if len(full_data)==0:
					msglen = self.readHeader(data)


				if len(full_data)-HEADERSIZE==msglen: #if all the message was already sended
					print(f'All the message was received: {full_data[HEADERSIZE:]} with lenght: {msglen}')
					self.sckt.close()
					#done = True
					break
				else:
					full_data += data.decode() 

			time.sleep(1.5)		
		


client = Cliente()
client.sendMessage()
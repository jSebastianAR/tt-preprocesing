from threading import Thread
import socket
import time
#from clienteSocket import GLOBAL_DATA
from cliente_socket import GLOBAL_DATA

class listener_thread(Thread):
	#docstring for listener_thread
	def run(self):
		print(f"Server socket escuchando a GLTerminal")
		self.listen()
		
	def listen(self):

		# socket de flujo
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Se establece la configuración donde estará escuchando el socket
		serversocket.bind((socket.gethostbyname(socket.gethostname()), 5021))
		# el server escucha y se establece como máximo dos request
		serversocket.listen(2)

		while True:

			print(f"Esperando conexion, escuchando en {socket.gethostbyname(socket.gethostname())}:{5021}")
			clientsocket, addr = serversocket.accept()
			print(f"Conexión recibida")
			while True:

				try:
					msg = clientsocket.recv(4096)
					#logger.info('LOG_ID'+ str(currentTransaction)+ ' TRAMA RECIBIDA DE PARTE DE GLTERMINAL: '+str(msg))
					print(' TRAMA RECIBIDA DE PARTE DE GLTERMINAL: '+str(msg))
					GLOBAL_DATA = "HELLO WORLD"
					clientsocket.close()
				except socket.error as e:
					err = e.args[0]
					if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
					    sleep(1)
					    continue
					else:
					    msg=err
					    break
				else:
					break

			clientsocket.close()
			self.send_data(msg)

	def send_data(self,data):

		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

		clientsocket.connect((socket.gethostbyname(socket.gethostname()),50000))

		try:
			clientsocket.send(data)	
		except Exception as e:
			print(f'Exception {e}')
		finally:
			clientsocket.close()
			time.sleep(.5)



def outThread():
	i = 0
	while True:
		i += 1
		print(f'Proceso externo a hilo ejecutandose por vez número {i}')
		time.sleep(2)

def main():
	listener = listener_thread()
	listener.start()
	
			
		

main()

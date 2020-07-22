#Script for test the casting from string to hex#

str_request = "01321-723-681                                 4.0.1                 01              101"
data = str_request #str_request.split("")[1].split("")[0]

import binascii

#Funcion para CRC
def xor_strings(data):
	results_list = []
	print(f"Data: {data}\n\n\n")
	
	for i in range(0,len(data)):

		if i==0:
			result = chr(ord(data[i]) ^ ord(data[i+1]))
			#print(f"{data[i]} xor {data[i+1]}={result}")
			results_list.append(result)
			#print(result)
		elif i>0 and i+1<len(data): 
			aux = result
			result = chr(ord(result) ^ ord(data[i+1]))
			#print(f"{aux} xor {data[i+1]}={result}")

	
	print(f"Resultado CRC: {result}")		
	return result		

#Convierte la info en hexadecimal
def string2hex(string_sentence):

	hex_string 	= binascii.hexlify(string_sentence.encode())

	print(f"El resultado hexadecimal es: {hex_string.decode()}")
	#print(data)

def main():

	while True:
		string_sentence = input("ingresa la trama a transformar: ")
		string2hex(str_request)

xor_strings(data)
#string2hex(str_request)


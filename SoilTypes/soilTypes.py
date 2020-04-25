import subprocess

def read_files():
	final_soil_types = []
	txt_list = get_txt()
	for txt in txt_list:
		print(f"Reading {txt}")
		with open(txt,'r') as soil_types_file:
			
			for line in soil_types_file:
				
				data = line.rstrip('\n')
				data = data.rstrip('\t')
				soil = data.split(' ')[0]

				#si no esta
				if not(soil in final_soil_types) and len(soil)>0:
					print(f"Agregando el tipo de suelo {soil}")
					final_soil_types.append(soil)
					write_file(soil)
				#si esta
				else:
					print(f"El tipo de suelo {soil} ya existe")
	
	return final_soil_types

def get_txt():
	result = subprocess.check_output('ls SoilTypes/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"TXT: \n{txt_list}")
	return txt_list

def write_file(line):
	with open('TiposDeSueloJalisco.txt','a+') as soil_final_types:
		soil_final_types.write(line+'\n')




result = read_files()

print(result)
import unidecode
import subprocess

def get_all_towns():
	l = []
	with open('ListaMunicipiosJalisco.txt','r') as file:
		for town in file:
			l.append(remove_accents(town.rstrip('\n')))
	return l

def remove_accents(name):
	return unidecode.unidecode(name)

def get_name_towns(txt_list):
	l = []
	for txt in txt_list:
		print(txt)
		name = txt.split('.txt')[0].split('-')[1]
		if not(name in l):
			l.append(name)
	return l	

def get_txt_list():
	txt_list = subprocess.check_output('ls Dataset\ Clima\ Diario/*.txt',shell=True).decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(txt_list)
	names_txt_list = get_name_towns(txt_list)
	return names_txt_list

def write_file(line):
	with open('MissingTowns.txt','a') as file:
		file.write(line+'\n')

def get_missing_towns():
	current_towns = get_txt_list()
	all_towns = get_all_towns()
	print(f"Current Towns {current_towns} \n\nAll Towns {all_towns}")

	#POR CADA MUNICIPIO DE JALISCO
	for town in all_towns:
		#SI ESTÁ EN LA LISTA QUE DESCARGAMOS
		if town in current_towns:
			print(f"{town} se encuentra en current_towns")
		else:
			write_file(town)


get_missing_towns()
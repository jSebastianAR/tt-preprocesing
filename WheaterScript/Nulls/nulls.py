import subprocess
from dates import generate_date_list
import re

REGEX_BLANK_SPACES = r'[ ]+'
REGEX_DATES = r'[\d]{2}\/[\d]{2}\/[\d]{4}'
LIST_DAYS = generate_date_list('01/01/2008','31/12/2018')
	
def Evaluate_Towns():
	txt_files = get_txt()
	#Por cada archivo
	for txt in txt_files:
		txt_dict = {}
		txt_dict['Name'] = txt
		print(f"File to read: {txt} \n")
		with open(txt,'r',encoding = "ISO-8859-1") as file:

			conteo = find_nulls(file,txt)
			write_file(info_to_write(txt,conteo))

#Obtendrá cada uno de los datos del archivo de cada town
def find_nulls(text,txt):

	#Obtiene todas las fechas con datos del archivo
	dates_list_file = get_dates_file_list(txt)
	#Contador de nulos para cada variable, inicia en cero todo
	counterList = [0,0,0,0] #[PRECIP,EVAP,TMAX,TMIN]
	
	for day in LIST_DAYS:
		
		if day in dates_list_file:
			#Busca la linea de datos de la fecha especifica
			line = search_date(text,day)
			print(line)
			#Limpia la linea y la convierte en lista: [FECHA,PRECIP,EVAP,TMAX,TMIN]
			cleaned_line = clean_line_data(line,txt)
			#Obtiene las variables en las cuales hay datos nulos
			nulls_to_sum = check_nulls_in_line(cleaned_line[1:])
			#Suma esos nuevos nulos en la lista de acumulables a cada contador de cada variable
			counterList = sum_nulls(counterList, nulls_to_sum)
		else:
			#Si la fecha no existe en el archivo entonces las 4 variables se toman como nulas
			counterList = sum_nulls(counterList, [1,1,1,1])

	return counterList

def search_date(text,date):

	for line in text:
		print(f'line: {line}, date: {date}')
		if date in line:
			print('Found it!!!')
			return line

def check_nulls_in_line(line):
	"""
	Analiza la lista con formato [PRECIP,EVAP,TMAX,TMIN],
	para ver cuál de todos en nulodates_list_file
	"""
	
	list_to_sum = []
	#Por cada variable [PRECIP,EVAP,TMAX,TMIN]
	for element in line:
		#Si es nulo
		if element == 'Nulo':
			#Se le aumentara uno a la variable
			list_to_sum.append(1)
		else:
			#Sino se le aumentara un cero a la cuenta acumulada de nulos de esa variable
			list_to_sum.append(0)

	return list_to_sum

def sum_nulls(counterList,nulls_to_sum):

	PRECIP 	= counterList[0] + nulls_to_sum[0]
	EVAP 	= counterList[1] + nulls_to_sum[1]
	TMAX 	= counterList[2] + nulls_to_sum[2]
	TMIN 	= counterList[3] + nulls_to_sum[3]

	return [PRECIP, EVAP, TMAX, TMIN]

def clean_line_data(line,txt):
	"""
	Limpia la linea de datos de un solo día de informacion que lleva el siguiento 
	formato: "01/02/2008  0      4.3    31     6.5\n"
	"""
	print(line)
	r1 = line.split('\n')[0] #Removes the '\n'
	r2 = re.sub(REGEX_BLANK_SPACES,' ',r1) #Replaces all concatenated blank spaces by just one of them
	r3 = r2.split(' ')
	
	if r3[len(r3)-1] == '':
		r4 = r3[0:len(r3)-1]
	else:
		r4 = r3

	if len(r4)==5:
		return r4
	else:
		raise ValueError(f"La línea {r4} no contiene el formato: [FECHA,PRECIP,EVAP,TMAX,TMIN] despues de la limpieza para archivo {txt}")

def info_to_write(txt,conteo):
	print(f'txt_dict: {txt} conteo: {conteo}')
	info 	= "Nulos en "+txt+'\n'+"Precipitacion "+str(conteo[0])+'\n' \
												+"Evaporacion " +str(conteo[1])+'\n' \
												+"Tmax "+str(conteo[2])+'\n' \
												+"Tmin "+str(conteo[3])+'\n\n' \

	return info

def get_txt():
	result = subprocess.check_output('ls ../CleanedData/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	#print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def get_name_txt(txt):
	name = txt.split('.txt.txt')[0].split('/')[1]
	return name

def write_file(info):
	
	with open('Nulls.txt','a+') as file:
		file.write(info)


def delete_file():
	file = subprocess.check_output('find . -name Nulls.txt',shell=True)
	if len(file)>0:
		name_file = file.decode().split('/')[1].split('\n')[0]
		print(f"{name_file}")
		if name_file == "Nulls.txt":
			
			print(subprocess.call(['rm', '-rf', 'Nulls.txt']))

def get_dates_file_list(txt):

	with open(txt,'r',encoding = "ISO-8859-1") as archivo:
		text = archivo.read()
		parts = text.split('FECHA')
		dates = re.findall(REGEX_DATES,parts[1])
		#print(f'dates {dates} tam:{len(dates)}')
	return dates

if __name__ == '__main__':
	"""
	files = get_txt()
	with open(files[0],'r',encoding = "ISO-8859-1") as archivito:
		#text = archivito.read()
		#parts = text.split('FECHA')
		#print(parts)
		#data = get_dates_file_list(parts[1])
		for line in archivito:
			print(line)
	
	"""
	print(f'LIST_DAYS: {len(LIST_DAYS)}')
	#delete_file()
	#Evaluate_Towns()
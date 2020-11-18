import subprocess
from dates import generate_date_list
import re
from graphics import graph_global_nulls
import pickle

REGEX_BLANK_SPACES = r'[ ]+'
REGEX_DATES = r'[\d]{2}\/[\d]{2}\/[\d]{4}'
LIST_DAYS = generate_date_list('01/01/2008','31/12/2018')
TOTAL_DAYS_FOR_FILE = 4018
TOTAL_DATA_FOR_FILE = 16072
TOTAL_NULLS = 0
TOTAL_DATA_IN_DATASET = 0
ETAPA_1_PATH = 'Archivos_Etapa_1'
ETAPA_2_PATH = 'Archivos_Etapa_2'
ETAPA_3_PATH = 'Archivos_Etapa_3'
ETAPA_4_PATH = 'Archivos_Etapa_4'
ETAPA_5_PATH = 'Archivos_Etapa_5'
PRE_ETAPAS = 'CleanedData'

PICKLE_PRE_ETAPA = 'pre_etapas_datos_graficas.pickle'
PICKLE_ETAPA_1 = 'etapa1_datos_graficas.pickle'
PICKLE_ETAPA_2 = 'etapa2_datos_graficas.pickle'
PICKLE_ETAPA_3 = 'etapa3_datos_graficas.pickle'
PICKLE_ETAPA_4 = 'etapa4_datos_graficas.pickle'
PICKLE_ETAPA_5 = 'etapa5_datos_graficas.pickle'

def Evaluate_Towns():
	global TOTAL_NULLS
	#Working path debe ser modificado por cada etapa que se desee hacer
	working_path = ETAPA_5_PATH
	current_path = build_path(working_path)
	delete_file(current_path)
	txt_files = get_txt(working_path)
	
	TOTAL_DATA_IN_DATASET = TOTAL_DATA_FOR_FILE * len(txt_files)
	RESULTS_FOR_FILE_LIST = []
	#Por cada archivo
	for txt in txt_files:
		txt_dict = {}
		txt_dict['Path'] = txt
		print(f"File to read: {txt} \n")
		with open(txt,'r',encoding = "ISO-8859-1") as file:

			conteo = find_nulls(file,txt)
			txt_dict['Name'] = get_name_txt(txt_dict['Path'])
			txt_dict['Conteo'] = conteo
			txt_dict['Total_nulos'] = get_total_nulls_for_file(conteo)
			txt_dict['Porcentaje_local_nulos'] = get_percentage(txt_dict['Total_nulos'])
			txt_dict['Total dias existentes'] = len(get_dates_file_list(txt))
			RESULTS_FOR_FILE_LIST.append(txt_dict)
			TOTAL_NULLS += txt_dict['Total_nulos']
	
	write_file('TOTAL DE DATOS QUE DEBEN EXISTIR EN EL DATASET:' + str(TOTAL_DATA_IN_DATASET) + \
				'\nTOTAL DE DATOS NULOS EN EL DATASET:'+ str(TOTAL_NULLS) + \
				'\nTOTAL DE DATOS POR ARCHIVO:'+ str(TOTAL_DATA_FOR_FILE) + \
				'\nTOTAL DE DIAS QUE DEBE CONTENER UN ARCHIVO:' + str(TOTAL_DAYS_FOR_FILE) + '\n\n', current_path)
	
	for txt in RESULTS_FOR_FILE_LIST:
		txt['Porcentaje_global_nulos'] = round(get_global_percentage(txt['Total_nulos']),2)
		write_file(info_to_write(txt),current_path)
	print(RESULTS_FOR_FILE_LIST)
	return RESULTS_FOR_FILE_LIST

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
			#print(line)
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
		#print(f'line: {line}, date: {date}')
		if date in line:
			#print('Found it!!!')
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
	#print(line)
	r1 = line.split('\n')[0] #Removes the '\n'
	r2 = re.sub(REGEX_BLANK_SPACES,' ',r1) #Replaces all concatenated blank spaces by just one txt_dict['Total_nulos']of them
	r3 = r2.split(' ')
	
	if r3[len(r3)-1] == '':
		r4 = r3[0:len(r3)-1]
	else:
		r4 = r3

	if len(r4)==5:
		return r4
	else:
		raise ValueError(f"La línea {r4} no contiene el formato: [FECHA,PRECIP,EVAP,TMAX,TMIN] despues de la limpieza para archivo {txt}")

def info_to_write(txt):
	#print(f'txt_dict: {txt["Name"]} conteo: {txt['Conteo']}')
	#nulls_percentage = get_percentage(txt['Total_nulos'])
	info 	= "Nulos en "+txt['Path']+'\n'+"Precipitacion: "+str(txt['Conteo'][0])+'\n' \
												+"Evaporacion: " +str(txt['Conteo'][1])+'\n' \
												+"Tmax: "+str(txt['Conteo'][2])+'\n' \
												+"Tmin: "+str(txt['Conteo'][3])+'\n' \
												+"Total: " + str(txt['Total_nulos']) + '\n' \
												+"Porcentaje local de nulos en el archivo: " + str(txt['Porcentaje_local_nulos']) + '%\n' \
												+"Total dias existentes en el archivo: " + str(txt['Total dias existentes']) + '\n' \
												+"Porcentaje global de nulos en el archivo: " + str(txt['Porcentaje_global_nulos']) + '%\n\n'

	return info

def get_name_txt(txt):
	name = txt.split('.txt')[0].split('/')[2]
	return name

def get_total_nulls_for_file(conteo):
	return conteo[0] + conteo[1] + conteo[2] + conteo[3]

def get_percentage(total_nulls):
	#total_current_data = TOTAL_DATA_FOR_FILE - total_nulls
	nulls_percentage = (total_nulls * 100)/ TOTAL_DATA_FOR_FILE
	return round(nulls_percentage,1)

def get_global_percentage(total_nulls_file):

	nulls_percentage = (total_nulls_file * 100)/ TOTAL_NULLS
	return nulls_percentage
#					FUNCIONES PARA ARCHIVOS
def get_txt(path_folder):
	result = subprocess.check_output('ls ../'+ path_folder +'/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	#print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def write_file(info,path_file):
	
	with open(path_file + 'Nulls.txt','a+') as file:
		file.write(info)


def delete_file(path_file):
	#file = subprocess.check_output('find . -name '+ path_file +'Nulls.txt',shell=True)
	try:
		file = subprocess.check_output('find '+ path_file +'Nulls.txt',shell=True)
		if len(file)>0:
			parts = file.decode().split('/')#.split('\n')[0]
			name_file = parts[len(parts)-1]
			print(subprocess.call(['rm', '-rf', path_file + 'Nulls.txt']))
	except:
		print('No existe archivo Nulls.txt')

def get_dates_file_list(txt):

	with open(txt,'r',encoding = "ISO-8859-1") as archivo:
		text = archivo.read()
		parts = text.split('FECHA')
		dates = re.findall(REGEX_DATES,parts[1])
		#print(f'dates {dates} tam:{len(dates)}')
	return dates
#					FUNCIONES PARA ARCHIVOS

def build_path(path_folder):
	return '../'+ path_folder +'/'

def get_dump(name):

	with open('../Pickles/'+name, "rb") as a_file:
		output = pickle.load(a_file)
		print(output)
		return output

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
	#print(f'LIST_DAYS: {len(LIST_DAYS)}')
	
	#Esta función analiza todos los archivos y obtiene los nulos
	#result_towns = Evaluate_Towns()

	#Esta funcion obtiene el pickle especifico con la lista de datos
	#que la función Evaluate_Towns() calcula, pero sin necesidad de obtenerlos nuevamente
	option = 0
	while(True):
		option = int(input('Graficar: 0-Pre_Etapa 1-Etapa_1 2-Etapa_2 3-Etapa_3 4-Etapa_4 5-Etapa_5: '))
		if option==0:
			result_towns = get_dump(PICKLE_PRE_ETAPA)
		elif option==1:
			result_towns = get_dump(PICKLE_ETAPA_1)
		elif option==2:
			result_towns = get_dump(PICKLE_ETAPA_2)
		elif option==3:
			result_towns = get_dump(PICKLE_ETAPA_3)
		elif option==4:
			result_towns = get_dump(PICKLE_ETAPA_4)
		elif option==5:
			result_towns = get_dump(PICKLE_ETAPA_5)

		graph_global_nulls(result_towns)
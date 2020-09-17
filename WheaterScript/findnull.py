import re
import subprocess

"""
Este script permite encontrar todos los nulos que existen en los archivos
climaticos de algún municipio.
"""

# https://regex101.com/r/bY2njt/1
# https://regex101.com/r/bY2njt/3

# reg = r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+([\d]+[.\d]*|Nulo)[ ]+([\d]+[.?\d]*|Nulo)[ ]+([\d]+[.\d]*|Nulo)[ ]+([\d]+[.\d]*|Nulo)"
# reg = r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
#														 	PRECIṔ 			 EVAP 		    TMAX 	       TMIN
reg_precip 					= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
reg_evap  					= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
reg_tmax 					= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+[\d]+[.\d]*"
reg_tmin 					= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+Nulo"
reg_tmax_tmin				= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+Nulo"
reg_evap_tmin				= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+Nulo"
reg_evap_tmax				= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+Nulo[ ]+[\d]+[.\d]*"
reg_evap_tmax_tmin	 		= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+Nulo[ ]+Nulo"
reg_precip_tmin 			= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+Nulo"
reg_precip_tmax 			= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+[\d]+[.\d]*"
reg_precip_tmax_tmin 		= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+Nulo"
reg_precip_evap 			= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
reg_precip_evap_tmin 		= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+Nulo"
reg_precip_evap_tmax 		= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+Nulo[ ]+Nulo[ ]+[\d]+[.\d]*"
reg_precip_evap_tmax_tmin	= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+Nulo[ ]+Nulo[ ]+Nulo"



def find_nulls_reg(text,txt_dict):

	txt_dict['precip'] 					= re.findall(reg_precip,text)
	#print(f"precip {txt_dict['precip']}")
	txt_dict['evap'] 					= re.findall(reg_evap,text)
	#print(f"evap {txt_dict['evap']}")
	txt_dict['tmax'] 					= re.findall(reg_tmax,text)
	#print(f"tmax {txt_dict['tmax']}")
	txt_dict['tmin'] 					= re.findall(reg_tmin,text)

	txt_dict['tmax_tmin']				= re.findall(reg_tmax_tmin,text)	

	txt_dict['evap_tmin'] 				= re.findall(reg_evap_tmin,text)

	txt_dict['evap_tmax'] 				= re.findall(reg_evap_tmax,text)

	txt_dict['evap_tmax_tmin'] 			= re.findall(reg_evap_tmax_tmin,text)

	txt_dict['precip_tmin'] 			= re.findall(reg_precip_tmin,text)

	txt_dict['precip_tmax'] 			= re.findall(reg_precip_tmax,text)

	txt_dict['precip_tmax_tmin'] 		= re.findall(reg_precip_tmax_tmin,text)

	txt_dict['precip_evap'] 			= re.findall(reg_precip_evap,text)

	txt_dict['precip_evap_tmin'] 		= re.findall(reg_precip_evap_tmin,text)

	txt_dict['precip_evap_tmax'] 		= re.findall(reg_precip_evap_tmax,text)

	txt_dict['precip_evap_tmax_tmin'] 	= re.findall(reg_precip_evap_tmax_tmin,text)	
	
	return txt_dict

def find_nulls():
	txt_files = get_txt()
	
	#Por cada archivo
	for txt in txt_files:
		name = get_name_txt(txt)
		txt_dict = {}
		txt_dict['Name'] = txt
		print(f"File to read: {txt} \n")
		with open(txt,'r',encoding = "ISO-8859-1") as file:

			text = file.read()
			txt_dict = find_nulls_reg(text,txt_dict)

			write_file(info_to_write(txt_dict))

def count_nulls_per_case(txt_dict):

	#Para Precipitacion se consideran todos los registros que contienen precipitacion
	total_precip 	= 	str(len(txt_dict['precip']) + \
						len(txt_dict['precip_tmin']) + \
						len(txt_dict['precip_tmax']) + \
						len(txt_dict['precip_tmax_tmin']) + \
						len(txt_dict['precip_evap']) + \
						len(txt_dict['precip_evap_tmin']) + \
						len(txt_dict['precip_evap_tmax']) + \
						len(txt_dict['precip_evap_tmax_tmin']))
	#Para evaporacion se consideran todos los registros que contienen evaporacion
	total_evap 	 	=	str(len(txt_dict['evap']) + \
						len(txt_dict['evap_tmin']) + \
						len(txt_dict['evap_tmax']) + \
						len(txt_dict['evap_tmax_tmin']) + \
						len(txt_dict['precip_evap']) + \
						len(txt_dict['precip_evap_tmin']) + \
						len(txt_dict['precip_evap_tmax']) + \
						len(txt_dict['precip_evap_tmax_tmin']))
	#Para tmax se consideran todos los registros que contienen tmax
	total_tmax		=	str(len(txt_dict['tmax']) + \
							len(txt_dict['tmax_tmin']) + \
							len(txt_dict['evap_tmax']) + \
							len(txt_dict['evap_tmax_tmin']) + \
							len(txt_dict['precip_tmax']) + \
							len(txt_dict['precip_tmax_tmin']) + \
							len(txt_dict['precip_evap_tmax']) + \
							len(txt_dict['precip_evap_tmax_tmin']))
	#Para tmin se consideran todos los registros que contienen tmin
	total_tmin 		=	str(len(txt_dict['tmin']) + \
							len(txt_dict['tmax_tmin']) + \
							len(txt_dict['evap_tmin']) + \
							len(txt_dict['evap_tmax_tmin']) + \
							len(txt_dict['precip_tmin']) + \
							len(txt_dict['precip_tmax_tmin']) + \
							len(txt_dict['precip_evap_tmin']) + \
							len(txt_dict['precip_evap_tmax_tmin']))

	return [total_precip,total_evap,total_tmax,total_tmin]


def info_to_write(txt_dict):
	conteo = count_nulls_per_case(txt_dict)
	
	info 	= "Nulos en "+txt_dict['Name']+'\n'+"Precipitacion "+conteo[0]+'\n' \
												+"Evaporacion " +conteo[1]+'\n' \
												+"Tmax "+conteo[2]+'\n' \
												+"Tmin "+conteo[3]+'\n\n' \

	return info

def get_txt():
	result = subprocess.check_output('ls CleanedData/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
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

		
delete_file()
find_nulls()




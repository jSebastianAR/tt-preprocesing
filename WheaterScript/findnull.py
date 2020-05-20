import re
import subprocess

# https://regex101.com/r/bY2njt/1

# reg = r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+([\d]+[.\d]*|Nulo)[ ]+([\d]+[.?\d]*|Nulo)[ ]+([\d]+[.\d]*|Nulo)[ ]+([\d]+[.\d]*|Nulo)"
# reg = r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"

reg_precip 	= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+Nulo[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
reg_evap  	= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+Nulo[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*"
reg_tmax 	= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+Nulo[ ]+[\d]+[.\d]*"
reg_tmin 	= r"[\d]{2}\/[\d]{2}\/[\d]{4}[ ]+[\d]+[.?\d]*[ ]+[\d]+[.\d]*[ ]+[\d]+[.\d]*[ ]+Nulo"

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
			txt_dict['precip'] 	= re.findall(reg_precip,text)
			#print(f"precip {txt_dict['precip']}")
			txt_dict['evap'] 	= re.findall(reg_evap,text)
			#print(f"evap {txt_dict['evap']}")
			txt_dict['tmax'] 	= re.findall(reg_tmax,text)
			#print(f"tmax {txt_dict['tmax']}")
			txt_dict['tmin'] 	= re.findall(reg_tmin,text)
			#print(f"tmin {txt_dict['tmin']}")

			write_file(info_to_write(txt_dict))



def info_to_write(txt_dict):
	salto 	= '\n'
	tab 	= '\t'
	info 	= "Nulos en "+txt_dict['Name']+salto+"Precipitacion "+str(len(txt_dict['precip']))+salto \
	+"Evaporacion " +str(len(txt_dict['evap']))+salto \
	+"Tmax "+str(len(txt_dict['tmax']))+salto \
	+"Tmin "+str(len(txt_dict['tmin']))+salto+salto \

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

find_nulls()



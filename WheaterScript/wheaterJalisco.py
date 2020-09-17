import subprocess
import re
import json

"""
Este script es para extraer los datos climaticos de nuestro interes 
de cada uno de los .txt que obtuvimos de conagua, en este caso
se obtendrán los datos de precipitacion, tempMax,tempMin y evaporación en el periodo 2008-2018
"""

def fill_list():
	return ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

def read_files():
	
	txt_list = get_txt()
	String_Stop = 'FECHA'
	String_restart = r"200[8-9]|201[0-9]"
	DICT_MISSING_YEARS_TOWN = {}
	YEARS = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
	for txt in txt_list:
		name = get_name_txt(txt)
		print(f"=====================================================\nReading {txt}")
		write_log("=====================================================\nReading "+txt)
		MISSING_YEARS_TOWN = fill_list()
		stop = False #Boolean used to stop recolect the data from the file
		aproved=False #Boolean used to know if recolect the data from the file was restarted
		nulls = []
		with open(txt,'r',encoding = "ISO-8859-1") as file:
			
			for line in file:
				
				#si no esta el string que dice que se deje de guardar info
				if String_Stop in line:
					d = line.rstrip('\n')
					print(f"Stopped because of the line {d}")
					write_log("Stopped because of the line "+d)
					stop = True
					write_file(line,txt)
				#si esta el string que permite volver a guardar info
				elif len(re.findall(String_restart,line))>0 and stop==True or len(re.findall(String_restart,line))>0 and aproved==True:
					write_log("Finded year "+str(re.findall(String_restart,line))+" MissingYears: "+str(MISSING_YEARS_TOWN))
					print(f"Finded year {re.findall(String_restart,line)}, len: {len(re.findall(String_restart,line))} MissingYears: {MISSING_YEARS_TOWN}")
					stop = False
					aproved = True

					#Ask if exist in the list of missing years

					if re.findall(String_restart,line)[0] in MISSING_YEARS_TOWN:
						print(f"year deleted {re.findall(String_restart,line)}")
						write_log("year deleted" +str(re.findall(String_restart,line)))
						MISSING_YEARS_TOWN.remove(re.findall(String_restart,line)[0]) #Delete the year

				#Si el boleano permite guardar info	
				if stop==False:
					#print(f"Writing {line}")
					write_file(line,txt)#EScribe en archivo

				

		DICT_MISSING_YEARS_TOWN[name] =	MISSING_YEARS_TOWN #Save the missing years of the town
		print(f"=====================================================\n")
		write_log("=====================================================")
	
	#write_missing_years(DICT_MISSING_YEARS_TOWN)

def get_name_txt(txt):
	name = txt.split('.txt.txt')[0].split('/')[1]
	return name

def get_txt():
	result = subprocess.check_output('ls Dataset\ Clima\ Diario/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def write_file(line,txt):
	name = get_name_txt(txt)
	#with open('CleanedData/'+name+'-Cleaned','a+') as file:
	with open('CleanedData/'+name,'a+') as file:
		file.write(line)

def write_file_missing_years(line):
	with open('missingYearsPerTown.txt','a+') as file:
		file.write(line+'\n')	

def write_missing_years(l):

	for key in l:
		write_file_missing_years(key)
		for year in l[key]:
			write_file_missing_years(year)
		write_file_missing_years('\n')

def write_log(line):
	with open('log.txt','a+') as file:
		file.write(line+'\n')	

result = read_files()

print(result)
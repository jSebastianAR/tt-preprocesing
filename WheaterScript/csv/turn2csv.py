import pandas as pd
import re
import subprocess
import time

REGEX_BLANK_SPACES = r'[ ]+'
COLUMNAS = ['FECHA','PRECIP(mm)','EVAP(mm)','TMAX(°C)','TMIN(°C)']
PATH_E5 = 'Archivos_Etapa_5'

#Obtendrá cada uno de los datos del archivo de cada town
def getContent(path,name):
    dataList = []
    #Flag que indicará si ya se puede obtener info
    getDailyData = lambda line: True if ('FECHA' in line) else False
    isLastLine = lambda line: True if('--------------------------------------' in line) else False #Si la última linea es leida 
    
    #Agregará la línea de datos si la bandera obtenida por getDailyData es true
    evaluateLine = lambda line,flag: dataList.append(clean_line_data(line)) if(flag and not(isLastLine(line))) else False
    getData = False

    with open(path,'r',encoding = "ISO-8859-1") as file:

        #Por cada línea de archivo
        for line in file:

            evaluateLine(line,getData)
            if getDailyData(line) and getData==False:
                getData = True
    
    print(f'Content for {name}: \n\n{dataList}')
    return dataList

def clean_line_data(line):

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
        raise ValueError(f"La línea {r4} no contiene el formato: [FECHA,PRECIP,EVAP,TMAX,TMIN] despues de la limpieza para archivo ")

def get_txt(path_folder):
	result = subprocess.check_output('ls ../'+ path_folder +'/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	#print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def get_name_txt(path_file):
    parts = path_file.split('/')
    name = parts[len(parts)-1]
    print(name)
    return name

def to_csv(list_content,filename):
    town_df = pd.DataFrame(list_content,columns=COLUMNAS)
    town_df.to_csv('csv_dataset/' + filename + '.csv')

def do_turn2csv(txt_list):

    for txt in txt_list:
        name = get_name_txt(txt)
        if name != 'Nulls.txt':
            content = getContent(txt,name)
            to_csv(content,name)

def main():
    current_path = PATH_E5
    txt_list = get_txt(current_path)
    do_turn2csv(txt_list)
    

if __name__ == '__main__':
    main()
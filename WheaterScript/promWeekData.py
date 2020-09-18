"""
Este script permitirá realizar un promedio de datos climaticos por semana
reduciendo así la cantidad de datos que se tienen.
"""
import re

REGEX_YEAR_STRING_PART1 = '\\d{2}\\/\\d{2}\\/'
REGEX_YEAR_STRING_PART2 = '([ ]+[\d]+(\.[\d]+)?){4})'
#REGEX_YEAR_STRING2 = '(\d{2}\/\d{2}\/\d{4}([ ]+[\d]+(\.[\d]+)?){4})'
REGEX_YEAR_STRING2 = '(\\d{2}\\/\\d{2}\\/\\d{4}([ ]+[\\d]+(\\.[\\d]+)?){4})'
YEARS = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

def make():

    list_towns = get_towns()
    #get_data_per_year = lambda year: expression

    for town in list_towns:
        
        data_town = read_file_town(town)
        
        for year in YEARS:
            regex_year = build_regex(year)
            data_per_year = get_data_per_year(data_town,regex_year)
            list_data_per_year = get_values_line(data_per_year)
            



def read_file_town(name_file):

    with open('CleanedData/'+name_file) as file:
        return file.read()

def build_regex(year):
    regex = REGEX_YEAR_STRING_PART1+year+REGEX_YEAR_STRING_PART2
    return re.compile(regex)

def get_values_line(data_per_year):

    list_data_per_year = []
    for line in data_per_year:
        splited_line = line.split(' ')
        list_data_per_year.append({'precip':splited_line[1],'evap':splited_line[2],'tmax':splited_line[3],'tmin':splited_line[4]})
    
    return list_data_per_year

def get_data_per_year(data,regex):
    return re.findall(regex,data,re.DOTALL)

def get_prom_week(lines):

    precip = 0
    evap = 0
    tmax = 0
    tmin = 0

    for line in lines:
        precip += float(line['precip'])
        evap += float(line['evap'])
        tmax += float(line['tmax'])
        tmin += float(line['tmin'])

    precip = precip/len(lines)
    evap = evap/len(lines)
    tmax = tmax/len(lines)
    tmin = tmin/len(lines)

    return {'precip':precip,'evap':evap,'tmax':tmax,'tmin':tmin}

def get_towns():
    
    with open('Municipios con información completa.txt') as file:
        
        data = file.read()
        towns_list = data.split('\n')[1:]
        return towns_list

def get_txt():
	result = subprocess.check_output('ls Dataset\ Clima\ Diario/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

if __name__ == '__main__':
    list_towns = get_towns()
    print(f'numtowns:{len(list_towns)}\n\nTowns:\n{list_towns}')
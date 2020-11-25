import sys
from pathlib import Path
from time import sleep
import pandas as pd
#Importando el modulo Towns
current_path = Path().absolute().as_posix()
parts = current_path.split('/')
parent_path = '/'.join(parts[1:len(parts)-1])
project_data_path = '/' + parent_path + '/project_data'
pickles_path = '/' + parent_path + '/Pickles'
sys.path.append(project_data_path)
sys.path.append(pickles_path)
from towns import Towns
import pickles as pk

path_pickles = '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/Pickles/'

def compare_list(original,fake,calculated):
    tam = len(original)
    for index in range(0,tam):
        #Si son distintos entonces encontro el nulo falso
        if original[index] != fake[index]:
            #Retorna el valor original y el valor calculado por el algoritmo
            return original[index],calculated[index]


def createCSV(list_content):
    COLUMNS = ['Archivo','Original','Falso nulo','Calculada','Valor O','Valor C']
    town_df = pd.DataFrame(list_content,columns=COLUMNS)
    town_df.to_csv('tabla_fake_nulls.csv')

def analyze_nulls(town,dict_fake_nulls):
    list_compare = []
    c = 0
    #Por cada nulo que hay en all_fakes
    for null_date in dict_fake_nulls['all_fakes']:
        #Si encuentra la llave de la fecha
        if town.index_date.get(null_date) != None:
            #Obtiene el indice donde esta esa linea
            index = town.index_date[null_date]
            #Obtiene la linea nueva
            calculated_line = town.content[index]
            #Obtiene la linea con el nulo
            null_line = dict_fake_nulls['all_fakes'][null_date]['fake']
            #Obtiene la linea con el original
            original_line = dict_fake_nulls['all_fakes'][null_date]['original']
            print(f'Original: {original_line} Fake null: {null_line} Calculated: {calculated_line}')
            #Obtiene el valor original y el calculado
            original_value, calculated_value = compare_list(original_line[1:],null_line[1:],calculated_line[1:])
            #Guarda la relacion en una lista
            list_compare.append([town.name,original_line, null_line, calculated_line,original_value,calculated_value])
        else:
            c +=1
            print(f'{c} nulos que no se pueden analizar')
        #sleep(0)
    return list_compare

def set_global_dict_fake_nulls(nulls_list):
    global_dict = {}
    for null in nulls_list:
        name_town = null['nombre']
        path = null['path']
        all_fakes = null['all_fakes']
        global_dict[name_town] = {'path': path, 'all_fakes': all_fakes}
    
    return global_dict

def main():

    paths = pk.get_dump( path_pickles + 'paths_file_f6.pickle')
    fakeNulls_dict = pk.get_dump( path_pickles + 'fake_nulls.pickle')
    #print(paths)
    #print(fakeNulls_dict)
    dict_fake_nulls = set_global_dict_fake_nulls(fakeNulls_dict)
    #print(dict_fake_nulls)
    final_list_nulls = []
    for key in paths:
        if key<=134:
            path_file = paths[key]
            new_town = Towns(path_file,0,0,0)
            print(f'Analizando: {new_town.name}')
            new_town.getContent()
            new_town.find_indexes_for_dates('01/01/2008','31/12/2018')
            fake_nulls = dict_fake_nulls[new_town.name]
            final_list_nulls.extend(analyze_nulls(new_town,fake_nulls)) #Agrega la lista de relacion de nulos
        else:
            break

    createCSV(final_list_nulls)
if __name__ == '__main__':
    main()



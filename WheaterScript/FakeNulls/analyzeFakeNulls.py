import sys
from pathlib import Path
from time import sleep
import pandas as pd
import numpy as np
#Importando el modulo Towns
current_path = Path().absolute().as_posix()
parts = current_path.split('/')
parent_path = '/'.join(parts[1:len(parts)-1])
project_data_path = '/' + parent_path + '/project_data'
pickles_path = '/' + parent_path + '/Pickles'
sys.path.append(project_data_path)
sys.path.append(pickles_path)
from towns import Towns # MARCA ERROR EN AMBOS IMPORTS DADO QUE SON IMPORTADOS DE OTRO 
import pickles as pk    # DIRECTORIO, PERO AUN ASÍ FUNCIONA

path_pickles = '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/Pickles/'

def compare_list(original,fake,calculated):
    tam = len(original)
    for index in range(0,tam):
        #Si son distintos entonces encontro el nulo falso
        if original[index] != fake[index]:
            #Retorna el valor original y el valor calculado por el algoritmo
            return original[index],calculated[index]


def createCSV(list_content):
    """
    Lista de listas con la sig estructura

    [[val1,val2,val3,...valn],[val1,val2,val3,...valn],[val1,val2,val3,...valn]]

    Cada lista interna representa una fila del .csv
    Cada valor de cada lista interna representa el n valor en la n columna
    """
    #Columnas del csv
    COLUMNS = ['Archivo','Original','Falso nulo','Calculada','Valor O','Valor C']
    #Se crea el dataframe con la informacion
    town_df = pd.DataFrame(list_content,columns=COLUMNS)
    #Se crea el csv
    #print(f'LIST_CONTENT\n {list_content}')
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
    #Para todos los nulos
    for null in nulls_list:
        #Obtiene el nombre del archivo
        name_town = null['nombre']
        #Obtiene el path
        path = null['path']
        #obtiene los falsos nulos
        all_fakes = null['all_fakes']
        #Guarda todo en el diccionario de nulos
        global_dict[name_town] = {'path': path, 'all_fakes': all_fakes}
    
    return global_dict

def get_csv_data():
    #Lee el .csv
    data = pd.read_csv('./tabla_fake_nulls.csv')
    #Obtiene la columna con los valores originales
    original_value = data['Valor O'].to_numpy()
    #Obtiene la columna con los valores calculados
    calculated_value = data['Valor C'].to_numpy()

    return original_value, calculated_value

def eficiency():
    #Obtiene las dos columnas a comparar
    valor_o, valor_c = get_csv_data()
    #Calcula la diferencia de ambas
    difference = np.subtract(valor_o,valor_c)
    #Convierte en positivos todos los resultados negativos
    for index in range(0,len(difference)):
        if difference[index] < 0:
            difference[index] = (-1) * difference[index]
    print(f'Difference array\n {difference}')
    #Calcula el promedio de los resultados obtenidos
    efficiency_mean = round(np.mean(difference),2)
    print(efficiency_mean)

def main():

    paths = pk.get_dump( path_pickles + 'paths_file_f6.pickle')
    fakeNulls_dict = pk.get_dump( path_pickles + 'fake_nulls.pickle')
    #print(paths)
    #print(fakeNulls_dict)
    dict_fake_nulls = set_global_dict_fake_nulls(fakeNulls_dict)
    #print(dict_fake_nulls)
    final_list_nulls = []
    #Por cada key
    for key in paths:
        if key<=134:
            #obtiene el path del archivo
            path_file = paths[key]
            #Crea una nueva ciudad
            new_town = Towns(path_file,0,0,0)
            print(f'Analizando: {new_town.name}')
            #Obtiene el contenido de esa ciudad
            new_town.getContent()
            #Obtiene los indices de las fechas
            new_town.find_indexes_for_dates('01/01/2008','31/12/2018')
            #Obtiene los nulos falsos agregados a esa ciudad
            fake_nulls = dict_fake_nulls[new_town.name]
            #Agrega el resultado de comparar los nulos
            final_list_nulls.extend(analyze_nulls(new_town,fake_nulls)) #Agrega la lista de relacion de nulos
        else:
            break
    #Crea el .csv
    createCSV(final_list_nulls)
if __name__ == '__main__':
    main()
    #eficiency()



from towns import get_distances_between_towns
from towns import build_towns, getValuesTown
import dates as dt
from nwsm import do_refill_data
import time
from writerFile import Writer
import pickle
from filechooser import get_lon_lat
import pickle

PATH_E1 = './Etapa_1/'
PATH_E2 = './Etapa_2/'
PATH_E3 = './Etapa_3/'
PATH_E4 = './Etapa_4/'


def bitacora(info,path):
        with open('/home/Archivos_Etapa_4/' + 'ArchivosLlenados.txt','a+', encoding = "utf-8") as file:
            file.write(info+'\n')

def save_last_key(key,path):
    path = '/home/shared_container/'
    with open(path + 'key.pickle', "wb") as a_file:
        pickle.dump(key, a_file, protocol=pickle.HIGHEST_PROTOCOL)
        a_file.close()

def get_next_key(path):
    path = '/home/shared_container/'
    with open(path + 'key.pickle', "rb") as a_file:
        output = pickle.load(a_file)
        return output + 1

def read_pickle(name,path):
    with open(path + name, "rb") as a_file:
        output = pickle.load(a_file)
    return output

def getLON_LAT(path_TF,paths_TU):
     #Get Lat and Lon of each town  
    towntofill_latlon = get_lon_lat(path_TF)
    townstouse_latlon = list(map(get_lon_lat,paths_TU))

    #print(f'Archivo a llenar: {filename_tofill}\n\nArchivos a usar para llenar: {files_touse}\n\n')
    #print(townstouse_latlon,towntofill_latlon)
    return {'tofill':towntofill_latlon,'touse':townstouse_latlon}

def get_paths_TUs(key,dict_rel,dict_paths):

    paths_TUs = [] 
    #Por cada indice que existe en la lista de relaciones de la TF con las TUs
    for index in dict_rel[key]:
        #Si el indice no es None
        if index != None:
            #Agrega el path a la lista
            paths_TUs.append(dict_paths[index])
    return paths_TUs

def run():
    #Obtiene los paths de todas los archivos
    dict_paths = read_pickle('paths_file_e4.pickle',PATH_E4)
    #Obtiene las listas de relacion de todas las ciudades con sus respectivas TU's
    dict_rel = read_pickle('rel_TF_TU.pickle',PATH_E4)
    #Obtiene el último valor de llave donde se detuvo el algoritmo(si es que se detuvo)
    next_index = get_next_key(PATH_E4)
    print(f'START KEY {next_index}')
    #Por cada key que hay en el diccionario que contiene todos los paths
    for key in range(next_index,len(dict_paths)+1):
        #Obtiene la TF
        path_TF = dict_paths[key]
        #Lista para las TUs
        paths_TUs = get_paths_TUs(key, dict_rel, dict_paths)
        data = getLON_LAT(path_TF, paths_TUs)
        #Calcula la distancia entre ciudades
        data_towns = get_distances_between_towns(data)
        towns_list = build_towns(data_towns)
        town_tf = towns_list[0] #Toma la TF ubicada en la primer posicion
        #print(towns_list)
        print(f"Values town: {list(map(getValuesTown,towns_list))}")

        dates = {'from': '01/01/2008', 'to': '31/12/2018'}

        for town in towns_list:
            print(f'Getting content for Town: {town.name}...')
            town.getContent()
            town.find_indexes_for_dates(dates['from'],dates['to'])
            time.sleep(.5)
        
        #Obtiene los nuevos datos con base en el algoritmo nwsm
        new_data = do_refill_data(towns_list, dt.generate_date_list(dates['from'],dates['to']),False)
        #Obtiene los indices donde se guardara la informacion nueva
        town_tf.get_start_index(dates['from'])
        #Inserta los nuevos datos en la lista final
        town_tf.refill_content(new_data)
        #Crea el escritor de archivos con base en el path de origen del archivo
        wrt = Writer(town_tf.path)
        #Crea un nuevo archivo y escribe todo el contenido
        wrt.newFile(town_tf.content)
        #Escribiendo en registro el archivo que fue llenado
        bitacora(town_tf.name,PATH_E4)
        #Guardando la última key que tenía el último archivo que se lleno
        save_last_key(key,PATH_E4)
        print('Esperando 25 segundos antes de volver...')
        time.sleep(25)
    
if __name__ == '__main__':
    run()
    #next_index = get_next_key()
    #print(next_index)
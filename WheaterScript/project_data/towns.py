from math import sin, cos, sqrt, atan2, radians
import dates as dt
import re
from random import randint, choice
from writerFile import Writer
import pickle
"""
KEYWORDS:

TF: Town to fill, se refiere a la ciudad de la cual se van a estar llenando datos con respecto
a otras ciudades

TU: Town to use, se refiere a cada una de las ciudades a usar para llenar los datos faltantes en TF
"""

REGEX_BLANK_SPACES = r'[ ]+'

#Obtiene la distancia entre TF con respecto a las TU
def get_distances_between_towns(dict_files):

    getDistances_lambda = lambda towntouse: getDistance(dict_files['tofill'][1],dict_files['tofill'][2],towntouse[1],towntouse[2]) #Distancia entre la TF a llenar datos y una TU
    all_distances = list(map(getDistances_lambda,dict_files['touse'])) #Mapea todas las ciudades a usar para el llenado y calcula las distancias
    
    #print(all_distances)
    appendNewDistance_lambda = lambda current_list,index: current_list.append(all_distances[index]) #Agrega las distancias que tiene cada TU con TF
    [appendNewDistance_lambda(townlist,dict_files['touse'].index(townlist)) for townlist in dict_files['touse']]
    
    #print(f'final data: {dict_files}')

    return dict_files

#Obtiene la distancia entre dos lugares dada la latitud y longitud de cada lugar
def getDistance (latPointA, lonPointA, latPointB, lonPointB):

    radiusOfEarth = 6373.0

    lat1 = radians(latPointA)
    lon1 = radians(lonPointA)
    lat2 = radians(latPointB)
    lon2 = radians(lonPointB)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radiusOfEarth * c

    return round(distance,2)

"""
Funcion que construye instancias de la clase Towns para la TF y las TU, que hasta el momento
en que se llama a esta funcion habían estado representadas por listas donde se guardan todos sus datos

Recibe data_towns: un diccionario con las keys: 'tofill' y 'touse' donde:

tofill: guarda en una lista la info de la TF de la siguiente forma
        [path,lat,lon]

touse: Es una lista de listas, donde cada lista indexada es una TU, su estructura es la sig:
        [[path,lat,lon,dist],[path,lat,lon,dist], ...]

Donde:

path = ruta completa del archivo de la ciudad que contiene los datos a usar.
lat = latitud donde se encuentra la ciudad, extraida del archivo señalado por 'path'
lon = longitud donde se encuentra la ciudad, extraida del archivo señalado por 'path'
dist = La distancia entre la TU y la TF (Cada TU tiene su propia dist)
"""
def build_towns(data_towns):

    list_towns = []
    list_towns.append(Towns(data_towns['tofill'][0],data_towns['tofill'][1],data_towns['tofill'][2],0.0)) #instancia de TF

    num_towns = len(data_towns['touse'])
    #Instancia de cada TU
    for x in range(0,num_towns):
        new_town = Towns(data_towns['touse'][x][0],data_towns['touse'][x][1],data_towns['touse'][x][2],data_towns['touse'][x][3])
        list_towns.append(new_town)

    return list_towns

def getValuesTown(town):
    list_values = [town.path,town.lat,town.lon,town.dist,town.name,town.content]
    return list_values

class Towns(object):
    
    #Constructor
    def __init__(self, path, lat, lon, dist):
        self.path = path
        self.lat = lat
        self.lon = lon
        self.dist = dist #Este parámetro tendrá un valor válido para las TU
        self.content = []
        self.name = self.getNameTown(path)
        self.index_date = {}
        self.boundaries_indexes = {'first': None, 'last': None} #Guarda el primer y último indice donde se ubican los datos a llenar
        self.fake_nulls = {}

    #Obtiene el nombre respecto al path
    def getNameTown(self,path):
        data = path.split('/')
        return data[len(data)-1]

    #Obtendrá cada uno de los datos del archivo de cada town
    def getContent(self):
        dataList = []
        #Flag que indicará si ya se puede obtener info
        getDailyData = lambda line: True if ('FECHA' in line) else False
        isLastLine = lambda line: True if('--------------------------------------' in line) else False #Si la última linea es leida 
        
        #Agregará la línea de datos si la bandera obtenida por getDailyData es true
        evaluateLine = lambda line,flag: dataList.append(self.clean_line_data(line)) if(flag and not(isLastLine(line))) else False
        getData = False

        with open(self.path,'r',encoding = "ISO-8859-1") as file:

            #Por cada línea de archivo
            for line in file:

                evaluateLine(line,getData)
                if getDailyData(line) and getData==False:
                    getData = True
        
        self.content = dataList
        #print(f'Content for {self.name}: \n\n{self.content}')

    def clean_line_data(self,line):

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
            raise ValueError(f"La línea {r4} no contiene el formato: [FECHA,PRECIP,EVAP,TMAX,TMIN] despues de la limpieza para archivo {self.name}")
    
    #Encuentra los index en el array de contenido lo que permite saber entre qué valores se estara llenando el array
    def find_indexes_for_dates(self,init_date,final_date):
    
        self.index_date = {}
        current_date_dt = dt.string2datetime(init_date)
        final_date_dt = dt.string2datetime(final_date)

        while (current_date_dt <= final_date_dt):
            
            current_date_str = dt.datetime2string(current_date_dt) #Convierte la fecha actual a str

            #Calcula la fecha de un día anterior
            prev_current_date_str = dt.datetime2string(dt.subsDay2Date(current_date_dt)) 
            #Si la fecha anterior tiene un indice que no es None
            if self.index_date.get(prev_current_date_str) != None:
                start_index = self.index_date[prev_current_date_str] #Obtiene el indice de busqueda para reducir tiempo
            else:
                start_index = 0 #busca desde el inicio
            #print(start_index,prev_current_date_str)
            for data_line in self.content[start_index:]:

                bool_date = dt.currentDayOlder_ThanDate(data_line[0].split('/'), current_date_str.split('/'))

                #data_line[0] > current_day,  la fecha buscada no está
                # or Si se ha llegado al final del archivo y no se encontro la fecha
                #if (bool_date == True) or (self.content.index(data_line) == len(self.content) -1):
                if (bool_date == True):
                    self.index_date[current_date_str] = None
                    break
                #Ha encontrado la fecha
                elif bool_date == 'This':
                    self.index_date[current_date_str] = self.content.index(data_line)
                    #Si aun no se ha guardado el primer indice válido de fechas
                    if self.boundaries_indexes['first'] == None:
                        #Guarda el indice
                        self.boundaries_indexes['first'] = self.index_date[current_date_str]
                    break
                #Si está en el último elemento y la fecha jamas alcanzo la que se buscaba
                elif (self.content.index(data_line) == len(self.content) -1) and bool_date==False:
                    self.index_date[current_date_str] = None
                    break

            current_date_dt = dt.addDay2Date(current_date_dt)
        
            #Obtiene el indice donde se debe poner el último elemento
        if self.boundaries_indexes['first'] != None:
            self.boundaries_indexes['last'] = self.boundaries_indexes['first'] + len(self.index_date) - 1

        print(self.index_date)
    def get_start_index(self,init_date):
        """
        current_date_dt = dt.subsDay2Date(dt.string2datetime(init_date))
        current_date_str = dt.datetime2string(current_date_dt)
        for key in self.index_date:
            if self.index_date[current_date_str] != None:
                self.boundaries_indexes['first'] = self.index_date[current_date_str]
                return
            else:
                current_date_dt = dt.subsDay2Date(current_date_dt)
                current_date_str = dt.datetime2string(current_date_dt)
        """
        #Si no encontro ningún indice(en el caso de que no exista ninguna fecha)
        current_date_dt = dt.subsDay2Date(dt.string2datetime(init_date))
        current_date_str = dt.datetime2string(current_date_dt)
        flag = False
        print(f'content: {self.content}')
        if self.boundaries_indexes['first'] == None:
            #Mientras el indice de la fecha de inicio para insertar los nuevos datos siga siendo None
            # o se llegué a la primer fecha que debe tener un archivo
            while (self.boundaries_indexes['first']== None or current_date_str != '01/01/2008'):
                print(f'LOOKING FOR: {current_date_str}')
                #Por cada linea de datos del archivo leido
                for data_line in self.content:
                    #Evalua si encontro la linea con la fecha requerida
                    print(f'comparando {data_line[0]} - {current_date_str}')
                    bool_date = dt.currentDayOlder_ThanDate(data_line[0].split('/'), current_date_str.split('/'))
                    #Si la encontro
                    if bool_date == 'This':
                        #Guarda el indice donde se encuentra esa linea, para comenzar a insertar los nuevos datos alli
                        print(f'ENCONTRE LA LINEA DE FRONTERA!!!: {data_line}')
                        self.boundaries_indexes['first'] = self.content.index(data_line) + 1
                        flag = True
                        break
                if flag:    
                    break
                else:
                    current_date_dt = dt.subsDay2Date(current_date_dt)
                    current_date_str = dt.datetime2string(current_date_dt)
        
        #Si continua siendo None (No hay ninguna fecha en el archivo)
        if self.boundaries_indexes['first'] == None:
            #Comenzará a insertar los datos desde el primer indice
            self.boundaries_indexes['first'] = 0

        self.boundaries_indexes['last'] = self.boundaries_indexes['first'] + len(self.index_date) - 1
        print(f'Boundaries: {self.boundaries_indexes["first"]},{self.boundaries_indexes["last"]}')

    def delete_old_content(self):
        del self.content[self.boundaries_indexes['first']:self.boundaries_indexes['last']+1]
        #print(f'after del {self.content}')

    def append_new_data(self,new_data):
        #print(f'new_data {new_data}')
        index_new_data = 0
        for index in range(self.boundaries_indexes['first'],self.boundaries_indexes['last']+1):
            self.content.insert(index,new_data[index_new_data])
            index_new_data += 1

    def refill_content(self,new_data):

        self.delete_old_content()
        self.append_new_data(new_data)

    def set_fake_nulls(self):
        dict_all_fakes = {}
        for i in range(0,3):
            random_fakeNull = 'Nulo'
            dict_fake_null = {}
            while(random_fakeNull == 'Nulo'):
                random_dataDay = choice(self.content) #Obtiene un día con datos
                random_fakeNull = choice(random_dataDay[1:])#Obtiene una variable no nula
            
            #Obtiene el indice donde esta la lista de datos
            index_original_day = self.content.index(random_dataDay)
            #Guarda el original como tupla para no sobreescribir cuando se modifique la lista
            dict_fake_null['original'] = tuple(random_dataDay)
            #Obtiene el indice del valor a sustituir
            index_fakeNull = random_dataDay.index(random_fakeNull)
            #Guarda la lista original
            dict_fake_null['fake'] = random_dataDay
            #Sustituye el valor por un fake nulo
            dict_fake_null['fake'][index_fakeNull] = 'Nulo' #se sustituye
            #Agrega los datos del diccionario de fake nulos a la lista
            dict_fake_null['original'] = list(dict_fake_null['original'])
            #Agrega en el diccionario y como llave, esta la fecha donde se tomo el nulo
            dict_all_fakes[dict_fake_null['original'][0]]= dict_fake_null
            #Sustituye el original por el que contiene el nulo
            self.content[index_original_day] = dict_fake_null['fake']

        #Guarda el nombre del archivo
        self.fake_nulls['nombre'] = self.name
        #Guarda el path del archivo
        self.fake_nulls['path'] = self.path
        self.fake_nulls['all_fakes'] = dict_all_fakes

def get_dump(name):

	with open(name, "rb") as a_file:
		output = pickle.load(a_file)
		print(output)
		return output

def dump_file(data,name):
	with open(name, "wb") as a_file:
		pickle.dump(data, a_file, protocol=pickle.HIGHEST_PROTOCOL)
		a_file.close()

if __name__ == '__main__':
    """path = '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14025-TEOCALTICHE.txt'
    lat = 20.421
    lon = -103.591
    dist = 0
    town = Towns(path,lat,lon,dist)

    town.getContent()
    #print(town.content)
    #town.find_indexes_for_dates('01/01/2008','31/12/2018')
    town.set_fake_nulls()
    print(f'LOS PINCHES NULOS ALV {town.fake_nulls}\n\n\n')
    for date in town.fake_nulls['all_fakes']:
        index = town.index_date[date]
        print(town.content[index])
    #print(town.content)
    wrt = Writer(town.path)
    wrt.newFile(town.content)"""

    """paths_dict = get_dump('../Pickles/paths_file_e1.pickle')
    List_fake_nulls = []
    for index in paths_dict:
        if index<=134:
            town = Towns(paths_dict[index],0.0,0.0,0.0)
            town.getContent()
            town.set_fake_nulls()
            wrt = Writer(town.path)
            wrt.newFile(town.content)
            print(f'NULOS DE {town.name} : {town.fake_nulls}\n\n')
            List_fake_nulls.append(town.fake_nulls)
        else:
            break
    
    dump_file(List_fake_nulls,'fake_nulls.pickle')"""

    get_dump('fake_nulls.pickle')
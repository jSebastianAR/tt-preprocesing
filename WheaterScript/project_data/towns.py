from math import sin, cos, sqrt, atan2, radians
import dates as dt
import re
#from dates import currentDayOlder_ThanDate

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
    
    print(all_distances)
    appendNewDistance_lambda = lambda current_list,index: current_list.append(all_distances[index]) #Agrega las distancias que tiene cada TU con TF
    [appendNewDistance_lambda(townlist,dict_files['touse'].index(townlist)) for townlist in dict_files['touse']]
    
    print(f'final data: {dict_files}')

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
    def find_index_forDate_nindex(self,init_date,final_date):
    
        self.index_date = {}
        current_date_dt = dt.string2datetime(init_date)
        final_date_dt = dt.string2datetime(final_date)

        while (current_date_dt <= final_date_dt):
            
            current_date_str = dt.datetime2string(current_date_dt)
            for data_line in self.content:

                bool_date = dt.currentDayOlder_ThanDate(data_line[0].split('/'), current_date_str.split('/'))

                #current_day > data_line[0] la fecha buscada no está
                if bool_date == True:
                    self.index_date[current_date_str] = None
                    break
                #Ha encontrado la fecha
                elif bool_date == 'This':
                    self.index_date[current_date_str] = self.content.index(data_line)
                    break
                

            current_date_dt = dt.addDay2Date(current_date_dt)
        print(self.index_date)
    
    #Encuentra los index en el array de contenido lo que permite saber entre qué valores se estara llenando el array
    def find_index_forDate(self,init_date,final_date):
    
        self.index_date = {}
        init_founded = False
        final_founded = False

        get_index_lambda = lambda index: 0 if (index==-1) else (index)

        for data_line in self.content:
            #print(data_line[0])
            bool_init_date = dt.currentDayOlder_ThanDate(data_line[0].split('/'),init_date.split('/'))
            bool_final_date = dt.currentDayOlder_ThanDate(data_line[0].split('/'),final_date.split('/'))

            #Si current_date>eval_date
            if bool_init_date == True and init_founded==False:
                self.index_date['init_date_index'] = get_index_lambda(self.content.index(data_line)-1) #retorna el indice del elemento anterior
                init_founded = True
            #Si current_date==eval_date
            elif bool_init_date == 'This' and init_founded==False:
                self.index_date['init_date_index'] = self.content.index(data_line) #retorna el indice del elemento actual
                init_founded = True

            if bool_final_date == True and final_founded==False:
                self.index_date['final_date_index'] = get_index_lambda(self.content.index(data_line)-1) #retorna el indice del elemento anterior
                #print(f'====================={self.index_date}=====================')
                final_founded = True
                break
            elif bool_final_date == 'This' and final_founded==False:
                self.index_date['final_date_index'] = self.content.index(data_line) #retorna el indice del elemento actual
                #print(f'====================={self.index_date}=====================')
                final_founded = True
                break
            

        print(f'Dates founded!!!: \n{self.content[self.index_date["init_date_index"]]}:{self.content[self.index_date["final_date_index"]]}')
        
        return self.index_date
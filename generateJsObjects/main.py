import re
from time import sleep
import json


REGEX_PLACEMARK = r'<Placemark>(.*?)<\/Placemark>'
REGEX_NAMETOWN = r'<SimpleData name=\"NOMGEO\">(.*?)</SimpleData>'
REGEX_GETLOCATION = r'<Polygon><outerBoundaryIs><LinearRing><coordinates>(.*?)</coordinates></LinearRing></outerBoundaryIs></Polygon>'

def openFile(name):
    with open(name, 'r') as target:
        return target.read()    
        

def getTowns(datafile):
    listTowns = re.findall(REGEX_PLACEMARK,datafile,re.DOTALL) #Lee todo el contenido de cada uno de los municipios
    return listTowns#Retorna los datos

def getDataForTowns(listTowns):
    time = 0
    #Por cada elemento(que tiene datos de un municipio)
    for town_data in listTowns:
        name = re.findall(REGEX_NAMETOWN,town_data) #Obtiene el nombre del municipio
        print(f'Generando archivo para {name[0]}')
        datalocation = re.findall(REGEX_GETLOCATION,town_data) #Obtiene la lista de lat y lon del municipio
        str_dataPoints = getMapPoints(datalocation[0]) #Obtiene un string con la estructura de la variable en js
        jsVar = buildJsVariable(name[0],str_dataPoints) #Construye la declaración completa de una variable js
        saveJsVariable(jsVar,name[0])
        sleep(time)

def getMapPoints(datalocation):
    #Separa cada par de coordenadas en una lista
    pointsList = datalocation.split(' ')
    #print(pointsList)
    FINAL_COORDS = []
    #Genera por cada coordenada un diccionario
    for point in pointsList:
        dictionary = {}
        coords = point.split(',')
        dictionary['lng'] = float(coords[0])
        dictionary['lat'] = float(coords[1])
        #Guarda el diccionario convertido a string
        FINAL_COORDS.append(json.dumps(dictionary))
    
    #Convierte toda la lista en un solo string
    FINAL_COORDS_STRING = ', '.join(FINAL_COORDS)
    return FINAL_COORDS_STRING

def buildJsVariable(name,datapoints):
    FINAL_COORDS_STRING = 'let '+ name +' = ['+ datapoints +']'
    FINAL_COORDS_STRING = FINAL_COORDS_STRING.replace('"','')
    #print(FINAL_COORDS_STRING)
    return FINAL_COORDS_STRING

def saveJsVariable(jsVar,nameFile):
    with open('jsFiles/'+nameFile+'.js', 'a', ) as target:
        target.write(jsVar)


if __name__ == '__main__':
    #openFile('acatic_feb2018.kml')
    data = openFile('municipios_jalisco_feb2018.kml')
    list_data = getTowns(data)
    getDataForTowns(list_data)
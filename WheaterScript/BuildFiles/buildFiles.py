import subprocess
from pathlib import Path
import time
import json
import dates as dt

MUNICIPIOS = ['ACATIC',
'AMACUECA',
'EL ARENAL',
'ATEMAJAC DE BRIZUELA',
'ATENGO',
'AYOTLAN',
'AYUTLA',
'BOLANOS',
'CASIMIRO CASTILLO',
'COCULA',
'CUAUTLA',
'CHIMALTITAN',
'CHIQUILISTLAN',
'ENCARNACION DE DIAZ',
'EL GRULLO',
'IXTLAHUACAN DEL RIO',
'JUANACATLAN',
'EL LIMON',
'SANTA MARIA DEL ORO',
'EL SALTO',
'SAN JUAN DE LOS LAGOS',
'SAN JULIAN',
'SAN MARCOS',
'SAN MARTIN DE BOLANOS',
'SAN MIGUEL EL ALTO',
'GOMEZ FARIAS',
'SAN SEBASTIAN DEL OESTE',
'SANTA MARIA DE LOS ANGELES',
'TECALITLAN',
'TENAMAXLAN',
'TLAJOMULCO DE ZUNIGA',
'TLAQUEPAQUE',
'TONAYA',
'VALLE DE GUADALUPE',
'SAN GABRIEL',
'VILLA CORONA',
'VILLA HIDALGO',
'CANADAS DE OBREGON',
'ZAPOTILTIC',
'ZAPOTITLAN DE VADILLO',
'ZAPOTLAN DEL REY',
'SAN IGNACIO CERRO GORDO']

"""
Fueron eliminados: BOLAÑOS, TLAJOMULCO DE ZUÑIGA, TLAQUEPAQUE y CAÑADAS DE OBREGON
"""
MUNICIPIOS_DICT = {'ACATIC': {'lat': '20.780°', 'lon': '-102.910°'},
'AMACUECA': {'lat': '20.008°', 'lon': '-103.597°'},
'EL ARENAL': {'lat': '20.769°', 'lon': '-103.695°'},
'ATEMAJAC DE BRIZUELA': {'lat': '20.139°', 'lon': '-103.726°'},
'ATENGO': {'lat': '20.274°', 'lon': '-104.235°'},
'AYOTLAN': {'lat': '20.533°', 'lon': '-102.332°'},
'AYUTLA': {'lat': '20.040°', 'lon': '-104.432°'},
'CASIMIRO CASTILLO': {'lat': '19.341°', 'lon': '-104.287°'},
'COCULA': {'lat': '20.363°', 'lon': '-103.826°'},
'CUAUTLA': {'lat': '20.202°', 'lon': '-104.408°'},
'CHIMALTITAN': {'lat': '21.899°', 'lon': '-103.467°'},
'CHIQUILISTLAN': {'lat': '20.089°', 'lon': '-103.861°'},
'ENCARNACION DE DIAZ': {'lat': '21.567°', 'lon': '-102.204°'},
'EL GRULLO': {'lat': '19.807°', 'lon': '-104.216°'},
'IXTLAHUACAN DEL RIO': {'lat': '20.904°', 'lon': '-103.219°'},
'JUANACATLAN': {'lat': '20.507°', 'lon': '-103.167°'},
'EL LIMON': {'lat': '19.749°', 'lon': '-104.016°'},
'SANTA MARIA DEL ORO': {'lat': '19.525°', 'lon': '-102.815°'},
'EL SALTO': {'lat': '20.519°', 'lon': '-103.189°'},
'SAN JUAN DE LOS LAGOS': {'lat': '21.250°', 'lon': '-102.329°'},
'SAN JULIAN': {'lat': '21.005°', 'lon': '-102.178°'},
'SAN MARCOS': {'lat': '20.791°', 'lon': '-104.198°'},
'SAN MARTIN DE BOLAÑOS': {'lat': '21.499°', 'lon': '-103.800°'},
'SAN MIGUEL EL ALTO': {'lat': '21.035°', 'lon': '-102.402°'},
'GOMEZ FARIAS': {'lat': '19.780°', 'lon': '-103.491°'},
'SAN SEBASTIAN DEL OESTE': {'lat': '20.762°', 'lon': '-104.854°'},
'SANTA MARIA DE LOS ANGELES': {'lat': '22.175°', 'lon': '-103.226°'},
'TECALITLAN': {'lat': '19.469°', 'lon': '-103.307°'},
'TENAMAXTLAN': {'lat': '20.213°', 'lon': '-104.163°'},
'TONAYA': {'lat': '19.787°', 'lon': '-103.970°'},
'VALLE DE GUADALUPE': {'lat': '21.011°', 'lon': '-102.620°'},
'SAN GABRIEL': {'lat': '19.744°', 'lon': '-103.765°'},
'VILLA CORONA': {'lat': '20.418°', 'lon': '-103.667°'},
'VILLA HIDALGO': {'lat': '21.675°', 'lon': '-102.587°'},
'ZAPOTILTIC': {'lat': '19.629°', 'lon': '-103.427°'},
'ZAPOTITLAN DE VADILLO': {'lat': '19.547°', 'lon': '-103.810°'},
'ZAPOTLAN DEL REY': {'lat': '20.465°', 'lon': '-102.924°'},
'SAN IGNACIO CERRO GORDO' : {'lat': '20.768°', 'lon': '-102.511°'}}

ROOT_PATH = '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/'

FINAL_LINE_HEADER = 'FECHA'

def get_header_data(dict_data):
        header = []
        with open('header_esqueleto.txt', 'r', encoding = "utf-8") as file:
            for line in file:        
                new_line = check_line_header(line, dict_data)
                header.append(new_line)
                if FINAL_LINE_HEADER in line:
                    break
        return header

def check_line_header(line, dict_data):
    parts = line.split('\n')

    if 'ESTACIÓN' in parts[0]:
        parts[0] += ' ' + str(dict_data['estacion']) + '\n'
    elif 'NOMBRE' in parts[0] or 'MUNICIPIO' in parts[0]:
        parts[0] += ' ' + dict_data['nombre'] + '\n'
    elif 'LATITUD' in parts[0]:
        parts[0] += ' ' + dict_data['lat'] + '\n'
    elif 'LONGITUD' in parts[0]:
        parts[0] += ' ' + dict_data['lon'] + '\n'
    else:
        parts[0] += '\n'
    return parts[0]

def write_file(path_file,info):
    with open(path_file,'a+', encoding = "utf-8") as file:
        file.write(info)

def newFile(content,key,dict_town,num_station):

    print(dict_town)
    path_file = build_path(key,num_station)
    header = get_header_data({'estacion':num_station,\
                                'nombre':key,\
                                'lat': dict_town['lat'],\
                                'lon': dict_town['lon']})
    
    #Writing header info
    for line in header:
        write_file(path_file,line)

    #Writing all wheater data
    for line_list in content:
        str_line = '    '.join(line_list)
        write_file(path_file,str_line + '\n')
    
    write_file(path_file,'--------------------------------------' + '\n')
    
def generate_content():
    dates_list = dt.generate_date_list('01/01/2008','31/12/2018')
    content = []
    for date in dates_list:
        line = [date,'Nulo','Nulo','Nulo','Nulo']
        content.append(line)
    return content


def build_path(name_file,num_station):
	final_path = ROOT_PATH + str(num_station) + '-' + name_file + '.txt'
	#print(final_path)
	return final_path

if __name__ == '__main__':

    STATION_COUNTER = 15001
    content = generate_content()
    for town in MUNICIPIOS_DICT:
        print(f'Building file for {town} with {MUNICIPIOS_DICT[town]}')
        newFile(content,town,MUNICIPIOS_DICT[town],STATION_COUNTER)
        STATION_COUNTER += 1
        #time.sleep(3)
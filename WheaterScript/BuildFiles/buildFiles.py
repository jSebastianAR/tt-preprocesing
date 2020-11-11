import subprocess
from pathlib import Path
import time
import json

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
'ETZATLAN',
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

MUNICIPIOS = {'ACATIC': {'lat': '20.780°', 'lon': '-102.91°'},
'AMACUECA': {'lat': '20.008°', 'lon': '-103.597°'},
'EL ARENAL': {'lat': '20.769°', 'lon': '-103.695°'},
'ATEMAJAC DE BRIZUELA': {'lat': '20.139°', 'lon': '-103.726°'},
'ATENGO': {'lat': '20.274°', 'lon': '-104.235°'},
'AYOTLAN': {'lat': '20.533°', 'lon': '-102.332°'},
'AYUTLA': {'lat': '20.040°', 'lon': '-104.432°'},
'BOLANOS': {'lat': '21.832°', 'lon': '-103.780°'},
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
'SAN MARTIN DE BOLANOS': {'lat': '21.499°', 'lon': '-103.800°'},
'SAN MIGUEL EL ALTO': {'lat': '21.035°', 'lon': '-102.402°'},
'GOMEZ FARIAS': {'lat': '19.780°', 'lon': '-103.491°'},
'SAN SEBASTIAN DEL OESTE': {'lat': '20.762°', 'lon': '-104.854°'},
'SANTA MARIA DE LOS ANGELES': {'lat': '22.175°', 'lon': '-103.226°'},
'TECALITLAN': {'lat': '19.469°', 'lon': '-103.307°'},
'TENAMAXTLAN': {'lat': '20.213°', 'lon': '-104.163°'},
'TLAJOMULCO DE ZUNIGA': {'lat': '20.462°', 'lon': '-103.435°'},
'TLAQUEPAQUE': {'lat': '20.596°', 'lon': '-103.338°'},
'TONAYA': {'lat': '19.787°', 'lon': '-103.970°'},
'VALLE DE GUADALUPE': {'lat': '21.011°', 'lon': '-102.620°'},
'SAN GABRIEL': {'lat': '19.744°', 'lon': '-103.765°'},
'VILLA CORONA': {'lat': '20.418°', 'lon': '-103.667°'},
'VILLA HIDALGO': {'lat': '21.675°', 'lon': '-102.587°'},
'CANADAS DE OBREGON': {'lat': '21.148°', 'lon': '-102.687°'},
'ZAPOTILTIC': {'lat': '19.629°', 'lon': '-103.427°'},
'ZAPOTITLAN DE VADILLO': {'lat': '19.547°', 'lon': '-103.810°'},
'ZAPOTLAN DEL REY': {'lat': '20.465°', 'lon': '-102.924°'},
'SAN IGNACIO CERRO GORDO' : {'lat': '20.768°', 'lon': '-102.511°'}}

FINAL_LINE_HEADER = 'FECHA'
INIT_COUNTER = 15000

def get_header_data(self):
        
        with open(self.path_origin_file, 'r', encoding = "ISO-8859-1") as file:
            #print(file)
            for line in file:
                self.header.append(line)
                #print(line)
                if FINAL_LINE_HEADER in line:
                    break

def write_file(self,info):
    with open(self.path_file,'a+', encoding = "ISO-8859-1") as file:
        file.write(info)

def build_path(name_file):
	root = Path('').resolve().as_posix()
	final_path = root + '/' + name_file
	print(final_path)
	return final_path
import subprocess
from pathlib import Path
import time
import json

DICT_LIST = {}

STATIC_DICT = {1: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14002-ACATLAN DE JUAREZ.txt', 2: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14006-TEOCALTICHE.txt', 3: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14009-AMECA.txt', 4: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14011-LA HUERTA.txt', 5: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14016-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 6: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14017-ATOTONILCO EL ALTO.txt', 7: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14018-ATOYAC.txt', 8: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14023-BOLAÑOS.txt', 9: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14024-TOMATLAN.txt', 10: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14025-TEOCALTICHE.txt',\
11: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14026-COLOTLAN.txt', 12: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14028-CIHUATLAN.txt', 13: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14029-CONCEPCION DE BUENOS AIRES.txt', 14: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14030-ZAPOTLAN EL GRANDE.txt', 15: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14032-COLOTLAN.txt', 16: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14033-LAGOS DE MORENO.txt', 17: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14034-TAMAZULA DE GORDIANO.txt', 18: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14035-MASCOTA.txt', 19: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14036-CUAUTITLAN DE GARCIA BARRAGAN.txt', 20: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14037-HUEJUCAR.txt',\
21: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14038-SAN CRISTOBAL DE LA BARRANCA.txt', 22: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14039-CUQUIO.txt', 23: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14040-CHAPALA.txt', 24: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14044-TALPA DE ALLENDE.txt', 25: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14046-AUTLAN DE NAVARRO.txt', 26: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14047-OCOTLAN.txt', 27: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14048-CIHUATLAN.txt', 28: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14052-TAPALPA.txt', 29: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14053-HUEJUQUILLA EL ALTO.txt', 30: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14054-LAGOS DE MORENO.txt',\
31: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14056-SAN MARTIN HIDALGO.txt', 32: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14059-CABO CORRIENTES.txt', 33: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14060-ARANDAS.txt', 34: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14063-ETZATLAN.txt', 35: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14065-GUADALAJARA.txt', 36: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14066-GUADALAJARA.txt', 37: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14067-TOMATLAN.txt', 38: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14068-HOSTOTIPAQUILLO.txt', 39: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14069-HUEJUCAR.txt', 40: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14070-DEGOLLADO.txt',\
41: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14071-HUEJUQUILLA EL ALTO.txt', 42: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14072-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 43: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14075-JAMAY.txt', 44: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14076-JESUS MARIA.txt', 45: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14078-JUCHITLAN.txt', 46: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14080-YAHUALICA DE GONZALEZ GALLO.txt', 47: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14081-PUERTO VALLARTA.txt', 48: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14083-LAGOS DE MORENO.txt', 49: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14084-LAGOS DE MORENO.txt', 50: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14085-LA HUERTA.txt',\
51: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14086-LA MANZANILLA DE LA PAZ.txt', 52: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14087-TEPATITLAN DE MORELOS.txt', 53: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14089-TEUCHITLAN.txt', 54: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14090-TOTOTLAN.txt', 55: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14093-MAGDALENA.txt', 56: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14096-MASCOTA.txt', 57: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14099-MAZAMITLA.txt', 58: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14100-MEXTICACAN.txt', 59: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14101-TEOCALTICHE.txt', 60: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14104-ZAPOTLANEJO.txt',\
61: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14112-PIHUAMO.txt', 62: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14113-ACATLAN DE JUAREZ.txt', 63: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14114-LAGOS DE MORENO.txt', 64: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14117-VILLA PURIFICACION.txt', 65: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14118-TUXPAN.txt', 66: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14119-QUITUPAN.txt', 67: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14122-TEOCALTICHE.txt', 68: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14123-SAN DIEGO DE ALEJANDRIA.txt', 69: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14125-MIXTLAN.txt', 70: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14129-TONILA.txt',\
71: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14132-SAN PEDRO TLAQUEPAQUE.txt', 72: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14136-AMATITAN.txt', 73: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14139-UNION DE TULA.txt', 74: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14140-TALPA DE ALLENDE.txt', 75: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14141-TAMAZULA DE GORDIANO.txt', 76: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14142-TAPALPA.txt', 77: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14143-TECOLOTLAN.txt', 78: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14144-COLOTLAN.txt', 79: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14145-TEOCALTICHE.txt', 80: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14146-TEOCUITATLAN DE CORONA.txt',\
81: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14155-TUXCACUESCO.txt', 82: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14156-TUXCUECA.txt', 83: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14157-UNION DE SAN ANTONIO.txt', 84: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14160-VALLE DE JUAREZ.txt', 85: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14164-VILLA GUERRERO.txt', 86: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14165-CAÑADAS DE OBREGON.txt', 87: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14167-YAHUALICA DE GONZALEZ GALLO.txt', 88: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14168-ZACOALCO DE TORRES.txt', 89: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14169-ZAPOPAN.txt', 90: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14179-OJUELOS DE JALISCO.txt',\
91: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14180-QUITUPAN.txt', 92: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14187-TEQUILA.txt', 93: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14189-TIZAPAN EL ALTO.txt', 94: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14191-VALLE DE JUAREZ.txt', 95: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14195-SAN JUANITO DE ESCOBEDO.txt', 96: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14197-UNION DE TULA.txt', 97: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14198-CUAUTITLAN DE GARCIA BARRAGAN.txt', 98: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14199-PONCITLAN.txt', 99: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14200-SAN PEDRO TLAQUEPAQUE.txt', 100: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14266-JALOSTOTITLAN.txt',\
101: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14269-AHUALULCO DE MERCADO.txt', 102: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14294-TLAJOMULCO DE ZUÑIGA.txt', 103: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14297-GUACHINANGO.txt', 104: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14306-HUEJUQUILLA EL ALTO.txt', 105: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14311-TOLIMAN.txt', 106: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14317-MIXTLAN.txt', 107: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14320-LAGOS DE MORENO.txt', 108: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14323-TECHALUTA DE MONTENEGRO.txt', 109: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14324-TOTATICHE.txt', 110: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14326-MEZQUITIC.txt',\
111: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14329-GUADALAJARA.txt', 112: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14331-COLOTLAN.txt', 113: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14336-PIHUAMO.txt', 114: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14337-YAHUALICA DE GONZALEZ GALLO.txt', 115: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14339-PUERTO VALLARTA.txt', 116: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14343-EJUTLA.txt', 117: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14346-MEZQUITIC.txt', 118: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14348-JILOTLAN DE LOS DOLORES.txt', 119: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14349-ATENGUILLO.txt', 120: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14350-TUXCACUESCO.txt',\
121: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14351-TALA.txt', 122: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14355-LA BARCA.txt', 123: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14367-UNION DE SAN ANTONIO.txt', 124: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14368-SAYULA.txt', 125: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14369-ARANDAS.txt', 126: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14379-PONCITLAN.txt', 127: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14386-TONALA.txt', 128: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14388-ZAPOTLANEJO.txt', 129: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14390-AUTLAN DE NAVARRO.txt', 130: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14391-TIZAPAN EL ALTO.txt',\
131: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14392-LAGOS DE MORENO.txt', 132: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14395-UNION DE TULA.txt', 133: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14396-JOCOTEPEC.txt', 134: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14397-ZAPOTLANEJO.txt'}

d = {1: '14002-ACATLAN DE JUAREZ.txt', 2: '14006-TEOCALTICHE.txt', 3: '14009-AMECA.txt', 4: '14011-LA HUERTA.txt', 5: '14016-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 6: '14017-ATOTONILCO EL ALTO.txt', 7: '14018-ATOYAC.txt', 8: '14023-BOLAÑOS.txt', 9: '14024-TOMATLAN.txt', 10: '14025-TEOCALTICHE.txt',\
	11: '14026-COLOTLAN.txt', 12: '14028-CIHUATLAN.txt', 13: '14029-CONCEPCION DE BUENOS AIRES.txt', 14: '14030-ZAPOTLAN EL GRANDE.txt', 15: '14032-COLOTLAN.txt', 16: '14033-LAGOS DE MORENO.txt', 17: '14034-TAMAZULA DE GORDIANO.txt', 18: '14035-MASCOTA.txt', 19: '14036-CUAUTITLAN DE GARCIA BARRAGAN.txt', 20: '14037-HUEJUCAR.txt',\ 
	21: '14038-SAN CRISTOBAL DE LA BARRANCA.txt', 22: '14039-CUQUIO.txt', 23: '14040-CHAPALA.txt', 24: '14044-TALPA DE ALLENDE.txt', 25: '14046-AUTLAN DE NAVARRO.txt', 26: '14047-OCOTLAN.txt', 27: '14048-CIHUATLAN.txt', 28: '14052-TAPALPA.txt', 29: '14053-HUEJUQUILLA EL ALTO.txt', 30: '14054-LAGOS DE MORENO.txt',\
	31: '14056-SAN MARTIN HIDALGO.txt', 32: '14059-CABO CORRIENTES.txt', 33: '14060-ARANDAS.txt', 34: '14063-ETZATLAN.txt', 35: '14065-GUADALAJARA.txt', 36: '14066-GUADALAJARA.txt', 37: '14067-TOMATLAN.txt', 38: '14068-HOSTOTIPAQUILLO.txt', 39: '14069-HUEJUCAR.txt', 40: '14070-DEGOLLADO.txt',\
	41: '14071-HUEJUQUILLA EL ALTO.txt', 42: '14072-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 43: '14075-JAMAY.txt', 44: '14076-JESUS MARIA.txt', 45: '14078-JUCHITLAN.txt', 46: '14080-YAHUALICA DE GONZALEZ GALLO.txt', 47: '14081-PUERTO VALLARTA.txt', 48: '14083-LAGOS DE MORENO.txt', 49: '14084-LAGOS DE MORENO.txt', 50: '14085-LA HUERTA.txt',\
	51: '14086-LA MANZANILLA DE LA PAZ.txt', 52: '14087-TEPATITLAN DE MORELOS.txt', 53: '14089-TEUCHITLAN.txt', 54: '14090-TOTOTLAN.txt', 55: '14093-MAGDALENA.txt', 56: '14096-MASCOTA.txt', 57: '14099-MAZAMITLA.txt', 58: '14100-MEXTICACAN.txt', 59: '14101-TEOCALTICHE.txt', 60: '14104-ZAPOTLANEJO.txt',\
	61: '14112-PIHUAMO.txt', 62: '14113-ACATLAN DE JUAREZ.txt', 63: '14114-LAGOS DE MORENO.txt', 64: '14117-VILLA PURIFICACION.txt', 65: '14118-TUXPAN.txt', 66: '14119-QUITUPAN.txt', 67: '14122-TEOCALTICHE.txt', 68: '14123-SAN DIEGO DE ALEJANDRIA.txt', 69: '14125-MIXTLAN.txt', 70: '14129-TONILA.txt',\
	71: '14132-SAN PEDRO TLAQUEPAQUE.txt', 72: '14136-AMATITAN.txt', 73: '14139-UNION DE TULA.txt', 74: '14140-TALPA DE ALLENDE.txt', 75: '14141-TAMAZULA DE GORDIANO.txt', 76: '14142-TAPALPA.txt', 77: '14143-TECOLOTLAN.txt', 78: '14144-COLOTLAN.txt', 79: '14145-TEOCALTICHE.txt', 80: '14146-TEOCUITATLAN DE CORONA.txt',\
	81: '14155-TUXCACUESCO.txt', 82: '14156-TUXCUECA.txt', 83: '14157-UNION DE SAN ANTONIO.txt', 84: '14160-VALLE DE JUAREZ.txt', 85: '14164-VILLA GUERRERO.txt', 86: '14165-CAÑADAS DE OBREGON.txt', 87: '14167-YAHUALICA DE GONZALEZ GALLO.txt', 88: '14168-ZACOALCO DE TORRES.txt', 89: '14169-ZAPOPAN.txt', 90: '14179-OJUELOS DE JALISCO.txt',\
	91: '14180-QUITUPAN.txt', 92: '14187-TEQUILA.txt', 93: '14189-TIZAPAN EL ALTO.txt', 94: '14191-VALLE DE JUAREZ.txt', 95: '14195-SAN JUANITO DE ESCOBEDO.txt', 96: '14197-UNION DE TULA.txt', 97: '14198-CUAUTITLAN DE GARCIA BARRAGAN.txt', 98: '14199-PONCITLAN.txt', 99: '14200-SAN PEDRO TLAQUEPAQUE.txt', 100: '14266-JALOSTOTITLAN.txt',\
	101: '14269-AHUALULCO DE MERCADO.txt', 102: '14294-TLAJOMULCO DE ZUÑIGA.txt', 103: '14297-GUACHINANGO.txt', 104: '14306-HUEJUQUILLA EL ALTO.txt', 105: '14311-TOLIMAN.txt', 106: '14317-MIXTLAN.txt', 107: '14320-LAGOS DE MORENO.txt', 108: '14323-TECHALUTA DE MONTENEGRO.txt', 109: '14324-TOTATICHE.txt', 110: '14326-MEZQUITIC.txt', \
	111: '14329-GUADALAJARA.txt', 112: '14331-COLOTLAN.txt', 113: '14336-PIHUAMO.txt', 114: '14337-YAHUALICA DE GONZALEZ GALLO.txt', 115: '14339-PUERTO VALLARTA.txt', 116: '14343-EJUTLA.txt', 117: '14346-MEZQUITIC.txt', 118: '14348-JILOTLAN DE LOS DOLORES.txt', 119: '14349-ATENGUILLO.txt', 120: '14350-TUXCACUESCO.txt',\
	121: '14351-TALA.txt', 122: '14355-LA BARCA.txt', 123: '14367-UNION DE SAN ANTONIO.txt', 124: '14368-SAYULA.txt', 125: '14369-ARANDAS.txt', 126: '14379-PONCITLAN.txt', 127: '14386-TONALA.txt', 128: '14388-ZAPOTLANEJO.txt', 129: '14390-AUTLAN DE NAVARRO.txt', 130: '14391-TIZAPAN EL ALTO.txt',\
	131: '14392-LAGOS DE MORENO.txt', 132: '14395-UNION DE TULA.txt', 133: '14396-JOCOTEPEC.txt', 134: '14397-ZAPOTLANEJO.txt', 135: '15001-ACATIC.txt', 136: '15002-AMACUECA.txt', 137: '15003-EL ARENAL.txt', 138: '15004-ATEMAJAC DE BRIZUELA.txt', 139: '15005-ATENGO.txt', 140: '15006-AYOTLAN.txt',\
	141: '15007-AYUTLA.txt', 142: '15008-CASIMIRO CASTILLO.txt', 143: '15009-COCULA.txt', 144: '15010-CUAUTLA.txt', 145: '15011-CHIMALTITAN.txt', 146: '15012-CHIQUILISTLAN.txt', 147: '15013-ENCARNACION DE DIAZ.txt', 148: '15014-EL GRULLO.txt', 149: '15015-IXTLAHUACAN DEL RIO.txt', 150: '15016-JUANACATLAN.txt',\
	151: '15017-EL LIMON.txt', 152: '15018-SANTA MARIA DEL ORO.txt', 153: '15019-EL SALTO.txt', 154: '15020-SAN JUAN DE LOS LAGOS.txt', 155: '15021-SAN JULIAN.txt', 156: '15022-SAN MARCOS.txt', 157: '15023-SAN MARTIN DE BOLAÑOS.txt', 158: '15024-SAN MIGUEL EL ALTO.txt', 159: '15025-GOMEZ FARIAS.txt', 160: '15026-SAN SEBASTIAN DEL OESTE.txt',\
	161: '15027-SANTA MARIA DE LOS ANGELES.txt', 162: '15028-TECALITLAN.txt', 163: '15029-TENAMAXTLAN.txt', 164: '15030-TONAYA.txt', 165: '15031-VALLE DE GUADALUPE.txt', 166: '15032-SAN GABRIEL.txt', 167: '15033-VILLA CORONA.txt', 168: '15034-VILLA HIDALGO.txt', 169: '15035-ZAPOTILTIC.txt', 170: '15036-ZAPOTITLAN DE VADILLO.txt',\
	171: '15037-ZAPOTLAN DEL REY.txt', 172: '15038-SAN IGNACIO CERRO GORDO.txt'}

DICT_REL_DATA = {1: [62,121,102,133,88,None], 2: [10,59,67,None,None,None,100,58,79], 3: [34,101,53,31,77,69,106,103], 4: [50,9,37,64,None,19,97,12,27], 5: [42,None,23,133,102], 6: [52,33,125], 7: [108,88,80,13,None,124,None], 8: [110,117,85,None,None], 9: [37,24,74,None,None,64,4,50], 10: [2,59,67,None,None,None,100,58,79],\
11: [15,78,112,109], 12: [27,4,50,19,97], 13: [80,82,51,57,17,75,None,7], 14: [None,None,17,75,None,65,70,None,None], 15: [11,78,112,109], 16: [30,48,49,63,107,131,90,None,None,83,123], 17: [75,13,57,84,94,None,118,None,None,14,None], 18: [56,None,103,69,106,119,24,74,115], 19: [97,None,25,129,81,120,105,12,27,4,50], 20: [39,None],\
21: [92,89,None], 22: [46,87,114,60,128,134,None,52,None], 23: [5,42,None,98,126,93,130,82,133], 24: [74,47,115,18,56,119,None,9,37,32], 25: [129,None,73,96,132,81,120,19,97,None,64], 26: [None,54,6,122,43,98,126,23], 27: [12,4,50,19,97], 28: [76,None,None,108,None,124,None,None], 29: [41,104], 30: [16,48,49,63,107,131,90,None,None,83,123],\
31: [53,3,77,None], 32: [47,115,24,74,9,37], 33: [125,None,None,68,None,52,6,None,44], 34: [55,3,95,101,None], 35: [36,111,None,127,60,128,134,71,99,89], 36: [35,111,None,127,60,128,134,71,99,89], 37: [9,24,74,None,None,64,4,50], 38: [92,55], 39: [20,None], 40: [None,44],\
41: [29,104], 42: [5,None,23,133,102], 43: [26,98,126,122], 44: [33,125,40,None], 45: [77,None,116,None], 46: [87,114,58,86,None,52,22], 47: [115], 48: [30,16,49,63,107,131,90,None,None,83,123], 49: [30,16,48,63,107,131,90,None,None,83,123], 50: [4,9,37,64,None,19,97,12,27],\
51: [82,93,130,57,13], 52: [None,46,87,114,54,6,None,60,128,134,22,None,None], 53: [101,72,None,121,31,3], 54: [52,6,26,None,60,128,134], 55: [38,None,34,95,92], 56: [18,None,103,69,106,119,24,74,115], 57: [51,84,94,17,75,13], 58: [2,10,59,67,100,86,46,87,114], 59: [2,10,67,None,None,None,100,58,79], 60: [128,134,None,22,None,52,54,None,None,127,35,36,111],\
61: [113,65,None], 62: [1,121,102,133,88,None], 63: [30,16,48,49,107,131,90,None,None,83,123], 64: [9,37,None,25,129,None,4,50], 65: [None,14,61,113,None,70], 66: [91,84,94,None], 67: [2,10,59,None,None,None,100,58,79], 68: [83,123,33,125], 69: [106,18,56,103,3,77,119,None], 70: [None,14,65],\
71: [99,127,89,35,36,111,102,None], 72: [92,89,None,53,101], 73: [96,132,None,None,116,None,25,129], 74: [24,47,115,18,56,119,None,9,37,32], 75: [17,13,57,84,94,None,118,None,None,14,None], 76: [28,None,None,108,None,124,None,None], 77: [None,3,31,None,None,None,45,None], 78: [11,15,112,109], 79: [2,10,59,None,None,None,100,58,67], 80: [88,133,82,13,7],\
81: [120,None,None,None,None,105,19,97,25,129], 82: [23,51,13,93,130,80,133], 83: [123,16,30,48,49,63,107,131,68,None], 84: [94,66,91,None,57,17,75], 85: [110,117,109,None,8], 86: [46,87,114,58,100,None], 87: [46,114,58,86,None,52,22], 88: [108,133,1,62,7,80,None], 89: [102,21,35,36,111,71,99,72,None,121,None,92], 90: [16,30,48,49,63,107,131],\
91: [66,84,94,None], 92: [95,21,38,55,72,89], 93: [130,23,51,82,98,126], 94: [84,66,91,None,57,17,75], 95: [55,92,101,34], 96: [73,132,None,None,116,None,25,129], 97: [19,None,25,129,81,120,105,12,27,4,50], 98: [126,None,None,26,43,23], 99: [71,127,89,35,36,111,102,None], 100: [2,10,59,67,79,58,86],\
101: [3,34,53,72,95], 102: [89,71,99,None,None,5,42,133,1,62,121], 103: [3,18,56,69,106], 104: [29,41], 105: [19,97,81,120], 106: [69,18,56,103,3,77,119,None], 107: [30,16,48,49,63,131,90,None,None,83,123], 108: [None,88,7,None,28,76], 109: [11,15,78,112,85], 110: [117,8,85,29,41,104],\
111: [35,36,None,127,60,128,134,71,99,89], 112: [11,15,78,109], 113: [61,65,None], 114: [46,87,58,86,None,52,22], 115: [47], 116: [73,96,132,45,None,None,None,None,None], 117: [110,8,85,29,41,104], 118: [None,17,75,None], 119: [18,56,69,None,None,24,74], 120: [81,None,None,None,None,105,19,97,25,129],\
121: [13,57,66,91,None,None,118,None,84,94,14,None], 122: [26,6,None,43], 123: [83,16,30,48,49,63,107,131,68,None], 124: [None,7,None,None,28,76], 125: [33,None,None,68,None,52,6,None,44], 126: [98,None,None,26,43,23], 127: [60,128,134,None,None,71,99,35,36,111], 128: [60,134,None,22,None,52,54,None,None,127,35,36,111], 129: [25,None,73,96,132,81,120,19,97,None,64], 130: [93,23,51,82,98,126],\
131: [30,16,48,49,63,107,90,None,None,83,123], 132: [73,96,None,None,116,None,25,129], 133: [102,5,42,23,82,80,88,1,62], 134: [60,128,None,22,None,52,54,None,None,127,35,36,111], 135: [22,52,60,128,134], 136: [28,76,108,7,124], 137: [72,121,89], 138: [143,167,88,108,28,76,146,77], 139: [69,106,77,163,141,144,119], 140: [122,6,33,125,44,40],\
141: [45,145,139,163,73,96,132,25,129,64,9,37], 142: [64,25,129,19,97,4,50], 143: [62,31,167,138,77], 144: [73,45,119,139,141,9,37,24,74], 145: [11,8,85,109,157], 146: [77,138,28,76,164,116,45], 147: [16,30,48,49,63,107,131,154,2,10,59,67,79], 148: [73,96,132,116,25,129,151,81,120], 149: [35,36,111,60,128,134,22,21,89], 150: [127,60,128,134,23,98,126,171,5,42,153,102],\
151: [25,129,116,81,120,164,148], 152: [17,75,84,94,66,91,118], 153: [5,42,127,71,99,102,150], 154: [2,10,59,67,79,147,100,158,155,83,123], 155: [33,125,83,123,154,158,68], 156: [95,34,3,8], 157: [8,145,92,38], 158: [86,100,154,33,125,155,52,165], 159: [7,14,17,75,13,124], 160: [69,106,18,56,103,47,115],\
161: [11,15,78,112,20,39], 162: [65,169,17,75,118,61,113], 163: [139,73,96,132,77,45,141], 164: [146,81,120,28,76,166,116,151], 165: [86,100,52,158,46,87,114], 166: [28,76,124,105,170,14,159,164,81,120], 167: [121,31,138,88,1,62,143], 168: [2,10,59,67,79], 169: [65,14,17,75,162], 170: [166,105,70,14],\
171: [60,128,134,54,98,126,26,150], 172: [6,33,125,52]}

def get_txt():
	result = subprocess.check_output('ls CleanedData/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def build_path(name_file):
	root = Path('').resolve().as_posix()
	final_path = root + '/' + name_file
	print(final_path)
	return final_path

def get_name_txt(txt):
	parts = txt.split('/')
	name = parts[len(parts)-1]
	return name

def dump_file(data,name):
	a_file = open(name, "w")
	json.dump(data, a_file)
	a_file.close()

def get_dump(name):
	a_file = open("data.json", "r")
	output = a_file.read()
	print(output)

if __name__ == '__main__':
	
	text_files = get_txt()
	index = 1
	for text_file in text_files:
		#str_index = str(index)
		#DICT_LIST[index] = build_path(text_file)
		DICT_LIST[index] = get_name_txt(text_file)
		DICT_REL_DATA[index] = [] 
		index += 1
	print(f'len: {len(DICT_LIST)} list: {DICT_LIST}')
	print(DICT_REL_DATA)
	

	#dump_file(STATIC_DICT,'paths_file.json')
	#dump_file(DICT_REL_DATA,'rel_TF_TU.json')

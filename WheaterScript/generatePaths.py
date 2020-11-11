import subprocess
from pathlib import Path
import time

DICT_LIST = {}

STATIC_DICT = {1: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14002-ACATLAN DE JUAREZ.txt', 2: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14006-TEOCALTICHE.txt', 3: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14009-AMECA.txt', 4: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14011-LA HUERTA.txt', 5: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14016-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 6: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14017-ATOTONILCO EL ALTO.txt', 7: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14018-ATOYAC.txt', 8: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14023-BOLAÑOS.txt', 9: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14024-TOMATLAN.txt', 10: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14025-TEOCALTICHE.txt', 11: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14026-COLOTLAN.txt', 12: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14028-CIHUATLAN.txt', 13: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14029-CONCEPCION DE BUENOS AIRES.txt', 14: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14030-ZAPOTLAN EL GRANDE.txt', 15: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14032-COLOTLAN.txt', 16: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14033-LAGOS DE MORENO.txt', 17: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14034-TAMAZULA DE GORDIANO.txt', 18: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14035-MASCOTA.txt', 19: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14036-CUAUTITLAN DE GARCIA BARRAGAN.txt', 20: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14037-HUEJUCAR.txt', 21: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14038-SAN CRISTOBAL DE LA BARRANCA.txt', 22: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14039-CUQUIO.txt', 23: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14040-CHAPALA.txt', 24: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14044-TALPA DE ALLENDE.txt', 25: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14046-AUTLAN DE NAVARRO.txt', 26: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14047-OCOTLAN.txt', 27: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14048-CIHUATLAN.txt', 28: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14052-TAPALPA.txt', 29: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14053-HUEJUQUILLA EL ALTO.txt', 30: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14054-LAGOS DE MORENO.txt', 31: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14056-SAN MARTIN HIDALGO.txt', 32: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14059-CABO CORRIENTES.txt', 33: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14060-ARANDAS.txt', 34: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14063-ETZATLAN.txt', 35: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14065-GUADALAJARA.txt', 36: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14066-GUADALAJARA.txt', 37: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14067-TOMATLAN.txt', 38: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14068-HOSTOTIPAQUILLO.txt', 39: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14069-HUEJUCAR.txt', 40: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14070-DEGOLLADO.txt', 41: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14071-HUEJUQUILLA EL ALTO.txt', 42: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14072-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 43: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14075-JAMAY.txt', 44: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14076-JESUS MARIA.txt', 45: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14078-JUCHITLAN.txt', 46: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14080-YAHUALICA DE GONZALEZ GALLO.txt', 47: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14081-PUERTO VALLARTA.txt', 48: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14083-LAGOS DE MORENO.txt', 49: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14084-LAGOS DE MORENO.txt', 50: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14085-LA HUERTA.txt', 51: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14086-LA MANZANILLA DE LA PAZ.txt', 52: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14087-TEPATITLAN DE MORELOS.txt', 53: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14089-TEUCHITLAN.txt', 54: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14090-TOTOTLAN.txt', 55: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14093-MAGDALENA.txt', 56: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14096-MASCOTA.txt', 57: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14099-MAZAMITLA.txt', 58: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14100-MEXTICACAN.txt', 59: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14101-TEOCALTICHE.txt', 60: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14104-ZAPOTLANEJO.txt', 61: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14112-PIHUAMO.txt', 62: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14113-ACATLAN DE JUAREZ.txt', 63: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14114-LAGOS DE MORENO.txt', 64: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14117-VILLA PURIFICACION.txt', 65: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14118-TUXPAN.txt', 66: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14119-QUITUPAN.txt', 67: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14122-TEOCALTICHE.txt', 68: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14123-SAN DIEGO DE ALEJANDRIA.txt', 69: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14125-MIXTLAN.txt', 70: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14129-TONILA.txt', 71: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14132-SAN PEDRO TLAQUEPAQUE.txt', 72: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14136-AMATITAN.txt', 73: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14139-UNION DE TULA.txt', 74: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14140-TALPA DE ALLENDE.txt', 75: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14141-TAMAZULA DE GORDIANO.txt', 76: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14142-TAPALPA.txt', 77: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14143-TECOLOTLAN.txt', 78: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14144-COLOTLAN.txt', 79: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14145-TEOCALTICHE.txt', 80: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14146-TEOCUITATLAN DE CORONA.txt', 81: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14155-TUXCACUESCO.txt', 82: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14156-TUXCUECA.txt', 83: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14157-UNION DE SAN ANTONIO.txt', 84: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14160-VALLE DE JUAREZ.txt', 85: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14164-VILLA GUERRERO.txt', 86: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14165-CAÑADAS DE OBREGON.txt', 87: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14167-YAHUALICA DE GONZALEZ GALLO.txt', 88: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14168-ZACOALCO DE TORRES.txt', 89: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14169-ZAPOPAN.txt', 90: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14179-OJUELOS DE JALISCO.txt', 91: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14180-QUITUPAN.txt', 92: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14187-TEQUILA.txt', 93: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14189-TIZAPAN EL ALTO.txt', 94: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14191-VALLE DE JUAREZ.txt', 95: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14195-SAN JUANITO DE ESCOBEDO.txt', 96: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14197-UNION DE TULA.txt', 97: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14198-CUAUTITLAN DE GARCIA BARRAGAN.txt', 98: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14199-PONCITLAN.txt', 99: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14200-SAN PEDRO TLAQUEPAQUE.txt', 100: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14266-JALOSTOTITLAN.txt', 101: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14269-AHUALULCO DE MERCADO.txt', 102: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14294-TLAJOMULCO DE ZUÑIGA.txt', 103: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14297-GUACHINANGO.txt', 104: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14306-HUEJUQUILLA EL ALTO.txt', 105: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14311-TOLIMAN.txt', 106: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14317-MIXTLAN.txt', 107: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14320-LAGOS DE MORENO.txt', 108: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14323-TECHALUTA DE MONTENEGRO.txt', 109: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14324-TOTATICHE.txt', 110: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14326-MEZQUITIC.txt', 111: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14329-GUADALAJARA.txt', 112: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14331-COLOTLAN.txt', 113: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14336-PIHUAMO.txt', 114: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14337-YAHUALICA DE GONZALEZ GALLO.txt', 115: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14339-PUERTO VALLARTA.txt', 116: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14343-EJUTLA.txt', 117: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14346-MEZQUITIC.txt', 118: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14348-JILOTLAN DE LOS DOLORES.txt', 119: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14349-ATENGUILLO.txt', 120: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14350-TUXCACUESCO.txt', 121: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14351-TALA.txt', 122: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14355-LA BARCA.txt', 123: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14367-UNION DE SAN ANTONIO.txt', 124: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14368-SAYULA.txt', 125: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14369-ARANDAS.txt', 126: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14379-PONCITLAN.txt', 127: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14386-TONALA.txt', 128: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14388-ZAPOTLANEJO.txt', 129: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14390-AUTLAN DE NAVARRO.txt', 130: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14391-TIZAPAN EL ALTO.txt', 131: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14392-LAGOS DE MORENO.txt', 132: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14395-UNION DE TULA.txt', 133: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14396-JOCOTEPEC.txt', 134: '/home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/CleanedData/14397-ZAPOTLANEJO.txt'}

d = {1: '14002-ACATLAN DE JUAREZ.txt', 2: '14006-TEOCALTICHE.txt', 3: '14009-AMECA.txt', 4: '14011-LA HUERTA.txt', 5: '14016-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 6: '14017-ATOTONILCO EL ALTO.txt', 7: '14018-ATOYAC.txt', 8: '14023-BOLAÑOS.txt', 9: '14024-TOMATLAN.txt', 10: '14025-TEOCALTICHE.txt', 11: '14026-COLOTLAN.txt', 12: '14028-CIHUATLAN.txt', 13: '14029-CONCEPCION DE BUENOS AIRES.txt', 14: '14030-ZAPOTLAN EL GRANDE.txt', 15: '14032-COLOTLAN.txt', 16: '14033-LAGOS DE MORENO.txt', 17: '14034-TAMAZULA DE GORDIANO.txt', 18: '14035-MASCOTA.txt', 19: '14036-CUAUTITLAN DE GARCIA BARRAGAN.txt', 20: '14037-HUEJUCAR.txt', 21: '14038-SAN CRISTOBAL DE LA BARRANCA.txt', 22: '14039-CUQUIO.txt', 23: '14040-CHAPALA.txt', 24: '14044-TALPA DE ALLENDE.txt', 25: '14046-AUTLAN DE NAVARRO.txt', 26: '14047-OCOTLAN.txt', 27: '14048-CIHUATLAN.txt', 28: '14052-TAPALPA.txt', 29: '14053-HUEJUQUILLA EL ALTO.txt', 30: '14054-LAGOS DE MORENO.txt', 31: '14056-SAN MARTIN HIDALGO.txt', 32: '14059-CABO CORRIENTES.txt', 33: '14060-ARANDAS.txt', 34: '14063-ETZATLAN.txt', 35: '14065-GUADALAJARA.txt', 36: '14066-GUADALAJARA.txt', 37: '14067-TOMATLAN.txt', 38: '14068-HOSTOTIPAQUILLO.txt', 39: '14069-HUEJUCAR.txt', 40: '14070-DEGOLLADO.txt', 41: '14071-HUEJUQUILLA EL ALTO.txt', 42: '14072-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 43: '14075-JAMAY.txt', 44: '14076-JESUS MARIA.txt', 45: '14078-JUCHITLAN.txt', 46: '14080-YAHUALICA DE GONZALEZ GALLO.txt', 47: '14081-PUERTO VALLARTA.txt', 48: '14083-LAGOS DE MORENO.txt', 49: '14084-LAGOS DE MORENO.txt', 50: '14085-LA HUERTA.txt', 51: '14086-LA MANZANILLA DE LA PAZ.txt', 52: '14087-TEPATITLAN DE MORELOS.txt', 53: '14089-TEUCHITLAN.txt', 54: '14090-TOTOTLAN.txt', 55: '14093-MAGDALENA.txt', 56: '14096-MASCOTA.txt', 57: '14099-MAZAMITLA.txt', 58: '14100-MEXTICACAN.txt', 59: '14101-TEOCALTICHE.txt', 60: '14104-ZAPOTLANEJO.txt', 61: '14112-PIHUAMO.txt', 62: '14113-ACATLAN DE JUAREZ.txt', 63: '14114-LAGOS DE MORENO.txt', 64: '14117-VILLA PURIFICACION.txt', 65: '14118-TUXPAN.txt', 66: '14119-QUITUPAN.txt', 67: '14122-TEOCALTICHE.txt', 68: '14123-SAN DIEGO DE ALEJANDRIA.txt', 69: '14125-MIXTLAN.txt', 70: '14129-TONILA.txt', 71: '14132-SAN PEDRO TLAQUEPAQUE.txt', 72: '14136-AMATITAN.txt', 73: '14139-UNION DE TULA.txt', 74: '14140-TALPA DE ALLENDE.txt', 75: '14141-TAMAZULA DE GORDIANO.txt', 76: '14142-TAPALPA.txt', 77: '14143-TECOLOTLAN.txt', 78: '14144-COLOTLAN.txt', 79: '14145-TEOCALTICHE.txt', 80: '14146-TEOCUITATLAN DE CORONA.txt', 81: '14155-TUXCACUESCO.txt', 82: '14156-TUXCUECA.txt', 83: '14157-UNION DE SAN ANTONIO.txt', 84: '14160-VALLE DE JUAREZ.txt', 85: '14164-VILLA GUERRERO.txt', 86: '14165-CAÑADAS DE OBREGON.txt', 87: '14167-YAHUALICA DE GONZALEZ GALLO.txt', 88: '14168-ZACOALCO DE TORRES.txt', 89: '14169-ZAPOPAN.txt', 90: '14179-OJUELOS DE JALISCO.txt', 91: '14180-QUITUPAN.txt', 92: '14187-TEQUILA.txt', 93: '14189-TIZAPAN EL ALTO.txt', 94: '14191-VALLE DE JUAREZ.txt', 95: '14195-SAN JUANITO DE ESCOBEDO.txt', 96: '14197-UNION DE TULA.txt', 97: '14198-CUAUTITLAN DE GARCIA BARRAGAN.txt', 98: '14199-PONCITLAN.txt', 99: '14200-SAN PEDRO TLAQUEPAQUE.txt', 100: '14266-JALOSTOTITLAN.txt', 101: '14269-AHUALULCO DE MERCADO.txt', 102: '14294-TLAJOMULCO DE ZUÑIGA.txt', 103: '14297-GUACHINANGO.txt', 104: '14306-HUEJUQUILLA EL ALTO.txt', 105: '14311-TOLIMAN.txt', 106: '14317-MIXTLAN.txt', 107: '14320-LAGOS DE MORENO.txt', 108: '14323-TECHALUTA DE MONTENEGRO.txt', 109: '14324-TOTATICHE.txt', 110: '14326-MEZQUITIC.txt', 111: '14329-GUADALAJARA.txt', 112: '14331-COLOTLAN.txt', 113: '14336-PIHUAMO.txt', 114: '14337-YAHUALICA DE GONZALEZ GALLO.txt', 115: '14339-PUERTO VALLARTA.txt', 116: '14343-EJUTLA.txt', 117: '14346-MEZQUITIC.txt', 118: '14348-JILOTLAN DE LOS DOLORES.txt', 119: '14349-ATENGUILLO.txt', 120: '14350-TUXCACUESCO.txt', 121: '14351-TALA.txt', 122: '14355-LA BARCA.txt', 123: '14367-UNION DE SAN ANTONIO.txt', 124: '14368-SAYULA.txt', 125: '14369-ARANDAS.txt', 126: '14379-PONCITLAN.txt', 127: '14386-TONALA.txt', 128: '14388-ZAPOTLANEJO.txt', 129: '14390-AUTLAN DE NAVARRO.txt', 130: '14391-TIZAPAN EL ALTO.txt', 131: '14392-LAGOS DE MORENO.txt', 132: '14395-UNION DE TULA.txt', 133: '14396-JOCOTEPEC.txt', 134: '14397-ZAPOTLANEJO.txt'}

DICT_REL_DATA = {1: [62,121,102,133,88,None], 2: [10,59,67,None,None,None,100,58], 3: [34,101,53,31,77,69,106,103], 4: [50,9,37,64,None,19,97,12,27], 5: [42,None,23,133,102], 6: [52,33,125], 7: [108,88,80,13,None,124,None], 8: [110,117,85,None,None], 9: [37,24,74,None,None,64,4,50], 10: [2,59,67,None,None,None,100,58], 11: [15,78,112,109], 12: [27,4,50,19,97], 13: [80,82,51,57,17,75,None,7], 14: [None,None,17,75,None,65,70,None,None], 15: [11,78,112,109], 16: [30,48,49,63,107,131,90,None,None,83,123], 17: [75,13,57,84,94,None,118,None,None,14,None], 18: [56,None,103,69,], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: [], 26: [], 27: [], 28: [], 29: [], 30: [], 31: [], 32: [], 33: [], 34: [], 35: [], 36: [], 37: [], 38: [], 39: [], 40: [], 41: [], 42: [], 43: [], 44: [], 45: [], 46: [], 47: [], 48: [], 49: [], 50: [], 51: [], 52: [], 53: [], 54: [], 55: [], 56: [], 57: [], 58: [], 59: [], 60: [], 61: [], 62: [], 63: [], 64: [], 65: [], 66: [], 67: [], 68: [], 69: [], 70: [], 71: [], 72: [], 73: [], 74: [], 75: [], 76: [], 77: [], 78: [], 79: [], 80: [], 81: [], 82: [], 83: [], 84: [], 85: [], 86: [], 87: [], 88: [], 89: [], 90: [], 91: [], 92: [], 93: [], 94: [], 95: [], 96: [], 97: [], 98: [], 99: [], 100: [], 101: [], 102: [], 103: [], 104: [], 105: [], 106: [], 107: [], 108: [], 109: [], 110: [], 111: [], 112: [], 113: [], 114: [], 115: [], 116: [], 117: [], 118: [], 119: [], 120: [], 121: [], 122: [], 123: [], 124: [], 125: [], 126: [], 127: [], 128: [], 129: [], 130: [], 131: [], 132: [], 133: [], 134: []}

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
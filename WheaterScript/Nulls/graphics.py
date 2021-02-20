import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
from numpy.random import randn
from fractions import gcd

TOTAL_ARCHIVOS_EN_DATASET = 134
data_before_refill = [{'Path': '../CleanedData/14002-ACATLAN DE JUAREZ.txt', 'Name': '14002-ACATLAN DE JUAREZ', 'Conteo': [580, 580, 580, 580], 'Total_nulos': 2320, 'Porcentaje_local_nulos': 14.4, 'Total dias existentes': 3438, 'Porcentaje_global_nulos': 0.39}, {'Path': '../CleanedData/14006-TEOCALTICHE.txt', 'Name': '14006-TEOCALTICHE', 'Conteo': [488, 489, 488, 489], 'Total_nulos': 1954, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14009-AMECA.txt', 'Name': '14009-AMECA', 'Conteo': [504, 505, 505, 503], 'Total_nulos': 2017, 'Porcentaje_local_nulos': 12.5, 'Total dias existentes': 3515, 'Porcentaje_global_nulos': 0.34}, {'Path': '../CleanedData/14011-LA HUERTA.txt', 'Name': '14011-LA HUERTA', 'Conteo': [824, 2408, 822, 822], 'Total_nulos': 4876, 'Porcentaje_local_nulos': 30.3, 'Total dias existentes': 3196, 'Porcentaje_global_nulos': 0.83}, {'Path': '../CleanedData/14016-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 'Name': '14016-IXTLAHUACAN DE LOS MEMBRILLOS', 'Conteo': [655, 661, 660, 654], 'Total_nulos': 2630, 'Porcentaje_local_nulos': 16.4, 'Total dias existentes': 3369, 'Porcentaje_global_nulos': 0.45}, {'Path': '../CleanedData/14017-ATOTONILCO EL ALTO.txt', 'Name': '14017-ATOTONILCO EL ALTO', 'Conteo': [490, 522, 497, 493], 'Total_nulos': 2002, 'Porcentaje_local_nulos': 12.5, 'Total dias existentes': 3541, 'Porcentaje_global_nulos': 0.34}, {'Path': '../CleanedData/14018-ATOYAC.txt', 'Name': '14018-ATOYAC', 'Conteo': [672, 678, 673, 673], 'Total_nulos': 2696, 'Porcentaje_local_nulos': 16.8, 'Total dias existentes': 3347, 'Porcentaje_global_nulos': 0.46}, {'Path': '../CleanedData/14023-BOLAÑOS.txt', 'Name': '14023-BOLAÑOS', 'Conteo': [551, 550, 550, 550], 'Total_nulos': 2201, 'Porcentaje_local_nulos': 13.7, 'Total dias existentes': 3468, 'Porcentaje_global_nulos': 0.37}, {'Path': '../CleanedData/14024-TOMATLAN.txt', 'Name': '14024-TOMATLAN', 'Conteo': [883, 900, 884, 884], 'Total_nulos': 3551, 'Porcentaje_local_nulos': 22.1, 'Total dias existentes': 3135, 'Porcentaje_global_nulos': 0.6}, {'Path': '../CleanedData/14025-TEOCALTICHE.txt', 'Name': '14025-TEOCALTICHE', 'Conteo': [2761, 3505, 2727, 2700], 'Total_nulos': 11693, 'Porcentaje_local_nulos': 72.8, 'Total dias existentes': 1319, 'Porcentaje_global_nulos': 1.98}, {'Path': '../CleanedData/14026-COLOTLAN.txt', 'Name': '14026-COLOTLAN', 'Conteo': [458, 457, 457, 457], 'Total_nulos': 1829, 'Porcentaje_local_nulos': 11.4, 'Total dias existentes': 3561, 'Porcentaje_global_nulos': 0.31}, {'Path': '../CleanedData/14028-CIHUATLAN.txt', 'Name': '14028-CIHUATLAN', 'Conteo': [584, 612, 597, 598], 'Total_nulos': 2391, 'Porcentaje_local_nulos': 14.9, 'Total dias existentes': 3443, 'Porcentaje_global_nulos': 0.4}, {'Path': '../CleanedData/14029-CONCEPCION DE BUENOS AIRES.txt', 'Name': '14029-CONCEPCION DE BUENOS AIRES', 'Conteo': [518, 1551, 519, 518], 'Total_nulos': 3106, 'Porcentaje_local_nulos': 19.3, 'Total dias existentes': 3500, 'Porcentaje_global_nulos': 0.53}, {'Path': '../CleanedData/14030-ZAPOTLAN EL GRANDE.txt', 'Name': '14030-ZAPOTLAN EL GRANDE', 'Conteo': [2284, 2294, 2275, 2279], 'Total_nulos': 9132, 'Porcentaje_local_nulos': 56.8, 'Total dias existentes': 1764, 'Porcentaje_global_nulos': 1.55}, {'Path': '../CleanedData/14032-COLOTLAN.txt', 'Name': '14032-COLOTLAN', 'Conteo': [1957, 1953, 1928, 1928], 'Total_nulos': 7766, 'Porcentaje_local_nulos': 48.3, 'Total dias existentes': 2093, 'Porcentaje_global_nulos': 1.31}, {'Path': '../CleanedData/14033-LAGOS DE MORENO.txt', 'Name': '14033-LAGOS DE MORENO', 'Conteo': [1650, 1782, 1650, 1651], 'Total_nulos': 6733, 'Porcentaje_local_nulos': 41.9, 'Total dias existentes': 2368, 'Porcentaje_global_nulos': 1.14}, {'Path': '../CleanedData/14034-TAMAZULA DE GORDIANO.txt', 'Name': '14034-TAMAZULA DE GORDIANO', 'Conteo': [610, 612, 638, 639], 'Total_nulos': 2499, 'Porcentaje_local_nulos': 15.5, 'Total dias existentes': 3408, 'Porcentaje_global_nulos': 0.42}, {'Path': '../CleanedData/14035-MASCOTA.txt', 'Name': '14035-MASCOTA', 'Conteo': [691, 702, 690, 688], 'Total_nulos': 2771, 'Porcentaje_local_nulos': 17.2, 'Total dias existentes': 3337, 'Porcentaje_global_nulos': 0.47}, {'Path': '../CleanedData/14036-CUAUTITLAN DE GARCIA BARRAGAN.txt', 'Name': '14036-CUAUTITLAN DE GARCIA BARRAGAN', 'Conteo': [488, 608, 488, 488], 'Total_nulos': 2072, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14037-HUEJUCAR.txt', 'Name': '14037-HUEJUCAR', 'Conteo': [1096, 1096, 1096, 1096], 'Total_nulos': 4384, 'Porcentaje_local_nulos': 27.3, 'Total dias existentes': 2922, 'Porcentaje_global_nulos': 0.74}, {'Path': '../CleanedData/14038-SAN CRISTOBAL DE LA BARRANCA.txt', 'Name': '14038-SAN CRISTOBAL DE LA BARRANCA', 'Conteo': [489, 492, 488, 488], 'Total_nulos': 1957, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14039-CUQUIO.txt', 'Name': '14039-CUQUIO', 'Conteo': [519, 519, 519, 519], 'Total_nulos': 2076, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3499, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14040-CHAPALA.txt', 'Name': '14040-CHAPALA', 'Conteo': [518, 518, 518, 518], 'Total_nulos': 2072, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3500, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14044-TALPA DE ALLENDE.txt', 'Name': '14044-TALPA DE ALLENDE', 'Conteo': [580, 2789, 581, 581], 'Total_nulos': 4531, 'Porcentaje_local_nulos': 28.2, 'Total dias existentes': 3438, 'Porcentaje_global_nulos': 0.77}, {'Path': '../CleanedData/14046-AUTLAN DE NAVARRO.txt', 'Name': '14046-AUTLAN DE NAVARRO', 'Conteo': [518, 637, 518, 518], 'Total_nulos': 2191, 'Porcentaje_local_nulos': 13.6, 'Total dias existentes': 3500, 'Porcentaje_global_nulos': 0.37}, {'Path': '../CleanedData/14047-OCOTLAN.txt', 'Name': '14047-OCOTLAN', 'Conteo': [488, 510, 488, 488], 'Total_nulos': 1974, 'Porcentaje_local_nulos': 12.3, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14048-CIHUATLAN.txt', 'Name': '14048-CIHUATLAN', 'Conteo': [675, 686, 797, 793], 'Total_nulos': 2951, 'Porcentaje_local_nulos': 18.4, 'Total dias existentes': 3350, 'Porcentaje_global_nulos': 0.5}, {'Path': '../CleanedData/14052-TAPALPA.txt', 'Name': '14052-TAPALPA', 'Conteo': [519, 519, 519, 519], 'Total_nulos': 2076, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3499, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14053-HUEJUQUILLA EL ALTO.txt', 'Name': '14053-HUEJUQUILLA EL ALTO', 'Conteo': [488, 488, 488, 489], 'Total_nulos': 1953, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14054-LAGOS DE MORENO.txt', 'Name': '14054-LAGOS DE MORENO', 'Conteo': [707, 3987, 709, 708], 'Total_nulos': 6111, 'Porcentaje_local_nulos': 38.0, 'Total dias existentes': 3312, 'Porcentaje_global_nulos': 1.03}, {'Path': '../CleanedData/14056-SAN MARTIN HIDALGO.txt', 'Name': '14056-SAN MARTIN HIDALGO', 'Conteo': [702, 961, 702, 702], 'Total_nulos': 3067, 'Porcentaje_local_nulos': 19.1, 'Total dias existentes': 3316, 'Porcentaje_global_nulos': 0.52}, {'Path': '../CleanedData/14059-CABO CORRIENTES.txt', 'Name': '14059-CABO CORRIENTES', 'Conteo': [638, 648, 637, 637], 'Total_nulos': 2560, 'Porcentaje_local_nulos': 15.9, 'Total dias existentes': 3381, 'Porcentaje_global_nulos': 0.43}, {'Path': '../CleanedData/14060-ARANDAS.txt', 'Name': '14060-ARANDAS', 'Conteo': [2271, 2644, 2739, 2734], 'Total_nulos': 10388, 'Porcentaje_local_nulos': 64.6, 'Total dias existentes': 1751, 'Porcentaje_global_nulos': 1.76}, {'Path': '../CleanedData/14063-ETZATLAN.txt', 'Name': '14063-ETZATLAN', 'Conteo': [63, 810, 62, 96], 'Total_nulos': 1031, 'Porcentaje_local_nulos': 6.4, 'Total dias existentes': 3987, 'Porcentaje_global_nulos': 0.17}, {'Path': '../CleanedData/14065-GUADALAJARA.txt', 'Name': '14065-GUADALAJARA', 'Conteo': [2133, 2053, 2034, 2042], 'Total_nulos': 8262, 'Porcentaje_local_nulos': 51.4, 'Total dias existentes': 2037, 'Porcentaje_global_nulos': 1.4}, {'Path': '../CleanedData/14066-GUADALAJARA.txt', 'Name': '14066-GUADALAJARA', 'Conteo': [458, 467, 458, 459], 'Total_nulos': 1842, 'Porcentaje_local_nulos': 11.5, 'Total dias existentes': 3560, 'Porcentaje_global_nulos': 0.31}, {'Path': '../CleanedData/14067-TOMATLAN.txt', 'Name': '14067-TOMATLAN', 'Conteo': [1144, 1171, 1147, 1145], 'Total_nulos': 4607, 'Porcentaje_local_nulos': 28.7, 'Total dias existentes': 2887, 'Porcentaje_global_nulos': 0.78}, {'Path': '../CleanedData/14068-HOSTOTIPAQUILLO.txt', 'Name': '14068-HOSTOTIPAQUILLO', 'Conteo': [564, 594, 564, 564], 'Total_nulos': 2286, 'Porcentaje_local_nulos': 14.2, 'Total dias existentes': 3456, 'Porcentaje_global_nulos': 0.39}, {'Path': '../CleanedData/14069-HUEJUCAR.txt', 'Name': '14069-HUEJUCAR', 'Conteo': [519, 552, 518, 519], 'Total_nulos': 2108, 'Porcentaje_local_nulos': 13.1, 'Total dias existentes': 3500, 'Porcentaje_global_nulos': 0.36}, {'Path': '../CleanedData/14070-DEGOLLADO.txt', 'Name': '14070-DEGOLLADO', 'Conteo': [586, 587, 586, 586], 'Total_nulos': 2345, 'Porcentaje_local_nulos': 14.6, 'Total dias existentes': 3434, 'Porcentaje_global_nulos': 0.4}, {'Path': '../CleanedData/14071-HUEJUQUILLA EL ALTO.txt', 'Name': '14071-HUEJUQUILLA EL ALTO', 'Conteo': [579, 2119, 518, 520], 'Total_nulos': 3736, 'Porcentaje_local_nulos': 23.2, 'Total dias existentes': 3500, 'Porcentaje_global_nulos': 0.63}, {'Path': '../CleanedData/14072-IXTLAHUACAN DE LOS MEMBRILLOS.txt', 'Name': '14072-IXTLAHUACAN DE LOS MEMBRILLOS', 'Conteo': [489, 644, 489, 489], 'Total_nulos': 2111, 'Porcentaje_local_nulos': 13.1, 'Total dias existentes': 3529, 'Porcentaje_global_nulos': 0.36}, \
        {'Path': '../CleanedData/14075-JAMAY.txt', 'Name': '14075-JAMAY', 'Conteo': [1017, 1017, 1015, 1017], 'Total_nulos': 4066, 'Porcentaje_local_nulos': 25.3, 'Total dias existentes': 3004, 'Porcentaje_global_nulos': 0.69}, {'Path': '../CleanedData/14076-JESUS MARIA.txt', 'Name': '14076-JESUS MARIA', 'Conteo': [692, 726, 692, 692], 'Total_nulos': 2802, 'Porcentaje_local_nulos': 17.4, 'Total dias existentes': 3330, 'Porcentaje_global_nulos': 0.47}, {'Path': '../CleanedData/14078-JUCHITLAN.txt', 'Name': '14078-JUCHITLAN', 'Conteo': [612, 1838, 612, 611], 'Total_nulos': 3673, 'Porcentaje_local_nulos': 22.9, 'Total dias existentes': 3407, 'Porcentaje_global_nulos': 0.62}, {'Path': '../CleanedData/14080-YAHUALICA DE GONZALEZ GALLO.txt', 'Name': '14080-YAHUALICA DE GONZALEZ GALLO', 'Conteo': [1831, 1832, 1831, 1832], 'Total_nulos': 7326, 'Porcentaje_local_nulos': 45.6, 'Total dias existentes': 2191, 'Porcentaje_global_nulos': 1.24}, {'Path': '../CleanedData/14081-PUERTO VALLARTA.txt', 'Name': '14081-PUERTO VALLARTA', 'Conteo': [1596, 1609, 1608, 1608], 'Total_nulos': 6421, 'Porcentaje_local_nulos': 40.0, 'Total dias existentes': 2425, 'Porcentaje_global_nulos': 1.09}, {'Path': '../CleanedData/14083-LAGOS DE MORENO.txt', 'Name': '14083-LAGOS DE MORENO', 'Conteo': [1858, 1881, 1880, 1880], 'Total_nulos': 7499, 'Porcentaje_local_nulos': 46.7, 'Total dias existentes': 2161, 'Porcentaje_global_nulos': 1.27}, {'Path': '../CleanedData/14084-LAGOS DE MORENO.txt', 'Name': '14084-LAGOS DE MORENO', 'Conteo': [779, 998, 777, 779], 'Total_nulos': 3333, 'Porcentaje_local_nulos': 20.7, 'Total dias existentes': 3245, 'Porcentaje_global_nulos': 0.56}, {'Path': '../CleanedData/14085-LA HUERTA.txt', 'Name': '14085-LA HUERTA', 'Conteo': [3987, 3987, 3987, 3987], 'Total_nulos': 15948, 'Porcentaje_local_nulos': 99.2, 'Total dias existentes': 31, 'Porcentaje_global_nulos': 2.7}, {'Path': '../CleanedData/14086-LA MANZANILLA DE LA PAZ.txt', 'Name': '14086-LA MANZANILLA DE LA PAZ', 'Conteo': [822, 822, 822, 822], 'Total_nulos': 3288, 'Porcentaje_local_nulos': 20.5, 'Total dias existentes': 3196, 'Porcentaje_global_nulos': 0.56}, {'Path': '../CleanedData/14087-TEPATITLAN DE MORELOS.txt', 'Name': '14087-TEPATITLAN DE MORELOS', 'Conteo': [490, 492, 488, 488], 'Total_nulos': 1958, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14089-TEUCHITLAN.txt', 'Name': '14089-TEUCHITLAN', 'Conteo': [439, 507, 439, 439], 'Total_nulos': 1824, 'Porcentaje_local_nulos': 11.3, 'Total dias existentes': 3583, 'Porcentaje_global_nulos': 0.31}, {'Path': '../CleanedData/14090-TOTOTLAN.txt', 'Name': '14090-TOTOTLAN', 'Conteo': [549, 549, 549, 549], 'Total_nulos': 2196, 'Porcentaje_local_nulos': 13.7, 'Total dias existentes': 3469, 'Porcentaje_global_nulos': 0.37}, {'Path': '../CleanedData/14093-MAGDALENA.txt', 'Name': '14093-MAGDALENA', 'Conteo': [553, 602, 553, 555], 'Total_nulos': 2263, 'Porcentaje_local_nulos': 14.1, 'Total dias existentes': 3465, 'Porcentaje_global_nulos': 0.38}, {'Path': '../CleanedData/14096-MASCOTA.txt', 'Name': '14096-MASCOTA', 'Conteo': [488, 488, 488, 488], 'Total_nulos': 1952, 'Porcentaje_local_nulos': 12.1, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14099-MAZAMITLA.txt', 'Name': '14099-MAZAMITLA', 'Conteo': [396, 2420, 2419, 2420], 'Total_nulos': 7655, 'Porcentaje_local_nulos': 47.6, 'Total dias existentes': 3622, 'Porcentaje_global_nulos': 1.3}, {'Path': '../CleanedData/14100-MEXTICACAN.txt', 'Name': '14100-MEXTICACAN', 'Conteo': [581, 4018, 4018, 3987], 'Total_nulos': 12604, 'Porcentaje_local_nulos': 78.4, 'Total dias existentes': 3468, 'Porcentaje_global_nulos': 2.13}, {'Path': '../CleanedData/14101-TEOCALTICHE.txt', 'Name': '14101-TEOCALTICHE', 'Conteo': [637, 1657, 639, 636], 'Total_nulos': 3569, 'Porcentaje_local_nulos': 22.2, 'Total dias existentes': 3382, 'Porcentaje_global_nulos': 0.6}, {'Path': '../CleanedData/14104-ZAPOTLANEJO.txt', 'Name': '14104-ZAPOTLANEJO', 'Conteo': [2319, 3596, 2538, 2539], 'Total_nulos': 10992, 'Porcentaje_local_nulos': 68.4, 'Total dias existentes': 1709, 'Porcentaje_global_nulos': 1.86}, {'Path': '../CleanedData/14112-PIHUAMO.txt', 'Name': '14112-PIHUAMO', 'Conteo': [855, 855, 855, 855], 'Total_nulos': 3420, 'Porcentaje_local_nulos': 21.3, 'Total dias existentes': 3163, 'Porcentaje_global_nulos': 0.58}, {'Path': '../CleanedData/14113-ACATLAN DE JUAREZ.txt', 'Name': '14113-ACATLAN DE JUAREZ', 'Conteo': [580, 580, 1525, 1523], 'Total_nulos': 4208, 'Porcentaje_local_nulos': 26.2, 'Total dias existentes': 3438, 'Porcentaje_global_nulos': 0.71}, {'Path': '../CleanedData/14114-LAGOS DE MORENO.txt', 'Name': '14114-LAGOS DE MORENO', 'Conteo': [577, 649, 577, 577], 'Total_nulos': 2380, 'Porcentaje_local_nulos': 14.8, 'Total dias existentes': 3441, 'Porcentaje_global_nulos': 0.4}, {'Path': '../CleanedData/14117-VILLA PURIFICACION.txt', 'Name': '14117-VILLA PURIFICACION', 'Conteo': [1058, 3968, 1060, 1061], 'Total_nulos': 7147, 'Porcentaje_local_nulos': 44.5, 'Total dias existentes': 2960, 'Porcentaje_global_nulos': 1.21}, {'Path': '../CleanedData/14118-TUXPAN.txt', 'Name': '14118-TUXPAN', 'Conteo': [522, 4018, 522, 523], 'Total_nulos': 5585, 'Porcentaje_local_nulos': 34.7, 'Total dias existentes': 3497, 'Porcentaje_global_nulos': 0.95}, {'Path': '../CleanedData/14119-QUITUPAN.txt', 'Name': '14119-QUITUPAN', 'Conteo': [3987, 3987, 3987, 3987], 'Total_nulos': 15948, 'Porcentaje_local_nulos': 99.2, 'Total dias existentes': 31, 'Porcentaje_global_nulos': 2.7}, {'Path': '../CleanedData/14122-TEOCALTICHE.txt', 'Name': '14122-TEOCALTICHE', 'Conteo': [852, 2453, 852, 852], 'Total_nulos': 5009, 'Porcentaje_local_nulos': 31.2, 'Total dias existentes': 3166, 'Porcentaje_global_nulos': 0.85}, {'Path': '../CleanedData/14123-SAN DIEGO DE ALEJANDRIA.txt', 'Name': '14123-SAN DIEGO DE ALEJANDRIA', 'Conteo': [1406, 2322, 1408, 1408], 'Total_nulos': 6544, 'Porcentaje_local_nulos': 40.7, 'Total dias existentes': 2614, 'Porcentaje_global_nulos': 1.11}, {'Path': '../CleanedData/14125-MIXTLAN.txt', 'Name': '14125-MIXTLAN', 'Conteo': [853, 853, 853, 853], 'Total_nulos': 3412, 'Porcentaje_local_nulos': 21.2, 'Total dias existentes': 3165, 'Porcentaje_global_nulos': 0.58}, {'Path': '../CleanedData/14129-TONILA.txt', 'Name': '14129-TONILA', 'Conteo': [1038, 4018, 3047, 3047], 'Total_nulos': 11150, 'Porcentaje_local_nulos': 69.4, 'Total dias existentes': 2980, 'Porcentaje_global_nulos': 1.89}, {'Path': '../CleanedData/14132-SAN PEDRO TLAQUEPAQUE.txt', 'Name': '14132-SAN PEDRO TLAQUEPAQUE', 'Conteo': [488, 4018, 488, 488], 'Total_nulos': 5482, 'Porcentaje_local_nulos': 34.1, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.93}, {'Path': '../CleanedData/14136-AMATITAN.txt', 'Name': '14136-AMATITAN', 'Conteo': [706, 806, 801, 803], 'Total_nulos': 3116, 'Porcentaje_local_nulos': 19.4, 'Total dias existentes': 3326, 'Porcentaje_global_nulos': 0.53}, {'Path': '../CleanedData/14139-UNION DE TULA.txt', 'Name': '14139-UNION DE TULA', 'Conteo': [3352, 3606, 3404, 3405], 'Total_nulos': 13767, 'Porcentaje_local_nulos': 85.7, 'Total dias existentes': 666, 'Porcentaje_global_nulos': 2.33}, {'Path': '../CleanedData/14140-TALPA DE ALLENDE.txt', 'Name': '14140-TALPA DE ALLENDE', 'Conteo': [886, 892, 885, 885], 'Total_nulos': 3548, 'Porcentaje_local_nulos': 22.1, 'Total dias existentes': 3133, 'Porcentaje_global_nulos': 0.6}, {'Path': '../CleanedData/14141-TAMAZULA DE GORDIANO.txt', 'Name': '14141-TAMAZULA DE GORDIANO', 'Conteo': [519, 519, 519, 519], 'Total_nulos': 2076, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3499, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14142-TAPALPA.txt', 'Name': '14142-TAPALPA', 'Conteo': [610, 621, 610, 610], 'Total_nulos': 2451, 'Porcentaje_local_nulos': 15.3, 'Total dias existentes': 3408, 'Porcentaje_global_nulos': 0.41}, {'Path': '../CleanedData/14143-TECOLOTLAN.txt', 'Name': '14143-TECOLOTLAN', 'Conteo': [488, 490, 488, 488], 'Total_nulos': 1954, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14144-COLOTLAN.txt', 'Name': '14144-COLOTLAN', 'Conteo': [488, 493, 488, 488], 'Total_nulos': 1957, 'Porcentaje_local_nulos': 12.2, 'Total dias existentes': 3530, 'Porcentaje_global_nulos': 0.33}, {'Path': '../CleanedData/14145-TEOCALTICHE.txt', 'Name': '14145-TEOCALTICHE', 'Conteo': [457, 457, 457, 457], 'Total_nulos': 1828, 'Porcentaje_local_nulos': 11.4, 'Total dias existentes': 3561, 'Porcentaje_global_nulos': 0.31}, {'Path': '../CleanedData/14146-TEOCUITATLAN DE CORONA.txt', 'Name': '14146-TEOCUITATLAN DE CORONA', 'Conteo': [549, 553, 549, 549], 'Total_nulos': 2200, 'Porcentaje_local_nulos': 13.7, 'Total dias existentes': 3469, 'Porcentaje_global_nulos': 0.37}, {'Path': '../CleanedData/14155-TUXCACUESCO.txt', 'Name': '14155-TUXCACUESCO', 'Conteo': [457, 4018, 1253, 1254], 'Total_nulos': 6982, 'Porcentaje_local_nulos': 43.4, 'Total dias existentes': 3561, 'Porcentaje_global_nulos': 1.18}, {'Path': '../CleanedData/14156-TUXCUECA.txt', 'Name': '14156-TUXCUECA', 'Conteo': [457, 457, 457, 457], 'Total_nulos': 1828, 'Porcentaje_local_nulos': 11.4, 'Total dias existentes': 3561, 'Porcentaje_global_nulos': 0.31}, {'Path': '../CleanedData/14157-UNION DE SAN ANTONIO.txt', 'Name': '14157-UNION DE SAN ANTONIO', 'Conteo': [549, 772, 552, 549], 'Total_nulos': 2422, 'Porcentaje_local_nulos': 15.1, 'Total dias existentes': 3469, 'Porcentaje_global_nulos': 0.41}, {'Path': '../CleanedData/14160-VALLE DE JUAREZ.txt', 'Name': '14160-VALLE DE JUAREZ', 'Conteo': [1157, 1161, 1168, 1168], 'Total_nulos': 4654, 'Porcentaje_local_nulos': 29.0, 'Total dias existentes': 2920, 'Porcentaje_global_nulos': 0.79}, \
        {'Path': '../CleanedData/14164-VILLA GUERRERO.txt', 'Name': '14164-VILLA GUERRERO', 'Conteo': [1662, 1834, 1684, 1684], 'Total_nulos': 6864, 'Porcentaje_local_nulos': 42.7, 'Total dias existentes': 2361, 'Porcentaje_global_nulos': 1.16}, {'Path': '../CleanedData/14165-CAÑADAS DE OBREGON.txt', 'Name': '14165-CAÑADAS DE OBREGON', 'Conteo': [1, 133, 362, 362], 'Total_nulos': 858, 'Porcentaje_local_nulos': 5.3, 'Total dias existentes': 4018, 'Porcentaje_global_nulos': 0.15}, {'Path': '../CleanedData/14167-YAHUALICA DE GONZALEZ GALLO.txt', 'Name': '14167-YAHUALICA DE GONZALEZ GALLO', 'Conteo': [213, 1821, 213, 213], 'Total_nulos': 2460, 'Porcentaje_local_nulos': 15.3, 'Total dias existentes': 3805, 'Porcentaje_global_nulos': 0.42}, {'Path': '../CleanedData/14168-ZACOALCO DE TORRES.txt', 'Name': '14168-ZACOALCO DE TORRES', 'Conteo': [540, 3777, 411, 409], 'Total_nulos': 5137, 'Porcentaje_local_nulos': 32.0, 'Total dias existentes': 3704, 'Porcentaje_global_nulos': 0.87}, {'Path': '../CleanedData/14169-ZAPOPAN.txt', 'Name': '14169-ZAPOPAN', 'Conteo': [2, 3934, 5, 0], 'Total_nulos': 3941, 'Porcentaje_local_nulos': 24.5, 'Total dias existentes': 4138, 'Porcentaje_global_nulos': 0.67}, {'Path': '../CleanedData/14179-OJUELOS DE JALISCO.txt', 'Name': '14179-OJUELOS DE JALISCO', 'Conteo': [197, 257, 199, 199], 'Total_nulos': 852, 'Porcentaje_local_nulos': 5.3, 'Total dias existentes': 3912, 'Porcentaje_global_nulos': 0.14}, {'Path': '../CleanedData/14180-QUITUPAN.txt', 'Name': '14180-QUITUPAN', 'Conteo': [519, 519, 519, 519], 'Total_nulos': 2076, 'Porcentaje_local_nulos': 12.9, 'Total dias existentes': 3558, 'Porcentaje_global_nulos': 0.35}, {'Path': '../CleanedData/14187-TEQUILA.txt', 'Name': '14187-TEQUILA', 'Conteo': [61, 200, 61, 62], 'Total_nulos': 384, 'Porcentaje_local_nulos': 2.4, 'Total dias existentes': 3988, 'Porcentaje_global_nulos': 0.07}, {'Path': '../CleanedData/14189-TIZAPAN EL ALTO.txt', 'Name': '14189-TIZAPAN EL ALTO', 'Conteo': [4, 469, 5, 4], 'Total_nulos': 482, 'Porcentaje_local_nulos': 3.0, 'Total dias existentes': 4075, 'Porcentaje_global_nulos': 0.08}, {'Path': '../CleanedData/14191-VALLE DE JUAREZ.txt', 'Name': '14191-VALLE DE JUAREZ', 'Conteo': [3744, 3757, 3744, 3744], 'Total_nulos': 14989, 'Porcentaje_local_nulos': 93.3, 'Total dias existentes': 274, 'Porcentaje_global_nulos': 2.54}, {'Path': '../CleanedData/14195-SAN JUANITO DE ESCOBEDO.txt', 'Name': '14195-SAN JUANITO DE ESCOBEDO', 'Conteo': [1987, 2226, 1948, 1948], 'Total_nulos': 8109, 'Porcentaje_local_nulos': 50.5, 'Total dias existentes': 2132, 'Porcentaje_global_nulos': 1.37}, {'Path': '../CleanedData/14197-UNION DE TULA.txt', 'Name': '14197-UNION DE TULA', 'Conteo': [1592, 1601, 1642, 1642], 'Total_nulos': 6477, 'Porcentaje_local_nulos': 40.3, 'Total dias existentes': 2432, 'Porcentaje_global_nulos': 1.1}, {'Path': '../CleanedData/14198-CUAUTITLAN DE GARCIA BARRAGAN.txt', 'Name': '14198-CUAUTITLAN DE GARCIA BARRAGAN', 'Conteo': [1461, 1489, 1460, 1462], 'Total_nulos': 5872, 'Porcentaje_local_nulos': 36.5, 'Total dias existentes': 2649, 'Porcentaje_global_nulos': 0.99}, {'Path': '../CleanedData/14199-PONCITLAN.txt', 'Name': '14199-PONCITLAN', 'Conteo': [2465, 2479, 2476, 2477], 'Total_nulos': 9897, 'Porcentaje_local_nulos': 61.6, 'Total dias existentes': 1553, 'Porcentaje_global_nulos': 1.68}, {'Path': '../CleanedData/14200-SAN PEDRO TLAQUEPAQUE.txt', 'Name': '14200-SAN PEDRO TLAQUEPAQUE', 'Conteo': [2521, 2529, 2524, 2523], 'Total_nulos': 10097, 'Porcentaje_local_nulos': 62.8, 'Total dias existentes': 1564, 'Porcentaje_global_nulos': 1.71}, {'Path': '../CleanedData/14266-JALOSTOTITLAN.txt', 'Name': '14266-JALOSTOTITLAN', 'Conteo': [191, 208, 215, 213], 'Total_nulos': 827, 'Porcentaje_local_nulos': 5.1, 'Total dias existentes': 3828, 'Porcentaje_global_nulos': 0.14}, {'Path': '../CleanedData/14269-AHUALULCO DE MERCADO.txt', 'Name': '14269-AHUALULCO DE MERCADO', 'Conteo': [61, 61, 61, 61], 'Total_nulos': 244, 'Porcentaje_local_nulos': 1.5, 'Total dias existentes': 4047, 'Porcentaje_global_nulos': 0.04}, {'Path': '../CleanedData/14294-TLAJOMULCO DE ZUÑIGA.txt', 'Name': '14294-TLAJOMULCO DE ZUÑIGA', 'Conteo': [3435, 3917, 3587, 3590], 'Total_nulos': 14529, 'Porcentaje_local_nulos': 90.4, 'Total dias existentes': 608, 'Porcentaje_global_nulos': 2.46}, {'Path': '../CleanedData/14297-GUACHINANGO.txt', 'Name': '14297-GUACHINANGO', 'Conteo': [0, 0, 0, 0], 'Total_nulos': 0, 'Porcentaje_local_nulos': 0.0, 'Total dias existentes': 4169, 'Porcentaje_global_nulos': 0.0}, {'Path': '../CleanedData/14306-HUEJUQUILLA EL ALTO.txt', 'Name': '14306-HUEJUQUILLA EL ALTO', 'Conteo': [31, 31, 31, 32], 'Total_nulos': 125, 'Porcentaje_local_nulos': 0.8, 'Total dias existentes': 4046, 'Porcentaje_global_nulos': 0.02}, {'Path': '../CleanedData/14311-TOLIMAN.txt', 'Name': '14311-TOLIMAN', 'Conteo': [348, 350, 347, 349], 'Total_nulos': 1394, 'Porcentaje_local_nulos': 8.7, 'Total dias existentes': 3671, 'Porcentaje_global_nulos': 0.24}, {'Path': '../CleanedData/14317-MIXTLAN.txt', 'Name': '14317-MIXTLAN', 'Conteo': [2293, 2995, 2261, 2261], 'Total_nulos': 9810, 'Porcentaje_local_nulos': 61.0, 'Total dias existentes': 1759, 'Porcentaje_global_nulos': 1.66}, {'Path': '../CleanedData/14320-LAGOS DE MORENO.txt', 'Name': '14320-LAGOS DE MORENO', 'Conteo': [792, 792, 791, 791], 'Total_nulos': 3166, 'Porcentaje_local_nulos': 19.7, 'Total dias existentes': 3227, 'Porcentaje_global_nulos': 0.54}, {'Path': '../CleanedData/14323-TECHALUTA DE MONTENEGRO.txt', 'Name': '14323-TECHALUTA DE MONTENEGRO', 'Conteo': [3815, 3818, 3815, 3816], 'Total_nulos': 15264, 'Porcentaje_local_nulos': 95.0, 'Total dias existentes': 262, 'Porcentaje_global_nulos': 2.58}, {'Path': '../CleanedData/14324-TOTATICHE.txt', 'Name': '14324-TOTATICHE', 'Conteo': [36, 392, 37, 38], 'Total_nulos': 503, 'Porcentaje_local_nulos': 3.1, 'Total dias existentes': 3984, 'Porcentaje_global_nulos': 0.09}, {'Path': '../CleanedData/14326-MEZQUITIC.txt', 'Name': '14326-MEZQUITIC', 'Conteo': [108, 514, 227, 227], 'Total_nulos': 1076, 'Porcentaje_local_nulos': 6.7, 'Total dias existentes': 4001, 'Porcentaje_global_nulos': 0.18}, {'Path': '../CleanedData/14329-GUADALAJARA.txt', 'Name': '14329-GUADALAJARA', 'Conteo': [365, 365, 365, 365], 'Total_nulos': 1460, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3804, 'Porcentaje_global_nulos': 0.25}, {'Path': '../CleanedData/14331-COLOTLAN.txt', 'Name': '14331-COLOTLAN', 'Conteo': [2933, 3597, 2932, 2931], 'Total_nulos': 12393, 'Porcentaje_local_nulos': 77.1, 'Total dias existentes': 1088, 'Porcentaje_global_nulos': 2.1}, {'Path': '../CleanedData/14336-PIHUAMO.txt', 'Name': '14336-PIHUAMO', 'Conteo': [578, 583, 577, 577], 'Total_nulos': 2315, 'Porcentaje_local_nulos': 14.4, 'Total dias existentes': 3441, 'Porcentaje_global_nulos': 0.39}, {'Path': '../CleanedData/14337-YAHUALICA DE GONZALEZ GALLO.txt', 'Name': '14337-YAHUALICA DE GONZALEZ GALLO', 'Conteo': [365, 479, 365, 365], 'Total_nulos': 1574, 'Porcentaje_local_nulos': 9.8, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.27}, {'Path': '../CleanedData/14339-PUERTO VALLARTA.txt', 'Name': '14339-PUERTO VALLARTA', 'Conteo': [0, 0, 0, 0], 'Total_nulos': 0, 'Porcentaje_local_nulos': 0.0, 'Total dias existentes': 4139, 'Porcentaje_global_nulos': 0.0}, {'Path': '../CleanedData/14343-EJUTLA.txt', 'Name': '14343-EJUTLA', 'Conteo': [0, 0, 0, 0], 'Total_nulos': 0, 'Porcentaje_local_nulos': 0.0, 'Total dias existentes': 4018, 'Porcentaje_global_nulos': 0.0}, {'Path': '../CleanedData/14346-MEZQUITIC.txt', 'Name': '14346-MEZQUITIC', 'Conteo': [365, 365, 365, 365], 'Total_nulos': 1460, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3712, 'Porcentaje_global_nulos': 0.25}, {'Path': '../CleanedData/14348-JILOTLAN DE LOS DOLORES.txt', 'Name': '14348-JILOTLAN DE LOS DOLORES', 'Conteo': [1371, 2534, 2709, 2709], 'Total_nulos': 9323, 'Porcentaje_local_nulos': 58.0, 'Total dias existentes': 2647, 'Porcentaje_global_nulos': 1.58}, {'Path': '../CleanedData/14349-ATENGUILLO.txt', 'Name': '14349-ATENGUILLO', 'Conteo': [365, 1441, 365, 365], 'Total_nulos': 2536, 'Porcentaje_local_nulos': 15.8, 'Total dias existentes': 3774, 'Porcentaje_global_nulos': 0.43}, {'Path': '../CleanedData/14350-TUXCACUESCO.txt', 'Name': '14350-TUXCACUESCO', 'Conteo': [365, 367, 365, 365], 'Total_nulos': 1462, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.25}, {'Path': '../CleanedData/14351-TALA.txt', 'Name': '14351-TALA', 'Conteo': [396, 410, 396, 397], 'Total_nulos': 1599, 'Porcentaje_local_nulos': 9.9, 'Total dias existentes': 3681, 'Porcentaje_global_nulos': 0.27}, {'Path': '../CleanedData/14355-LA BARCA.txt', 'Name': '14355-LA BARCA', 'Conteo': [366, 372, 365, 365], 'Total_nulos': 1468, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.25}, {'Path': '../CleanedData/14367-UNION DE SAN ANTONIO.txt', 'Name': '14367-UNION DE SAN ANTONIO', 'Conteo': [2479, 2567, 2480, 2479], 'Total_nulos': 10005, 'Porcentaje_local_nulos': 62.3, 'Total dias existentes': 1540, 'Porcentaje_global_nulos': 1.69}, {'Path': '../CleanedData/14368-SAYULA.txt', 'Name': '14368-SAYULA', 'Conteo': [703, 757, 701, 701], 'Total_nulos': 2862, 'Porcentaje_local_nulos': 17.8, 'Total dias existentes': 3377, 'Porcentaje_global_nulos': 0.48}, {'Path': '../CleanedData/14369-ARANDAS.txt', 'Name': '14369-ARANDAS', 'Conteo': [828, 838, 828, 828], 'Total_nulos': 3322, 'Porcentaje_local_nulos': 20.7, 'Total dias existentes': 3191, 'Porcentaje_global_nulos': 0.56}, {'Path': '../CleanedData/14379-PONCITLAN.txt', 'Name': '14379-PONCITLAN', 'Conteo': [365, 1611, 365, 365], 'Total_nulos': 2706, 'Porcentaje_local_nulos': 16.8, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.46}, {'Path': '../CleanedData/14386-TONALA.txt', 'Name': '14386-TONALA', 'Conteo': [414, 492, 439, 409], 'Total_nulos': 1754, 'Porcentaje_local_nulos': 10.9, 'Total dias existentes': 3742, 'Porcentaje_global_nulos': 0.3}, \
        {'Path': '../CleanedData/14388-ZAPOTLANEJO.txt', 'Name': '14388-ZAPOTLANEJO', 'Conteo': [2619, 2619, 2619, 2619], 'Total_nulos': 10476, 'Porcentaje_local_nulos': 65.2, 'Total dias existentes': 1399, 'Porcentaje_global_nulos': 1.77}, {'Path': '../CleanedData/14390-AUTLAN DE NAVARRO.txt', 'Name': '14390-AUTLAN DE NAVARRO', 'Conteo': [2537, 2676, 2546, 2549], 'Total_nulos': 10308, 'Porcentaje_local_nulos': 64.1, 'Total dias existentes': 1494, 'Porcentaje_global_nulos': 1.75}, {'Path': '../CleanedData/14391-TIZAPAN EL ALTO.txt', 'Name': '14391-TIZAPAN EL ALTO', 'Conteo': [366, 365, 365, 365], 'Total_nulos': 1461, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.25}, {'Path': '../CleanedData/14392-LAGOS DE MORENO.txt', 'Name': '14392-LAGOS DE MORENO', 'Conteo': [812, 817, 816, 816], 'Total_nulos': 3261, 'Porcentaje_local_nulos': 20.3, 'Total dias existentes': 3209, 'Porcentaje_global_nulos': 0.55}, {'Path': '../CleanedData/14395-UNION DE TULA.txt', 'Name': '14395-UNION DE TULA', 'Conteo': [2773, 2776, 2773, 2773], 'Total_nulos': 11095, 'Porcentaje_local_nulos': 69.0, 'Total dias existentes': 1245, 'Porcentaje_global_nulos': 1.88}, {'Path': '../CleanedData/14396-JOCOTEPEC.txt', 'Name': '14396-JOCOTEPEC', 'Conteo': [396, 492, 396, 396], 'Total_nulos': 1680, 'Porcentaje_local_nulos': 10.5, 'Total dias existentes': 3681, 'Porcentaje_global_nulos': 0.28}, {'Path': '../CleanedData/14397-ZAPOTLANEJO.txt', 'Name': '14397-ZAPOTLANEJO', 'Conteo': [366, 365, 365, 365], 'Total_nulos': 1461, 'Porcentaje_local_nulos': 9.1, 'Total dias existentes': 3743, 'Porcentaje_global_nulos': 0.25}]

def graph_nulls_comparison(pct_list,etapa):
    if etapa == 0:
        etapa_name = 'Pre-Etapa'
    else:
        etapa_name = f'Etapa {etapa}'
    # Wedge properties 
    wp = { 'linewidth' : 1, 'edgecolor' : "black"} 

    # Creating autocpt arguments 
    def func(pct, allvalues): 
        #absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.2f}%".format(pct)
        

    # Creating explode data 
    #explode = tuple([0.01 for i in range(0,len(pct_list))])#(0.1, 0.1, 0.1, 0.1)

    # Creating plot 
    fig, ax = plt.subplots(figsize =(10, 7)) 
    wedges, texts, autotexts = ax.pie(pct_list, 
                                    autopct = lambda pct: func(pct, pct_list), 
                                    startangle = 90, 
                                    wedgeprops = wp, 
    #                                explode = explode,
                                    textprops = dict(color ="black")) 
    #Changing font color of pct's
    for autotext in autotexts:
        autotext.set_color('white')

    labels = ['Recuperado', 'Nulo']

    ax.legend(wedges, labels, 
            loc ="center left", 
            title = 'Tipo de dato',
            bbox_to_anchor =(1,0, 0.5, 1)) 
    
    ax.set_title(f'Balance de datos Nulos y No Nulos en {etapa_name}')
    fig.canvas.set_window_title(f'BalanceNulosVsNoNulos-E{etapa}')
    plt.setp(autotexts, size = 8, weight ="bold") 
    plt.show()

def graph_comparison(etapa):
    Total_data_in_dataset = 2764384
    Total_data_in_finaldataset = 2009000
    total_nulos_preetapa = 1201445
    total_nulos_etapa1 = 151216
    total_nulos_etapa2 = 24516
    total_nulos_etapa3 = 6947
    total_nulos_etapa4 = 6366
    total_nulos_etapa5 = 6056
    total_nulos_etapa6 = 6008
    total_nulos_finaldataset = 2748

    if etapa == 0:
        pct_list = [Total_data_in_dataset-total_nulos_preetapa,total_nulos_preetapa]
        total_nulos_recuperados = 0
        nulos_existentes = total_nulos_preetapa
    elif etapa == 1:
        pct_list = [Total_data_in_dataset-total_nulos_etapa1,total_nulos_etapa1]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa1
        nulos_existentes = total_nulos_etapa1
    elif etapa == 2:
        pct_list = [Total_data_in_dataset-total_nulos_etapa2,total_nulos_etapa2]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa2
        nulos_existentes = total_nulos_etapa2
    elif etapa == 3:
        pct_list = [Total_data_in_dataset-total_nulos_etapa3,total_nulos_etapa3]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa3
        nulos_existentes = total_nulos_etapa3
    elif etapa == 4:
        pct_list = [Total_data_in_dataset-total_nulos_etapa4,total_nulos_etapa4]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa4
        nulos_existentes = total_nulos_etapa4
    elif etapa == 5:
        pct_list = [Total_data_in_dataset-total_nulos_etapa5,total_nulos_etapa5]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa5
        nulos_existentes = total_nulos_etapa5
    elif etapa == 6:
        pct_list = [Total_data_in_dataset-total_nulos_etapa6,total_nulos_etapa6]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_etapa6
        nulos_existentes = total_nulos_etapa6
    elif etapa == 7:
        pct_list = [Total_data_in_finaldataset-total_nulos_finaldataset,total_nulos_finaldataset]
        total_nulos_recuperados = total_nulos_preetapa - total_nulos_finaldataset
        nulos_existentes = total_nulos_finaldataset
    else:
        total_nulos_recuperados = 0
        nulos_existentes = total_nulos_preetapa
    
    nulls_comp = [total_nulos_recuperados, nulos_existentes]
    graph_nulls_comparison(nulls_comp, etapa)
    # Wedge properties 
    wp = { 'linewidth' : 1, 'edgecolor' : "black"} 

    # Creating autocpt arguments 
    def func(pct, allvalues): 
        #absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.2f}%".format(pct)
        

    # Creating explode data 
    #explode = tuple([0.01 for i in range(0,len(pct_list))])#(0.1, 0.1, 0.1, 0.1)

    # Creating plot 
    fig, ax = plt.subplots(figsize =(10, 7)) 
    wedges, texts, autotexts = ax.pie(pct_list, 
                                    autopct = lambda pct: func(pct, pct_list), 
                                    startangle = 90, 
                                    wedgeprops = wp, 
    #                                explode = explode,
                                    textprops = dict(color ="black")) 
    #Changing font color of pct's
    for autotext in autotexts:
        autotext.set_color('white')

    labels = ['No nulo', 'Nulo']

    ax.legend(wedges, labels, 
            loc ="center left",
            title = 'Tipo de dato',
            bbox_to_anchor =(1,0, 0.5, 1)) 

    ax.set_title('Estado del Dataset')
    fig.canvas.set_window_title(f'EstadoDelDataset-E{etapa}')
    plt.setp(autotexts, size = 8, weight ="bold") 
    plt.show()

def plot_tables(townList,group):
    fig, axes = plt.subplots(figsize=(20,7))
    #Se llena la lista con cadenas vacías para que sea divisiblemente exacta    
    townList = fill_list(townList)
    #Obtiene el número de filas y columnas 
    rows,cols = get_num_of_cols_rows(townList)
    #Hace un reshape que permite tener una tabla de los datos de rows*cols
    reshaped_townList = reshape_Array(townList,rows,cols)
    #Obtiene el código del color para el grupo especifico
    colorCode = color_code(group)
    #Genera una lista con ese código del número de elementos que tendrá la tabla
    array_colors = [[colorCode] * len(townList)]
    #Hace reshape de ese arreglo de colores que corresponda al mismo tamaño de la tabla de datos
    array_colors = reshape_Array(array_colors,rows,cols)
    #Obtiene las labels para el grupo con respecto al número de columnas que tendrá
    collabel = get_labels_cols(cols,group)
    #Pinta la tabla con los datos
    table = axes.table(cellText=reshaped_townList,colLabels=collabel,loc='center',colColours =[colorCode] * cols, cellColours=array_colors, cellLoc='left')

def graph_global_nulls(data_dict):

    pct_list, names_list = data_for_graph_null(data_dict)
    # Wedge properties 
    wp = { 'linewidth' : 1, 'edgecolor' : "black" } 

    # Creating autocpt arguments 
    def func(pct, allvalues): 
        #absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.2f}%".format(pct)
        

    # Creating explode data 
    #explode = tuple([0.1 for i in range(0,len(pct_list))])#(0.1, 0.1, 0.1, 0.1)

    # Creating plot 
    fig, ax = plt.subplots(figsize =(10, 7)) 
    wedges, texts, autotexts = ax.pie(pct_list,  
                                    autopct = lambda pct: func(pct, pct_list), 
                                    startangle = 90, 
                                    wedgeprops = wp, 
                                    #explode = explode,
                                    textprops = dict(color ="black")) 
    
    
    ax.legend(wedges, ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4'], 
            title ="Grupos", 
            loc ="center left", 
            bbox_to_anchor =(1,0, 0.5, 1)) 
    
    plt.setp(autotexts, size = 8, weight ="bold") 
    #Crea las tablas de datos para cada grupo
    for i in range(0,len(names_list)):
        plot_tables(names_list[i],i+1)
    plt.show()

def group_data(global_nulls_percentage_list, names_towns):
    group1 = {'pct': 0, 'towns':[]}
    group2 = {'pct': 0, 'towns':[]}
    group3 = {'pct': 0, 'towns':[]}
    group4 = {'pct': 0, 'towns':[]}
    list_groups = []
    list_towns = []
    index = 0
    #Por cada porcentaje
    for pct in global_nulls_percentage_list:
        #Grupo 1 pertenece a las ciudades que aportan entre 0-0.5 porciento de nulos totales
        if pct <= 0.5:
            group1['pct'] += pct
            group1['towns'].append(names_towns[index])
        #Grupo 2 pertenece a las ciudades que aportan entre 0.5-1.0 porciento de nulos totales
        elif pct > 0.5 and pct <= 1:
            group2['pct'] += pct
            group2['towns'].append(names_towns[index])
        #Grupo 3 pertenece a las ciudades que aportan entre 1.0-2.0 porciento de nulos totales
        elif pct > 1 and pct <= 2:
            group3['pct'] += pct
            group3['towns'].append(names_towns[index])
        #Grupo 4 pertenece a las ciudades que aportan entre 2.0-3.0 porciento de nulos totales
        elif pct > 2:
            group4['pct'] += pct
            group4['towns'].append(names_towns[index])
        index += 1

    #Si el porcentaje de nulos en el grupo 1 tuvo porcentaje mayor a cero
    if group1['pct']>0:
        #list_groups.append(round(group1['pct'],2))
        list_groups.append(len(group1['towns']))
        list_towns.append(group1['towns'])
    #Si el porcentaje de nulos en el grupo 2 tuvo porcentaje mayor a cero
    if group2['pct']>0:
        #list_groups.append(round(group2['pct'],2))
        list_groups.append(len(group2['towns']))
        list_towns.append(group2['towns'])
    #Si el porcentaje de nulos en el grupo 3 tuvo porcentaje mayor a cero
    if group3['pct']>0:
        #list_groups.append(round(group3['pct'],2))
        list_groups.append(len(group3['towns']))
        list_towns.append(group3['towns'])
    #Si el porcentaje de nulos en el grupo 4 tuvo porcentaje mayor a cero
    if group4['pct']>0:
        #list_groups.append(round(group4['pct'],2))
        list_groups.append(len(group4['towns']))
        list_towns.append(group4['towns'])

    print(f'LENS   G1: {len(group1["towns"])} G2: {len(group2["towns"])} G3: {len(group3["towns"])} G4: {len(group4["towns"])}')
    print(f'GROUPS PCT: G1: {group1["pct"]} G2: {group2["pct"]} G3: {group3["pct"]} G4: {group4["pct"]}')
    print(list_groups)
    return np.array(list_groups), list_towns

def data_for_graph_null(list_data):

    #Ordena los diccionarios de las ciudades de mayor a menor porcentaje global de nulos que aportan
    ordered_data = sorted(list_data, key=itemgetter('Porcentaje_global_nulos'), reverse=True)
    #Obtiene la lista de porcentajes globales de cada ciudad
    global_nulls_percentage_list = np.array([dict_file['Porcentaje_global_nulos'] for dict_file in ordered_data])
    #Obtiene la lista de nombres de cada ciudad
    names_towns = np.array([dict_file['Name'] for dict_file in ordered_data])
    #Agrupa los datos de las ciudades hasta en 4 posibles grupos
    grouped_data, grouped_towns = group_data(global_nulls_percentage_list,names_towns)
    #print(grouped_data)
    #print(grouped_towns)
    return grouped_data, grouped_towns

def generate_labelGroups(num_groups):
    """
    Genera las etiquetas de cada grupo que se graficara
    """
    labels = []
    for i in range(1,num_groups+1):
        group = 'Group' + str(i)
        labels.append(group)
    return labels

def fill_list(townList):
    """
    Llena una lista de cadenas vacias para que la lista tenga un número de elementos par
    """
    while (len(townList)%2 != 0):
        townList.append('')
    
    return townList

def get_num_of_cols_rows(townList):
    """
    Obtiene el numero de columnas y filas que tendrá la tabla de datos
    """
    
    tam_list = len(townList)
    num_rows = 0
    num_cols = 0
    """if tam_list>=144 and tam_list<168:
        num_cols = 7
    elif tam_list>=120 and tam_list<144:
        num_cols = 6
    if tam_list>=96:
        num_cols = 5"""
    if tam_list>=72:
        num_cols = 4
    elif tam_list>=50 and tam_list<72:
        num_cols = 3
    elif tam_list>=25 and tam_list<50:
        num_cols = 2
    elif tam_list<25:
        num_cols = 1
    
    while(tam_list%num_cols!=0):
        num_cols = num_cols + 1
    
    num_rows = int(tam_list/num_cols)
    return num_rows, num_cols

def reshape_Array(townList,rows,cols):
    """
    Reconvierte el array que tenga la forma [rows,cols]
    """

    array_townList = np.array(townList)
    array_townList = np.reshape(array_townList,(rows,cols))

    return array_townList

def color_code(num_group):

    #Grupo 1 color azul
    if num_group == 1:
        return '#1151A7'
    #Grupo 2 color naranja
    elif num_group == 2:
        return '#F58216'
    #Grupo 3 color verde
    elif num_group == 3:
        return '#04A628'
    #Grupo 4 color rojo
    elif num_group == 4:
        return '#BC0E0E'

def get_labels_cols(num_cols, num_group):
    #Genera la tupla que contendrá el orden de las labels de las columnas para la tabla
    label = None
    #Si la tabla tendra 3 columnas
    if num_cols == 3:
        label = ('','Grupo ' + str(num_group), '')
    #Si la tabla tendra 2 o menos columnas
    elif num_cols < 3:
        label = ('Grupo ' + str(num_group), '')
    
    return label

if __name__ == '__main__':
    #graph_global_nulls(data_before_refill)
    while(True):
        etapa = int(input('0-Pre_Etapa\n1-Etapa_1\n2-Etapa_2\n3-Etapa_3\n4-Etapa_4\n5-Etapa_5\n6-Etapa_6\n'))
        graph_comparison(etapa)
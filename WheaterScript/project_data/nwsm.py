"""
NWSM: National Weather Service Method

Este archivo contiene el algoritmo que permite realizar la operación de relleno de datos
nulos en el dataset de clima, el algoritmo implementado es el llamado:

Método U.S. National Weather Service

El cual consiste en el calculo de variables faltantes con base en la información
de las estaciones colindantes, la formula es:

Vx = E(Vi * Wi) / E(Wi)

Donde:
E(): Es la suma de los i-elementos.

Vx: La variable a calcular en la x-estación, esta variable puede ser: PRECIP,EVAP,TMAX,TMIN.

Vi: La variable análoga a la que se desea calcular(Vx), pero en la i-esima estación, esta no
es nula.

Wi: También representada como 1/(Di)^2, se define como el cuadrado de la distancia inversa de la
i-esima estación a ser usada.
"""

from datetime import datetime

class NWSM(object):
    pass
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

def do_refill_data(towns_list, dates_list,testing):

    town_tf = towns_list[0] #Toma la TF ubicada en la primer posicion
    towns_tu = towns_list[1:] #Toma el resto de towns

    for data_date in dates_list:
        
        filtered_towns_tu = check_line_in_towns_touse(towns_tu,data_date)
        #Si hay suficientes TU  para llenar los datos
        if len(filtered_towns_tu)>1:
            
            index_for_tf = town_tf.index_date[data_date]
            #Si la fecha se encuentra en el índice
            if index_for_tf != None:
                line_tf = town_tf.content[index_for_tf]
                nulls_index_list = check_line_in_town_tofill(line_tf)
                
                if testing:
                    nulls_index_list = [1,2,3,4]

                new_data_for_line = refill_data(nulls_index_list,data_date,filtered_towns_tu)
                
                final_line = build_list_format_data(new_data_for_line,line_tf,nulls_index_list,data_date,testing)
                
                print(f'Result for date {data_date} data: {final_line} old_data: {line_tf}')
            else:
                
                new_data_for_line = refill_data([1,2,3,4],data_date,filtered_towns_tu)

                final_line =  build_list_format_data(new_data_for_line,[],[1,2,3,4],data_date,testing)

                print(f'Result for date {data_date} data: {final_line} old_data: {[]}')

def refill_data(nulls_index_list, data_date, filtered_towns_tu):

    """test = True
    if test:
        nulls_index_list = [1,2,3,4]"""
    new_data = []
    for null_index in nulls_index_list:
        data_for_param = [[town.content[town.index_date[data_date]][null_index], town.dist] for town in filtered_towns_tu \
            if town.content[town.index_date[data_date]][null_index] != 'Nulo']

        #Si 2 o más TU tienen el parametro requerido diferente de nulo
        if len(data_for_param)>1:
            new_data.append(nwsm(data_for_param))
        else:
            new_data.append('#Nulo')
    print(f'new_data:{new_data}')
    return new_data

def nwsm(params):
    
    """
    Recibe una lista de listas, con el parámetro a calcular para la TF con el sig formato:

    [[Vi,Di],[Vi+1,Di+1],...[Vn-1,Dn-1],[Vn,Dn]]

    Donde:

    Vi: es el valor de la variable en la i-esima TU
    Di: es el valor de la distancia entre la TF y la i-esima TU
    Vn: es el valor de la variable en la última TU
    Dn: es el valor de la distancia entre la TF y la última TU
    """

    get_w_value_lambda = lambda distance: 1/pow(distance,2)

    dividendo = 0
    divisor = 0
    #print(f'Ejecutando nwsm para: {params}')
    for param in params:
        w = get_w_value_lambda(float(param[1])) #Obtiene el valor Wi
        #print(f'w: {w}')
        dividendo += float(param[0]) * w   #E(Vi * Wi)
        divisor += w # E(Wi)
        #print(f'dividendo: {dividendo} divisor: {divisor}')

    #print(f'dividendo: {dividendo} divisor: {divisor}')
    #Sprint(f'dividendo/divisor: {dividendo/divisor}\n')
    return round(dividendo/divisor,1)

def clean_line(line):

    flag = True

    while flag:
        try:
            line.remove('Nulo')
        except:
            flag = False
            
    return line

def build_list_format_data(new_data,old_data,index_list,date,testing):
    
    #Si la línea a llenar no tiene la fecha
    if testing:
        new_data.insert(0,date)
        #print(f'buey2 {new_data} date2: {date} typedate: {type(date)}')
        return new_data

    if len(old_data) == 0:
        cleaned_data = [date]
    else:
        cleaned_data = clean_line(old_data)

    new_data_index = 0
    for index in index_list:
        cleaned_data.insert(index,new_data[new_data_index])
        new_data_index += 1

    return cleaned_data


def check_line_in_towns_touse(towns_tu,date):
    
    filtered_list_towns_tu = []
    for town in towns_tu:
        
        index_for_tu = town.index_date[date]
        if index_for_tu != None:
            filtered_list_towns_tu.append(town)

    #if len(filtered_list_towns_tu)<=1:
    #    return []
        #raise ValueError(f'La lista de ciudades tiene {len(filtered_list_towns_tu)} los cuales no suficientes elementos para continuar con el algoritmo: {filtered_list_towns_tu}')
        
    return filtered_list_towns_tu

def check_line_in_town_tofill(line):
    """
    Analiza la lista con formato [FECHA,PRECIP,EVAP,TMAX,TMIN], centrandose en los últimos 4 elementos
    para ver cuál de todos en nulo
    """

    nulls_index_list = [index for index in range(0,len(line)) if line[index] == 'Nulo']

    return nulls_index_list
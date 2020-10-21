"""
Este archivo contendrá todas las operaciones necesarias a realizar con fechas
"""
from datetime import datetime, timedelta

def generate_date_list(start_date, final_date):

    current_date_dt = string2datetime(start_date)
    final_date_dt = string2datetime(final_date)

    list_dates_str = []
    
    while(current_date_dt <= final_date_dt):

        list_dates_str.append(datetime2string(current_date_dt))
        current_date_dt = addDay2Date(current_date_dt)

    print(f'\nDates for search: {list_dates_str}')
    return list_dates_str

def subsDay2Date(date):
    adder = timedelta(days=1) #La variable permitira agregar un día a la fecha
    prev_date = date - adder #resta un día mas

    return prev_date

def addDay2Date(date):
    adder = timedelta(days=1) #La variable permitira agregar un día a la fecha
    next_date = date + adder #aumenta un día mas

    return next_date

def datetime2string(current_date):
    """
    Convierte una fecha datetime a un string en formato: dd/mm/aaaa
    """

    str_current_date = current_date.strftime('%x') #Regresa la fecha en string con formato: mm/dd/aaaa

    date_parts = str_current_date.split('/')
    date_rearranged = [date_parts[1],date_parts[0],"20"+date_parts[2]]

    return '/'.join(date_rearranged)
    
def string2datetime(current_date):
    """
    Convierte una fecha string con formato dd/mm/aaaa en su representacion en objeto datetime
    """
    
    date_parts = current_date.split('/')
    date_datetime = datetime(int(date_parts[2]),int(date_parts[1]),int(date_parts[0]))

    return date_datetime

def currentDayOlder_ThanDate(current_date,eval_date):

    #print(f'cd:{current_date} ed:{eval_date}')
    cast_to_int = lambda string: int(string)
    current_date_int = list(map(cast_to_int,current_date))
    eval_date_int = list(map(cast_to_int,eval_date))

    date1 = datetime(current_date_int[2],current_date_int[1],current_date_int[0])
    date2 = datetime(eval_date_int[2],eval_date_int[1],eval_date_int[0])

    #print(f'evaluando cd: {current_date_int} ed: {eval_date_int}')
    if date1>date2:
        #print('cd > ed')
        return True
    elif date1==date2:
        #print('cd == ed')
        return 'This'
    else:
        #print('cd < ed')
        return False


if __name__ == '__main__':

    generate_date_list('01/01/2008','31/03/2008')
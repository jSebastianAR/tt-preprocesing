from filechooser import Filechooser
from towns import get_distances_between_towns
from towns import build_towns, getValuesTown, find_index_forDate

dict_months_days = {'01':31,'02':[28,29],'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,\
    '11':30,'12':31}

leap_years = ['2008', '2012', '2016']

def build_date(day,month,year):

    return day+'/'+month+'/'+year

def main():
    fc = Filechooser()
    data_towns = get_distances_between_towns(fc.filechooser())
    towns_list = build_towns(data_towns)
    
    print(towns_list)
    print(f"Values town: {list(map(getValuesTown,towns_list))}")

    for town in towns_list:
        town.getContent()

    dates = fc.calendar()
    print(dates)

    for town in towns_list:
        print(f'Town: {town.name}')
        find_index_forDate(dates['from'],dates['to'],town.content)
    
    
if __name__ == '__main__':
    main()

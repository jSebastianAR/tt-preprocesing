from filechooser import Filechooser
from towns import get_distances_between_towns
from towns import build_towns, getValuesTown


def build_date(day,month,year):

    return day+'/'+month+'/'+year

def main():
    fc = Filechooser()
    data_towns = get_distances_between_towns(fc.filechooser())
    towns_list = build_towns(data_towns)
    
    print(towns_list)
    print(f"Values town: {list(map(getValuesTown,towns_list))}")

    dates = fc.calendar()
    print(dates)

    for town in towns_list:
        print(f'Town: {town.name}')
        town.getContent()
        town.find_index_forDate(dates['from'],dates['to'])

    
    
    
if __name__ == '__main__':
    main()

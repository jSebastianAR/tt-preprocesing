from filechooser import Filechooser
from towns import get_distances_between_towns
from towns import build_towns, getValuesTown
import dates as dt
from nwsm import do_refill_data
import time

def build_date(day,month,year):

    return day+'/'+month+'/'+year

def main():
    fc = Filechooser()
    data_towns = get_distances_between_towns(fc.filechooser())
    towns_list = build_towns(data_towns)
    
    #print(towns_list)
    print(f"Values town: {list(map(getValuesTown,towns_list))}")

    dates = fc.calendar()
    print(dates)

    for town in towns_list:
        print(f'Getting content for Town: {town.name}...')
        town.getContent()
        town.find_indexes_for_dates(dates['from'],dates['to'])
        time.sleep(.5)

    do_refill_data(towns_list, dt.generate_date_list(dates['from'],dates['to']),fc.testing)
if __name__ == '__main__':
    main()

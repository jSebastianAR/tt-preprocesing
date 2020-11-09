from filechooser import Filechooser
from towns import get_distances_between_towns
from towns import build_towns, getValuesTown
import dates as dt
from nwsm import do_refill_data
import time
from writerFile import Writer

def build_date(day,month,year):

    return day+'/'+month+'/'+year

def main():
    fc = Filechooser()
    data_towns = get_distances_between_towns(fc.filechooser())
    towns_list = build_towns(data_towns)
    town_tf = towns_list[0] #Toma la TF ubicada en la primer posicion
    #print(towns_list)
    print(f"Values town: {list(map(getValuesTown,towns_list))}")

    dates = fc.calendar()
    print(dates)

    for town in towns_list:
        print(f'Getting content for Town: {town.name}...')
        town.getContent()
        town.find_indexes_for_dates(dates['from'],dates['to'])
        time.sleep(.5)
    
    #Obtiene los nuevos datos con base en el algoritmo nwsm
    new_data = do_refill_data(towns_list, dt.generate_date_list(dates['from'],dates['to']),fc.testing)
    #Obtiene los indices donde se guardara la informacion nueva
    town_tf.get_start_index(dates['from'])
    #Inserta los nuevos datos en la lista final
    town_tf.refill_content(new_data)
    #Crea el escritor de archivos con base en el path de origen del archivo
    wrt = Writer(town_tf.path)
    #Crea un nuevo archivo y escribe todo el contenido
    wrt.newFile(town_tf.content)
if __name__ == '__main__':
    main()

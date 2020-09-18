import re
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename #Filechooser for one file
from tkinter.filedialog import askopenfilenames #Filechooser for multiple files

regex_lat = r'LATITUD[ ]+:(.*)°'
regex_lon = r'LONGITUD[ ]+:(.*)°'

def get_value(s,match):
    #print(f'{s}: {match}')
    match_splitted = match.split(' ')
    #print(match_splitted)
    return float(match_splitted[len(match_splitted)-1])

def get_lon_lat(file_path):

    with open(file_path,'r') as file:
        content = file.read()
        match_lat = re.findall(regex_lat,content)
        match_lon = re.findall(regex_lon,content)
        
        lat = get_value('Latitud',match_lat[0])
        lon = get_value('Longitud',match_lon[0])
        #print(f'Lat: {lat} Lon: {lon}')
        return [file_path,lat,lon]

class Filechooser(object):
    
    def __init__(self, *args, **kwargs):
        pass

    def filechooser(self):

        #Select files
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename_tofill = askopenfilename(initialdir='./CleanedData', title='Seleccione archivo a llenar información') # show an "Open" dialog box and return the path to the selected file
        files_touse = list(askopenfilenames(initialdir='./CleanedData', title='Seleccione archivos a a usar para llenar información')) # show an "Open" dialog box and return the path to the selected file

        #Get Lat and Lon of each town
        
        towntofill_latlon = get_lon_lat(filename_tofill)
        townstouse_latlon = list(map(get_lon_lat,files_touse))

        #print(f'Archivo a llenar: {filename_tofill}\n\nArchivos a usar para llenar: {files_touse}\n\n')
        #print(townstouse_latlon,towntofill_latlon)
        return {'tofill':towntofill_latlon,'touse':townstouse_latlon}


if __name__ == '__main__':

    chooser = Filechooser()
    result = chooser.filechooser()
    print(result)
import re
import tkinter as tk
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename #Filechooser for one file
from tkinter.filedialog import askopenfilenames #Filechooser for multiple files
from tkcalendar import Calendar, DateEntry
from tkinter import Label, Button
from datetime import datetime

regex_lat = r'LATITUD[ ]+:(.*)°'
regex_lon = r'LONGITUD[ ]+:(.*)°'

def refill_date(date):

    date_parts = date.split('/')
    date_parts[2] = "20"+date_parts[2]

    return '/'.join(date_parts)

def get_value(s,match):
    #print(f'{s}: {match}')
    match_splitted = match.split(' ')
    #print(match_splitted)
    return float(match_splitted[len(match_splitted)-1])

def get_lon_lat(file_path):

    with open(file_path,'r') as file:
        content = file.read()
        match_lat = re.findall(regex_lat,content) #Encuentra la latitud
        match_lon = re.findall(regex_lon,content) #Encuentra la longitud
        
        lat = get_value('Latitud',match_lat[0])
        lon = get_value('Longitud',match_lon[0])
        #print(f'Lat: {lat} Lon: {lon}')
        return [file_path,lat,lon]


class Filechooser(object):
    
    def __init__(self, *args, **kwargs):
        self.date_from = None
        self.date_to = None

    def grab_date(self,calendar,label,flag):
        
        date = refill_date(calendar.get_date())
        label.config(text=date)
        
        if flag:  
            self.date_from = date
        else:
            self.date_to = date

    def calendar(self):
        
        
        root = Tk() #Crea la ventana principal
        root.title('Get Date')
        root.geometry('500x700')

        mindate_date = datetime(2008,1,1) #Crea una variable del tipo datetime con param: Y:2008 M:1 D:1
        maxdate_date = datetime(2019,1,1) #Crea una variable del tipo datetime con param: Y:2019 M:1 D:1
        
        #Etiqueta de descripción para cal_from
        label_from = Label(root,text='Fecha de inicio')
        label_from.pack(pady=20)
        #label_from.pack(pady=20,padx=200, fill='x')

        #instancia de calendario para la fecha de inicio de llenado de datos y otra para la fecha de termino
        cal_from = Calendar(root, selectmode='day',year=2008, month=1, day=1, mindate=mindate_date ,maxdate=maxdate_date)
        cal_from.pack(pady=20)
        
        #Funcion para extraer las fechas seleccionadas
        grab_date_from_lambda = lambda : self.grab_date(cal_from,label_from,True)

        my_button_from = Button(root,text='Start date', command=grab_date_from_lambda)
        my_button_from.pack(pady=20)

        #Etiqueta de descripción para cal_to

        label_to = Label(root,text='Fecha de fin')
        label_to.pack(pady=20)
        
        #instancia de calendario para la fecha de termino
        cal_to = Calendar(root, selectmode='day',year=2008, month=1, day=1, mindate=mindate_date ,maxdate=maxdate_date)
        cal_to.pack(pady=20)
        
        #Funcion para extraer las fechas seleccionadas
        grab_date_to_lambda = lambda : self.grab_date(cal_to,label_to,False)

        my_button_to = Button(root,text='Final date', command=grab_date_to_lambda)
        my_button_to.pack(pady=20)

        the_button = Button(root,text='Finish', command = root.destroy)
        the_button.pack()
        root.mainloop()
        
        return {'from':self.date_from, 'to':self.date_to}
    """
    El filechooser permitira elegir el archivo con datos a llenar y los archivos a usar para llenar

    Retornara un diccionario con la siguiente info:

    {'tofill':[path,lat,lon],'touse':[[path,lat,lon,dist],[path,lat,lon,dist], ...]}

    donde: 
        tofill es la lista con la ciudad de los datos a llenar
        
        touse es la lista de listas, donde cada lista indexada es la info de las ciudades
        a usar para llenar la lista 'tofill'
    """

    def filechooser(self):

        #Select files
        root = Tk()
        root.withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename_tofill = askopenfilename(initialdir='../CleanedData', title='Seleccione archivo a llenar información') # show an "Open" dialog box and return the path to the selected file
        files_touse = list(askopenfilenames(initialdir='../CleanedData', title='Seleccione archivos a a usar para llenar información')) # show an "Open" dialog box and return the path to the selected file

        #Get Lat and Lon of each town
        
        towntofill_latlon = get_lon_lat(filename_tofill)
        townstouse_latlon = list(map(get_lon_lat,files_touse))

        #print(f'Archivo a llenar: {filename_tofill}\n\nArchivos a usar para llenar: {files_touse}\n\n')
        #print(townstouse_latlon,towntofill_latlon)
        root.destroy()
        return {'tofill':towntofill_latlon,'touse':townstouse_latlon}


if __name__ == '__main__':

    chooser = Filechooser()
    
    result = chooser.filechooser()
    print(result)
    
    dates = chooser.calendar()
    print(dates)
    #root.mainloop()
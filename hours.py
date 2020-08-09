def businessIsOpen(start,end,hour):

   HOURS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
   #current_hour = datetime.datetime.now().hour
   current_hour = hour
   if start=="undefined" or end=="undefined":
      return "undefined"
   else:
      
      start_index = HOURS.index(int(start))
      end_index   = HOURS.index(int(end),start_index+1)

      try:
         index_current_hour = HOURS.index(current_hour,start_index,end_index)
         print('Se ha encontrado la hora \n')
         return 'Open'
      except Exception as e:
         print('No se ha encontrado la hora \n')
         return 'Close'


if __name__ == '__main__':

   while True:
      i_hour = int(input('Ingresa la hora de apertura: '))
      l_hour = int(input('Ingresa la hora de cierre: '))
      e_hour = int(input('Ingresa la hora evaluada: '))
      businessIsOpen(i_hour,l_hour,e_hour)
FINAL_LINE_HEADER = 'FECHA'
import time
class Writer(object):
    
    def __init__(self,path):
        self.path_origin_file = path
        self.path_file = self.generate_path()
        self.header = []

    def generate_path(self):
        parts = self.path_origin_file.split('/')
        #Modificar el numero del path dependiendo de la etapa a ejecutar
        #path = '../Archivos_Etapa_6/'
        path = '../Archivos_Etapa_f1/'
        new_path = path + parts[len(parts)-1]
        return new_path

    def get_header_data(self):
        
        with open(self.path_origin_file, 'r', encoding = "utf-8") as file:
            #print(file)
            for line in file:
                """if 'PRECIP' in line:
                    line = '\t' + line
                elif 'FECHA' in line:
                    line = line[0:10] + '\t' + line[10:]"""
                self.header.append(line)
                #print(line)
                if FINAL_LINE_HEADER in line:
                    break

    def write_file(self,info):
        with open(self.path_file,'a+', encoding = "utf-8") as file:
            file.write(info)

    def newFile(self,content):

        self.get_header_data()
        #Writing header info
        for line in self.header:
            self.write_file(line)

        #Writing all wheater data
        for line_list in content:
            #Guarda solo la fecha
            final_list = [line_list[0]]
            #Obtiene los valores de las variables pero en string
            str_line_list = self.cast2string(line_list[1:])
            #Une la fecha con sus respectivos valores
            final_list.extend(str_line_list)
            str_line = '    '.join(final_list)
            self.write_file(str_line + '\n')
            #time.sleep(3)
        self.write_file('--------------------------------------\n')

    def cast2string(self,line):
        cast_str_lambda = lambda element: str(float(element)) if element!='Nulo' else element
        str_line = list(map(cast_str_lambda,line))
        return str_line

if __name__ == '__main__':

    wtr = Writer('../CleanedData/14002-ACATLAN DE JUAREZ.txt')
    wtr.newFile(['Nomanches\n','ese\n','buey\n'])
    
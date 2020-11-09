FINAL_LINE_HEADER = 'FECHA'
class Writer(object):
    
    def __init__(self,path):
        self.path_origin_file = path
        self.path_file = self.generate_path()
        self.header = []

    def generate_path(self):
        parts = self.path_origin_file.split('/')
        new_path = '../FilledData/'+parts[len(parts)-1]
        return new_path

    def get_header_data(self):
        
        with open(self.path_origin_file, 'r', encoding = "ISO-8859-1") as file:
            #print(file)
            for line in file:
                self.header.append(line)
                #print(line)
                if FINAL_LINE_HEADER in line:
                    break

    def write_file(self,info):
        with open(self.path_file,'a+', encoding = "ISO-8859-1") as file:
            file.write(info)

    def newFile(self,content):

        self.get_header_data()
        #Writing header info
        for line in self.header:
            self.write_file(line)

        #Writing all wheater data
        for line_list in content:
            str_line_list = self.cast2string(line_list)
            str_line = '    '.join(str_line_list)
            self.write_file(str_line + '\n')

    def cast2string(self,line):
        cast_str_lambda = lambda element: str(element)
        str_line = list(map(cast_str_lambda,line))
        return str_line

if __name__ == '__main__':

    wtr = Writer('../CleanedData/14002-ACATLAN DE JUAREZ.txt')
    wtr.newFile(['Nomanches\n','ese\n','buey\n'])
    
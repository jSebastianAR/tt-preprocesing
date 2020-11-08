FINAL_LINE_HEADER = 'FECHA'
class Writer(object):
    
    def __init__(self,path):
        self.path_origin_file = path
        self.path_file = self.generate_path()
        self.header = []

    def generate_path(self):
        parts = self.path_origin_file.split('/')
        new_path = '../FilledData/'+parts[2]
        return new_path

    def get_header_data(self):
        
        with open(self.path_origin_file, 'r', encoding = "ISO-8859-1") as file:
            #print(file)
            for line in file:
                self.header.append(line)
                #print(line)
                if FINAL_LINE_HEADER in line:
                    break
        
        print(self.header)

    def write_file(self,info):
        with open(self.path_file,'a+', encoding = "ISO-8859-1") as file:
            file.write(info)

    def newFile(self,content):

        #Writing header info
        for line in self.header:
            self.write_file(line)

        #Writing all wheater data
        
        for line in content:
            self.write_file(line)

if __name__ == '__main__':

    wtr = Writer('../CleanedData/14002-ACATLAN DE JUAREZ.txt')
    wtr.get_header_data()
    wtr.newFile(['Nomanches\n','ese\n','buey\n'])
    
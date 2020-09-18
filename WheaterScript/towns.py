from math import sin, cos, sqrt, atan2, radians

def get_distances_between_towns(dict_files):

    getDistances_lambda = lambda towntouse: getDistance(dict_files['tofill'][1],dict_files['tofill'][2],towntouse[1],towntouse[2])
    all_distances = list(map(getDistances_lambda,dict_files['touse']))
    
    print(all_distances)
    appendNewDistance_lambda = lambda current_list,index: current_list.append(all_distances[index])
    [appendNewDistance_lambda(townlist,dict_files['touse'].index(townlist)) for townlist in dict_files['touse']]
    
    print(f'final data: {dict_files}')

    return dict_files

def getDistance (latPointA, lonPointA, latPointB, lonPointB):

    radiusOfEarth = 6373.0

    lat1 = radians(latPointA)
    lon1 = radians(lonPointA)
    lat2 = radians(latPointB)
    lon2 = radians(lonPointB)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radiusOfEarth * c

    return round(distance,2)

def build_towns(data_towns):

    list_towns = []
    list_towns.append(Towns(data_towns['tofill'][0],data_towns['tofill'][1],data_towns['tofill'][2],0.0))

    num_towns = len(data_towns['touse'])
    for x in range(0,num_towns):
        new_town = Towns(data_towns['touse'][x][0],data_towns['touse'][x][1],data_towns['touse'][x][2],data_towns['touse'][x][3])
        list_towns.append(new_town)

    return list_towns

def getValuesTown(town):
    list_values = [town.path,town.lat,town.lon,town.dist,town.name,town.content,]
    return list_values

class Towns(object):
    
    
    def __init__(self, path, lat, lon, dist):
        self.path = path
        self.lat = lat
        self.lon = lon
        self.dist = dist
        self.content = []
        self.name = self.getNameTown(path)

    def getNameTown(self,path):

        data = path.split('/')
        return data[len(data)-1]

    def getContent(self):
        
        dataList = []
        getDailyData = lambda line: True if ('FECHA' in line) else False
        evaluateLine = lambda line,flag: dataList.append(line) if(flag) else False
        getData = False

        with open(self.path,'r',encoding = "ISO-8859-1") as file:

            for line in file:

                evaluateLine(line,getData)
                if getDailyData(line) and getData==False:
                    getData = True
        
        self.content = dataList
        print(f'Content for {self.name}: \n\n{self.content}')
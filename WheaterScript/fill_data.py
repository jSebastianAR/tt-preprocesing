from math import sin, cos, sqrt, atan2, radians
import re

regex_lat = r'LATITUD (.*)'
regex_lon = r'LONGITUD (.*)'

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

   return distance

def get_lon_lat(file_path):

    with open(file_path,'r') as file:
        content = file.read()
        match_lat = re.findall(regex_lat,content,re.DOTALL)
        match_lon = re.findall(regex_lon,content,re.DOTALL)
        
        lat = get_value(match_lat)
        lon = get_value(match_lon)

        return [lat,lon]

def get_value(match):

    match_splitted = match.split(' ')[2]
    return match_splitted[:len(match_splitted)-1]
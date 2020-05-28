import pandas as pd
import numpy as np
from operator import itemgetter


def saveArray(np_array,year):
	np.savetxt(str(year)+'_top_list.csv',np_array,delimiter = ',',fmt='%s')

def giveValues(data_top,year):

	d = {}
	d['year'] = year
	for i in range(0,data_top.size):
		d[data_top[i]] = i+1
	return d	

def getTop(year,data):
	index = year - 2008
	data_year = data[::,index]
	#print('\n\nYear %s'%(year))
	array2save = data_year.reshape((data_year.size,1))
	#print(array2save)
	#saveArray(array2save,year)
	data_top = giveValues(data_year,year)
	return data_top

def getProm(data,TOP_LIST):
	
	diccionary_prom = {}
	for key in data:
		number_of_years = 0
		if not key=='year':

			for top_list in TOP_LIST:
				if top_list.get(key):
					number_of_years += 1
					if diccionary_prom.get(key):
						diccionary_prom[key] = diccionary_prom[key] + top_list[key]
					else:
						diccionary_prom[key] = top_list[key]
				else:
					"""
					number_of_years += 1
					if diccionary_prom.get(key):
						diccionary_prom[key] = diccionary_prom[key] + 20
					else:
						diccionary_prom[key] = top_list[key]
					"""	
					print('Llave %s no encontrada en año %s'%(key,top_list['year']))
					
						
			diccionary_prom[key] = float(diccionary_prom[key]/number_of_years)
				
	return diccionary_prom		

def extract_data_money():

	doc = pd.read_excel('Productos Agrícolas.xlsx') #reading the data
	products = doc.head(10).values
	print(f"{products.shape} \n\n {products}")
	products = products[::,::2] #get only the product's name
	print(f"\n\n{products}")	

	return products

def extract_data():
	doc = pd.read_excel('Productos Agrícolas.xlsx') #reading the data
	#products = pd.DataFrame(doc,columns = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'])
	products = doc.head(20).values
	products = products[::,::2] #get only the product's name
	#print(products)	

	return products


def get_all_Top_lists():
	products = extract_data()
	TOP_LIST = []

	#Get all the top list between 2008-2018
	for i in range(2008,2019):
		TOP_LIST.append(getTop(i,products))

	for element in TOP_LIST:
		print(element)
		print()

	#Gets the average position for each product
	result = getProm(TOP_LIST[0],TOP_LIST)
	return result


def sort_elements(result):
	sortedResult = {}	
	print(result)
	#sortedResult = sorted(result.items(),key=itemgetter(1))
	#Sort the dictionary for value of position
	for key in sorted(result,key=result.get):
		sortedResult[key] = result[key]

	return sortedResult

def save_top_list(sortedResult):
	#Creates an array to save the result
	table = np.array(['Producto','Puntaje'])
	for key in sortedResult:
		new_row = np.array([key,sortedResult[key]])
		table = np.vstack([table,new_row])

	print(table[:21,:])

	#saveArray(table,'2008-2018')
	#print(sortedResult)
	#print(sortedResult.keys())


TOP_LIST = get_all_Top_lists()
sortedResult = sort_elements(TOP_LIST)
save_top_list(sortedResult)
#extract_data_money()
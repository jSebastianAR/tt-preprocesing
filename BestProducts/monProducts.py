import pandas as pd
import numpy as np
from operator import itemgetter

def get_all_products(TOP_LIST):

	list_products = []

	#Para todos los top de cada año
	for year_list in TOP_LIST: 

		#Para cada producto de cada top
		for key in year_list:
			if not(key == 'year'):
				#Si no se tiene el producto en el diccionario
				if not (key in list_products):
					list_products.append(key)


	print(f"products size: {len(list_products)}")
	return list_products

def saveArray(np_array,year):
	np.savetxt(str(year)+'_top_list.csv',np_array,delimiter = ',',fmt='%s')

def giveValues(data_top,year):

	d = {}
	d['year'] = year
	for i in range(0,data_top[0].size):
		d[data_top[0][i]] = data_top[1][i]
	return d	

def getTop(year,data,index):
	#index = year - 2008
	data_product = data[:,index-1]
	data_cash	 = data[:,index]
	print(f"product: {data_product} \n\n\n cash: {data_cash} \n")
	data_year = []
	data_year.append(data_product)
	data_year.append(data_cash)
	#print('\n\nYear %s'%(year))
	#array2save = data_year.reshape((data_year.size,1))
	#print(array2save)
	#saveArray(array2save,year)
	data_top = giveValues(data_year,year)
	return data_top

def getProm(all_products,TOP_LIST):
	
	diccionary_prom = {}
	for key in all_products:

		#number_of_years = 0

		for top_list in TOP_LIST:

			if top_list.get(key):

				#number_of_years += 1
				if diccionary_prom.get(key):

					diccionary_prom[key] = diccionary_prom[key] + top_list[key]

				else:

					diccionary_prom[key] = top_list[key]
			else:
				print('Llave %s no encontrada en año %s'%(key,top_list['year']))
				
					
		#diccionary_prom[key] = float(diccionary_prom[key]/number_of_years)
				
	return diccionary_prom		

def extract_data_money():

	doc = pd.read_excel('Productos Agrícolas.xlsx') #reading the data
	products = doc.head(100).values
	
	
	

	return products

def get_all_Top_lists():
	products = extract_data_money()
	TOP_LIST = []

	#Get all the top list between 2008-2018
	index = 1
	for i in range(2008,2019):
		TOP_LIST.append(getTop(i,products,index))
		index += 2

	for element in TOP_LIST:
		print(element)
		print()

	all_products = get_all_products(TOP_LIST)	
	#Gets the average position for each product
	result = getProm(all_products,TOP_LIST)
	return result


def sort_elements(result):
	sortedResult = {}	
	
	#sortedResult = sorted(result.items(),key=itemgetter(1))
	#Sort the dictionary for value of position
	for key in sorted(result,key=result.get, reverse=True):
		sortedResult[key] = result[key]

	print(sortedResult)	
	return sortedResult

def save_top_list(sortedResult):
	#Creates an array to save the result
	table = np.array(['Producto','Puntaje'])
	for key in sortedResult:
		new_row = np.array([key,sortedResult[key]])
		table = np.vstack([table,new_row])

	print(table[:21,:])

	#saveArray(table,'2008-2018-new')
	#print(sortedResult)
	#print(sortedResult.keys())



#extract_data_money()
result = get_all_Top_lists()
sortedResult = sort_elements(result)
save_top_list(sortedResult)
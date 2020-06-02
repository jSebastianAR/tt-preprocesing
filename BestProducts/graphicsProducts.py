import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib
import matplotlib.pyplot as plt

class Product(object):
	"""docstring for product"""
	def __init__(self, name):
		self.name_product 		= name
		self.position_per_year 	= {}
		self.sum_per_year		= {}

def extract_data_money():

	doc = pd.read_excel('Productos Agrícolas.xlsx') #reading the data
	products = doc.head(100).values
	return products

def get_top20():
	doc = pd.read_csv('New-2008-2018_top_list.csv') #reading the data
	products = doc.head(21).values[::,0]

	return products

def get_data_for_product(year,data,index,product):
	
	data_product = data[:,index-1]
	data_cash	 = data[:,index]
	
	if product.name_product == 'Arándano' and year==2008:
		product.position_per_year[year] = 123
		product.sum_per_year[year] 		= 0
	else:
		index_of_product = data_product.tolist().index(product.name_product) #Gets the index where is all the info of the product in both list(product and cash)
		#index_of_product = np.where(data_product == product.name_product) #Gets the index where is all the info of the product in both list(product and cash)
		product.position_per_year[year] = index_of_product + 1
		
		if year == 2008:
			product.sum_per_year[year] 	= data_cash[index_of_product]
		else:
			last_year = year - 1
			product.sum_per_year[year] 	= round(data_cash[index_of_product] + product.sum_per_year[last_year],2)
	
	
	return product

def get_all_Top_lists():
	products_info = extract_data_money() #gets all the info for all products in Jalisco
	products_list = get_top20() #gets the interested products 
	FINAL_LIST = []

	#Get all the top list between 2008-2018
	
	for product_name in products_list:
		index = 1
		product = Product(product_name)
		for i in range(2008,2019):
			product = get_data_for_product(i,products_info,index,product)
			index += 2
		#print(f"product: {product.name_product} data_pos: {product.position_per_year} data_cash: {product.sum_per_year} \n\n")
		FINAL_LIST.append(product)	
			
	return FINAL_LIST

def get_mark(index):

	markers_list = ["o",">","s","P"]

	if index <=4:
		index_marker = 0
	elif index>4 and index<=9:
		index_marker = 1
	elif index>9 and index<=14:
		index_marker = 2
	elif index>14:
		index_marker = 3

	return markers_list[index_marker]

def get_color(index):
	color_list = \
	["#808080","#000000","#FF0000","#800000","#FFFF00","#808000","#00FF00","#008000","#00FFFF","#D82A9E", \
	"#0000FF","#000080","#FF00FF","#800080","#73D5A2","#D24B4B","#FFAE20","#8A4303","#F9A7A7","#9F7ABD",]

	return color_list[index]

def turn_list_product(productObj,years_list):
	list_data_pos = []
	list_data_sum = []

	for year in years_list:
		list_data_pos.append(productObj.position_per_year[year])
		list_data_sum.append(productObj.sum_per_year[year])

	print(f"lists for {productObj.name_product} \n\n pos:{list_data_pos}\n\n sum:{list_data_sum}\n\n")	
	return [list_data_pos,list_data_sum]

def create_graphic(fig,title,xlabel,ylabel):
	graphic	= fig.add_subplot(1,1,1)
	graphic.set_title(title)
	graphic.set_xlabel(xlabel)
	graphic.set_ylabel(ylabel)

	return graphic

def customize_graphic(graphic,invert):

	if invert:
		graphic.invert_yaxis() #invert the values in y-axis
	
	leg = graphic.legend(loc = 'upper right',fontsize='x-small')
	plt.draw()
	# Get the bounding box of the original legend
	bb = leg.get_bbox_to_anchor().inverse_transformed(graphic.transAxes)

	# Change to location of the legend. 
	xOffset = .13
	#bb.x0 += xOffset
	bb.x1 += xOffset
	leg.set_bbox_to_anchor(bb, transform = graphic.transAxes)
	
	return graphic

def create_data_4plot():
	years_list = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
	products_list_info = get_all_Top_lists()

	fig_pos = plt.figure()
	fig_sum = plt.figure()
	
	graphic_pos = create_graphic(fig_pos,'Tabla de posicion de productos','Año','Posicion')
	graphic_sum = create_graphic(fig_sum,'Tabla de dinero generado por producto','Año','Dinero generado')
	
	index = 0
	num_product = 0
	for product in products_list_info:
		list_data_pos,list_data_sum = turn_list_product(product,years_list) #Turns the dicts data in list of data
		
		#Plot the list of data
		graphic_pos.plot(years_list[len(years_list)-5:len(years_list)],\
			list_data_pos[len(list_data_pos)-5:len(list_data_pos)],\
			label=product.name_product,color=get_color(index),marker=get_mark(num_product),markersize=8)
		
		graphic_sum.plot(years_list[len(years_list)-5:len(years_list)],\
			list_data_sum[len(list_data_sum)-5:len(list_data_sum)],\
			label=product.name_product,color=get_color(index),marker=get_mark(num_product),markersize=8)
		index += 1
		num_product += 1
	
	graphic_sum = customize_graphic(graphic_sum,False)	
	graphic_pos = customize_graphic(graphic_pos,True)
	
	plt.show()

create_data_4plot()

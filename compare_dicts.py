from operator import itemgetter

categories =	[{'Id': 2, 'Kind': 'Todos', 'KindDesc': 'Todos', 'KindImage': 'kindImages/todos.jpg'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 1, 'Kind': 'Polleria', 'KindDesc': 'Polleria', 'KindImage': 'kindImages/polleria.jpg'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 3, 'Kind': 'Tienda de Mascotas', 'KindDesc': 'Tienda de Mascotas', 'KindImage': 'kindImages/pets.png'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 1, 'Kind': 'Polleria', 'KindDesc': 'Polleria', 'KindImage': 'kindImages/polleria.jpg'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 3, 'Kind': 'Tienda de Mascotas', 'KindDesc': 'Tienda de Mascotas', 'KindImage': 'kindImages/pets.png'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 3, 'Kind': 'Tienda de Mascotas', 'KindDesc': 'Tienda de Mascotas', 'KindImage': 'kindImages/pets.png'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 2, 'Kind': 'Todos', 'KindDesc': 'Todos', 'KindImage': 'kindImages/todos.jpg'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				{'Id': 9, 'Kind': 'Cortes de Carne', 'KindDesc': 'Cortes de Carne', 'KindImage': 'kindImages/kitchen1.png'}, \
				]

#for categorie in categories:

print(f"Before filter \n")
for categorie in categories:
	print(categorie)


for categorie in categories:

	while categories.count(categorie)>1:
		categories.remove(categorie)

print(f"After filter \n")
for categorie in categories:
	print(categorie)	

print(f"After sort \n")
#names_to_filter = sorted([category['Kind'] for category in categories])
filtered_categories = [category for category in categories if category['Kind']=='Todos'] #First adds the categorie with kind=Todos
categories.remove(filtered_categories[0]) #removes "Todos" category

sorted_categories = sorted(categories, key=itemgetter('Kind'))
sorted_categories.insert(0,filtered_categories[0]) #adds the fisrt category("Todos")
for categorie in sorted_categories:
	print(categorie)	



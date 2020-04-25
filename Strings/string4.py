pumpsIsland = '1:1@2:1@3:2@4:2@5:3@6:3@7:4@8:4@9:5@10:5@'

list_one = pumpsIsland.split('@')
list_one.remove('')
print(list_one)
tam = len(list_one)
dict_islands = {}

for counter1 in range(0,len(list_one)):
	print('=============')
	data = list_one[0].split(':')
	island = data[1]
	print(f'Island:{island}')
	print('=============')
	list_island = []
	index_pair = 0
	for counter2 in range(0,len(list_one)):
		e = list_one[index_pair]#.split(':')
		e_splited = e.split(':')

		print(f"e:{e}")
		if e_splited[1]==island:
			list_island.append(e_splited[0])
			print(f"Pump {e_splited[0]} added to island {island}")
			list_one.remove(e)
		else:
			index_pair+=1

	print(list_one)		
	dict_islands[island] = list_island
	if len(list_one)==0:
		break;
			
print("Final result")
print(f"{dict_islands}")
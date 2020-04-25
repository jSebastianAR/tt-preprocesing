file = open('errores.txt',"r")
file2 = open('dict.txt',"w")

print('DICK_ERRORS_FLEETS = {')

for line in file:
	#print(f"{line}")
	key = "'"+line[:5]+"',"
	val = "'"+line[6:]+"',"
	#final_str = '\'' + key + '\':' + '\'' + val + '\','
	final_str = key + ':' + val
	print(f"{final_str}")
	file2.write(final_str+"\n")

print('}')
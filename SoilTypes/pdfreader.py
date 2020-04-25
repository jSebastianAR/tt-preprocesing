import PyPDF2
import re
import subprocess

# https://regex101.com/r/gOzhNn/2

#reg = r"([A-Z][a-z]*) ([0-9]+\.[0-9]*)"
reg = r"([A-Z][a-zñ]*) ([0-9]+\.[0-9]*)" #Allows get the ñ letter

def read_pdf(pdfs_list):
	for pdf in pdfs_list:
		print(f"PFD to read: {pdf}")
		try:
			pdfFileObj = open(pdf, 'rb')
			# pdf reader object
			pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			# a page object
			pageObj = pdfReader.getPage(7)
			name = get_name_pdf(pdf)
			write_file(pageObj.extractText(),name+'First.txt')
		except e:
			print(f"Cant read PDF because: "+e)

def static_reg():
	with open('AcaticFinal.txt','r') as file:
		data = file.read()
		print(f"data: {data}")
		final_result = re.findall(reg,data)
		print(f"Result with regex: {final_result}")

def reg_expression():
	txt_list = get_txt()
	for txt in txt_list:
		if 'Final' in txt:
			name = get_name_txt(txt)
			with open(txt,'r') as file:
				data = file.read()
				print(f"data: {data}")
				final_result = re.findall(reg,data)
				print(f"Result wit regex: {final_result}")
				for stype in final_result:
					soil = stype[0]
					percent = stype[1]
					write_file(soil+' '+percent+'\n','SoilTypes2/'+name+'SoilTypes.txt')
			delete_text_file(name,'Final')

def get_name_pdf(name_pdf):
	data = name_pdf.split('.pdf')[0].split('/')
	name = data[1]
	return name

def get_name_txt(name_txt):
	name = ''
	if 'First' in name_txt:
		data = name_txt.split('First.txt')
		name = data[0]
	elif 'Final' in name_txt:
		data = name_txt.split('Final.txt')
		name = data[0]
	return name

def write_file(data,name):
	with open(name,'a') as file:
		file.write(data)

def read_file():
	txt_list = get_txt()
	for txt in txt_list:
		name = get_name_txt(txt)
		print(f"Archivo a leer {txt}")
		with open(txt,'r') as file:
			getData = False
			for line in file:
				#print(f"{line}")
				if 'Tipo de suelo (%)' in line or 'Tipo de suelo' in line or 'Tipo' in line:
					getData = True
				elif 'Cobertura de suelo' in line or 'Cobertura de' in line or 'Cobertura' in line:
					break;
				elif getData==True:
					write_file(line.rstrip('\n'),name+'Final.txt')
		delete_text_file(name,'First')

def get_pdfs():
	result = subprocess.check_output('ls PDFs/*.pdf',shell=True).decode().split('\n')
	pdfs_list = result[:len(result)-1]
	print(f"PDFs: \n{pdfs_list}")
	return pdfs_list

def get_txt():
	result = subprocess.check_output('ls *.txt',shell=True)
	#print(f"result {result}")
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"TXT: \n{txt_list}")
	return txt_list

def check_if_exist(pdfs_list):
	for pdf in pdfs_list:
		#print(pdf)
		data = pdf.split('.pdf')[0].split('/')
		#print(data)
		name = data[1]
		delete_text_file(name,'Three')

def delete_text_file(name,both):
	try:
		if both=='Three':
			subprocess.call('rm -f '+name+'First.txt',shell=True)
			subprocess.call('rm -f '+name+'Final.txt',shell=True)
			subprocess.call('rm -f '+name+'SoilTypes.txt',shell=True)
		elif both=='First':
			subprocess.call('rm -f '+name+'First.txt',shell=True)
		elif both=='Final':
			subprocess.call('rm -f '+name+'Final.txt',shell=True)	

	except E:
		print(f"FileNotFound:"+E)



#Obtiene los pdfs
pdfs_list = get_pdfs()
#Elimina los archivos de texto si existen
check_if_exist(pdfs_list)
#Lee los archivos y obtiene la página donde está la info
read_pdf(pdfs_list)
#Obtiene la info de la página
read_file()
reg_expression()
#static_reg()

#reg = r"([A-Z][a-z]*)\n( )\n(.*)"
#reg = r"([A-Z][a-z]*)\n( )\n([0-9]+\.[0-9]*)"






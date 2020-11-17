import subprocess
from pathlib import Path
import time
import json
import pickle

def get_txt():
	result = subprocess.check_output('ls CleanedData/*.txt',shell=True)
	txt_list = result.decode().split('\n')
	txt_list = txt_list[:len(txt_list)-1]
	print(f"{len(txt_list)} Archivos a leer \nTXT: \n{txt_list}")
	return txt_list

def build_path(name_file):
	root = Path('').resolve().as_posix()
	final_path = root + '/' + name_file
	print(final_path)
	return final_path

def get_name_txt(txt):
	parts = txt.split('/')
	name = parts[len(parts)-1]
	return name

def dump_file(data,name):
	with open(name, "wb") as a_file:
		pickle.dump(data, a_file, protocol=pickle.HIGHEST_PROTOCOL)
		a_file.close()

def get_dump(name):

	with open(name, "rb") as a_file:
		output = pickle.load(a_file)
		print(output)
		return output

if __name__ == '__main__':
	
	#dump_file(0,'key.pickle')
	get_dump('key.pickle')

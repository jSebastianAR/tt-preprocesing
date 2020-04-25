import cv2
import sys
import os

def read_img(path):
	return cv2.imread(path)

def resize_img(img,size):
	re_img = cv2.resize(img,size)
	return re_img 

def save_reimg(img,name):
	current_path = os.getcwd()
	print(name+'.jpg')
	cv2.imwrite(current_path,img)

def split_size(param):
	l = []
	for element in param.split("x"):
		l.append(int(element))
		
	return tuple(l)

def split_path(param):
	l = param.split('/')
	return l[len(l)-1]

def split_name(name):
	return name.split('.jpg')[0]

def main(params):
	img = read_img(params[1])
	size = split_size(params[2])
	print(size)
	re_img = resize_img(img,size)
	name = split_name(split_path(params[1]))
	save_reimg(re_img,name)

main(sys.argv)

#pip install googletrans

import googletrans

def translate_word(word,flag):
	translator = Translator()

	if flag:
		fuente 	= 	"es"
		destino	=	"en" 
	else:
		fuente 	= 	"en"
		destino	=	"es" 
	
	return translator.translate(word,src=fuente,dest=destino).text


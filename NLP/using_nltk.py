"""
Librerías a instalar

pip install nltk
pip install inflector


Descargar el tagger para español de la universidad de Standford desde:
https://nlp.stanford.edu/software/tagger.shtml#Download
"""

#NLTK
import nltk
from nltk.tag import StanfordPOSTagger
"""
	Primero se debe descargar el tokenizer punkt y averaged_perceptron_tagger

	1-Se descomentan y ejecuta el script o desde la consola de python pueden ejecutarse(dentro del viertual env deseado)
	
	2-Solo se deben ejecutar una vez, después de ello se pueden volver a comentar
"""
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#TAGGER IN SPANISH FOR NLTK
"""
	Una vez desgargado el tagger de Standfor se descomprime y se busca el .tagger en español y el .jar

	El .jar se encuentra ubicado normalmente en la carpeta base del archivo descargado
	El .tagger se encuentra dentro de la carpeta models y debe tener un nombre tipo "spanish.tagger"
	
	*Se tienen que cambiar al directorio donde está almacenado el archivo .tagger y .jar si se usa el script en otro equipo*
"""

tagger="spanish-ud.tagger" 
jar="stanford-postagger-4.0.0.jar"

#Inflector for plural or singular words
import inflector

def get_noun(text):

	#Tokenizando

	tokenized_text = nltk.word_tokenize(text,language="spanish")
	
	#Etiquetando el tipo de palabra

	spanish_postagger = StanfordPOSTagger(tagger,jar)
	pos_tagged = spanish_postagger.tag(tokenized_text)
	nouns_list = []

	print(f"Lista: {pos_tagged} len: {len(pos_tagged)}")

	if len(pos_tagged) > 1:
		flag = False
		for tag_tuple in pos_tagged: #Busca en cada tag
			if tag_tuple[1] == 'VERB': #Si es un verbo
				flag = True #activa la bandera

			if flag == True and tag_tuple[1] == 'NOUN': #busca un sustantivo después de un verbo
				nouns_list.append(tag_tuple)
				

		finded_word = nouns_list[len(nouns_list)-1][0]	#Obtiene el último noun

	else:
		finded_word = pos_tagged[0][0]
		#print(f"word:{tag_tuple[0]} type:{tag_tuple[1]}")
	
	result = isplural(finded_word)
	
	return result

def isplural(word):
	ift = inflector.Spanish() #Instancia la clase que pluraliza y singulariza

	list_patterns = []
	list_patterns.append(word.lower())
	
	singular_word = ift.singularize(word) #Convierte a singular la palabra recibida
	
	if singular_word == word: #Si el resultado es el mismo, es singular

		plural_word = ift.pluralize(word) #Obtiene el plural de la palabra en ingles
		list_patterns.append(plural_word.lower()) #Agrega la palabra en plural
	else: #Sino es plural

		list_patterns.append(singular_word.lower()) #Agrega la palabra en singular

	
	return list_patterns

sentence = input("Ingresa la frase de busqueda: ")

print(f"Frase obtenida: {sentence}")
result = get_noun(sentence)
print(f"Se buscará: {result}")
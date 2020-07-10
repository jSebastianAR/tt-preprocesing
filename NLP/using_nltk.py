"""
Librerías a instalar

pip install nltk
pip install inflector


Descargar el tagger para español de la universidad de Standford desde:
https://nlp.stanford.edu/software/tagger.shtml#Download
"""

#Inflector for plural or singular words
import inflector

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



TERMINACIONES_ESPAÑOL_DIMINUTIVOS = {

"CASE_1":{"terminacion":("e","i","u","n","r"), "sufijo_diminutivo":("cito","cita","citos","citas")},
"CASE_2":{"terminacion":("a","o","ia","io"), "sufijo_diminutivo":("ito","ita","itos","itas")},
"CASE_3":{"terminacion":("b","c","d","f","g","h","j","k","l","m","ñ","p","q","s","t","v","w","x","y","z"),\
											 "sufijo_diminutivo":("ito","ita","itos","itas")}
}

def isDiminutive(noun):

	ift = inflector.Spanish()
	results = []

	for case in TERMINACIONES_ESPAÑOL_DIMINUTIVOS: #busca por cada caso

		if (case == "CASE_2" or case == "CASE_3") and noun.endswith(TERMINACIONES_ESPAÑOL_DIMINUTIVOS[case]["sufijo_diminutivo"]):

			#Si es singular
			if ift.singularize(noun) == noun:
				n_words_to_delete = 3 #palabras del diminutivo a quitar
				n_words_to_concat = 1 #palabras a agregar para el caso 1
			else:#es plural
				n_words_to_delete = 4
				n_words_to_concat = 2

			#Extrae la palabra exceptuando las últimas tres palabras(terminación del diminutivo) y concatenando la última palabra del noun
			word_in_first_case = noun[:len(noun)-n_words_to_delete] + noun[len(noun)-n_words_to_concat] 
			results.append(word_in_first_case)
			#Extrae la palabra eliminando la terminación en diminutivo
			word_in_third_case = noun[:len(noun)-n_words_to_delete] 
			results.append(word_in_third_case)

			break;

		elif case == "CASE_1" and noun.endswith(TERMINACIONES_ESPAÑOL_DIMINUTIVOS[case]["sufijo_diminutivo"]):

			#Extrae el noun omitiendo la terminación del diminutivo
			word_in_second_case = noun[:len(noun)-4]
			results.append(word_in_third_case)

			break;

		#No está en diminutivo	
		else:
			results.append(noun)
			break;


	return results		

def search4last_verb(pos_tagged):

	nouns_list = []
	flag = False
	for tag_tuple in pos_tagged: #Busca en cada tag

		if tag_tuple[1] == 'VERB': #Si es un verbo
			flag = True #activa la bandera

		if flag == True and tag_tuple[1] == 'NOUN': #busca un sustantivo después de un verbo
			nouns_list.append(tag_tuple)

	return nouns_list		

def get_noun(text):

	#Tokenizando

	tokenized_text = nltk.word_tokenize(text,language="spanish")
	
	#Etiquetando el tipo de palabra

	spanish_postagger = StanfordPOSTagger(tagger,jar)
	pos_tagged = spanish_postagger.tag(tokenized_text)
	nouns_list = []

	print(f"Lista: {pos_tagged} len: {len(pos_tagged)}")

	try:
		if len(pos_tagged) > 1:
			
			nouns_list = search4last_verb(pos_tagged)#Busca un noun después del último verbo en la frase
					
			if len(nouns_list) > 0:	#Si encontro nouns por verbos

				finded_word = nouns_list[len(nouns_list)-1][0]	#Obtiene el último noun
				print(f"RESULTADO DE NOUNS POR VERBOS: {finded_word}")
			else:#sino buscara todos los nouns

				nouns_list = [tag_tuple for tag_tuple in pos_tagged if tag_tuple[1]=='NOUN']
				
				if len(nouns_list) == 0: #Si no encontro ningun noun
					return "No se ha entendido la peticion"
				else:
					finded_word = nouns_list[len(nouns_list)-1][0]	#Obtiene el último noun
					print(f"RESULTADO DE BUSCAR TODOS LOS NOUNS: {finded_word}")

		elif len(pos_tagged)==1: #and pos_tagged[0][1]=='NOUN':

			finded_word = pos_tagged[0][0]
			print(f"RESULTADO DE SOLO UNA PALABRA: {finded_word}")
			#print(f"word:{tag_tuple[0]} type:{tag_tuple[1]}")

		list_finded_words = isDiminutive(finded_word)
		print(f"DESPUES DEL ANALISIS DE DIMINUTIVOS: {list_finded_words}")
		result = isplural(list_finded_words) #obtiene el plural de la palabra

	except: 

		result = ["Todo","Todos"]
	
	
	return result

def isplural(words):
	ift = inflector.Spanish() #Instancia la clase que pluraliza y singulariza

	list_patterns = []

	for word in words:

		list_patterns.append(word.lower())
		
		singular_word = ift.singularize(word) #Convierte a singular la palabra recibida
		
		if singular_word == word: #Si el resultado es el mismo, es singular

			plural_word = ift.pluralize(word) #Obtiene el plural de la palabra en ingles
			list_patterns.append(plural_word.lower()) #Agrega la palabra en plural
		else: #Sino es plural

			list_patterns.append(singular_word.lower()) #Agrega la palabra en singular

		#print(list_patterns)
	return list_patterns

def main():

	while True:

		sentence = input("Ingresa la frase de busqueda: ")

		print(f"Frase obtenida: {sentence}")
		result = get_noun(sentence)
		print(f"Se buscará: {result} \n")

main()
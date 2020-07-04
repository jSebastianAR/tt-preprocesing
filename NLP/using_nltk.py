#NLTK
import nltk
from nltk.tag import StanfordPOSTagger
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')


#TAGGER IN SPANISH FOR NLTK
tagger="/home/jsebastian-ar/Descargas/stanford-tagger-4.0.0/models/spanish-ud.tagger"
jar="/home/jsebastian-ar/Descargas/stanford-tagger-4.0.0/stanford-postagger-4.0.0.jar"

"""
#SPACY
#Import Tokenizer and tagger in spanish for spacy
import spacy 
## python -m spacy download es_core_news_sm
"""

#Inflect for plural or singular words
import inflect


#Google translate
from googletrans import Translator

def get_verb_word_tokenize(audiototext):

	#Tokenizando

	tokenized_text = nltk.word_tokenize(audiototext,"spanish")
	
	#Etiquetando el tipo de palabra

	spanish_postagger = StanfordPOSTagger(tagger,jar)
	pos_tagged = spanish_postagger.tag(tokenized_text)

	flag = False
	for tag_tuple in pos_tagged: #Busca en cada tag
		if tag_tuple[1] == 'VERB': #Si es un verbo
			flag = True #activa la bandera

		if flag == True and tag_tuple[1] != 'VERB': #busca un sustantivo después de un verbo

			finded_word = tag_tuple[0]
			break
		
		#print(f"word:{tag_tuple[0]} type:{tag_tuple[1]}")
	
	result = isplural(finded_word)

	return result

def get_verb_spacy(text):

	nlp = spacy.load("es_core_news_sm")
	tokenizer = nlp.Defaults.create_tokenizer(nlp)
	result = nlp(text)
	for token in result:
		print(token.pos_)

	#print(f"Result with spacy: {result}")

def isplural(word):
	ift = inflect.engine()

	list_patterns = []
	list_patterns.append(word)

	flag = ift.singular_noun(translate_word(word,True)) #Traduce de español a ingles para saber si es singular o plural

	if flag is False: #Si flag es falso, es singular
		plural_word 	= ift.plural(translate_word(word,True)) #Obtiene el plural de la palabra en ingles
		list_patterns.append(translate_word(plural_word,False))
	else: #Sino es plural
		singular_word 	= ift.singular_noun(translate_word(word,True)) #Obtiene el singular de la palabra en ingles
		list_patterns.append(translate_word(singular_word,False))

		return list_patterns

def translate_word(word,flag):
	translator = Translator()

	if flag:
		fuente 	= 	"es"
		destino	=	"en" 
	else:
		fuente 	= 	"en"
		destino	=	"es" 

	return translator.translate(word,src=fuente,dest=destino).text


sentence = "busca quiero necesitar buscar vinos"

print(get_verb_word_tokenize(sentence))

#get_verb_spacy(sentence)
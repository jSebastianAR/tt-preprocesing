#SPACY
#Import Tokenizer and tagger in spanish for spacy
import spacy 
## python -m spacy download es_core_news_sm

def get_verb_spacy(text):

	nlp = spacy.load("es_core_news_sm")
	tokenizer = nlp.Defaults.create_tokenizer(nlp)
	result = nlp(text)
	for token in result:
		print(token.pos_)

	print(f"Result with spacy: {result}")
import re
import random

regex_alphanumeric  = r'[a-zA-Z]*[0-9]*[A-Za-z0-9]+'
regex_alphanumeric2 = r'([a-zA-Z]*[0-9]*[A-Za-z0-9]+)'
regex_nonalphanumeric = r'[^ &&\w]'

list_static = ["Rodeo Cruzeli'z pizza","R½od#eo Cruzeli'z pizz4","#H3ll0 w0lrd<<<","Bue$yyyyy n00&00/0-00"]
static_word = "Rodeo Cruzeli'z pizza"
#static_word = "RodeoCruzeli'zpizza"

def analize_pattern(pattern):

    print(f"Pattern: {pattern}")
    r1 = re.findall(regex_nonalphanumeric,pattern)
    if r1:
        print(f"Caracteres no alfanumericos encontrados:{r1}")    
        cleaned_pattern = re.sub(regex_nonalphanumeric,'',pattern)
        print(f"Cadena limpia:{cleaned_pattern}")    
    
    return cleaned_pattern

def get_random():
    random_value = random.randint(0,len(list_static)-1)

    return list_static[random_value]

if __name__ == '__main__':
    analize_pattern(get_random())

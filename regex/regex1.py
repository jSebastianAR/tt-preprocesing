import re

REGEX_SEQUENCES = r'(\d+)$'

def delete_match(string):
	return re.sub(REGEX_SEQUENCES,'',string)


def check_match(string):

	if re.search(REGEX_SEQUENCES,string):
		return delete_match(string)
	else:
		return string
			
def main():

	while True:
		string = input('Ingrese cadena: ')
		result = check_match(string)
		print(f"El resultado fue {result}\n")

if __name__ == '__main__':
	main()

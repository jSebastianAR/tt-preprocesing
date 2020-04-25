class estacion(object):

	def __init__(self):
		self.param1 = 1
		self.param1 = 'A'
		self.param3 = 'Hola'
		self.param4 = {'1':1,'2':2}

	def getValues(self):
		return self



def main():

	station = estacion

	for element in station:
		print('param1'%(element.param1))
		print('param2'%(element.param2))
		print('param3'%(element.param3))
		print('param4'%(element.param4))

main()
from datetime import datetime
	def obtenir_temps():
		return "Hello ! Il est {}.".format(datetime.now().strfime("%H:%M:%S"))

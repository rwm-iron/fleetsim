from powerplants.powerplant import PowerPlant

class NukePlant(PowerPlant):
	"""
	Extends PowerPlant and implements the concrete subclass NukePlant.
	"""

	def __init__(self, identifier: str):
		super().__init__(identifier)
		print("%s %s: object created" % (self.__class__.__name__, self._identifier))

	def __repr__(self):
		return "%s" % (str(self.__class__.__name__) + " " + self._identifier) 

	def lightoff_plant(self):
		print ("%s %s: The reactor is critical. Ready to answer all bells." % (self.__class__.__name__, self._identifier))

	def shutdown_plant(self):
		print ("%s %s: The control rods are seated and the reactor is not critical." % (self.__class__.__name__, self._identifier))


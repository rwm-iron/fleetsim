from powerplants.powerplant import PowerPlant

class SteamPlant(PowerPlant):
	"""
	Extends PowerPlant and implements the concrete subclass SteamPlant.
	"""

	def __init__(self, identifier: str):
		super().__init__(identifier)
		print("%s %s: object created" % (self.__class__.__name__, self._identifier))

	def __repr__(self):
		return "%s" % (str(self.__class__.__name__) + " " + self._identifier) 

	def lightoff_plant(self):
		print ("%s %s: The boilers have a head of steam. Ready to answer all bells." % (self.__class__.__name__, self._identifier))

	def shutdown_plant(self):
		print ("%s %s: The boilers are shut down. The steam plant is cold and dark." % (self.__class__.__name__, self._identifier))


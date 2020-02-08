from abc import ABC, abstractmethod

class PowerPlant(ABC):
	"""
	Defines the interface for a PowerPlant object.
	"""
	def __init__(self, identifier: str):
		self._identifier = str(identifier)
		print("%s %s: base class object created" % (self.__class__.__bases__[0].__name__, self._identifier))

	@abstractmethod
	def lightoff_plant(self):
		pass

	@abstractmethod
	def shutdown_plant(self):
		pass

	@abstractmethod
	def __repr__(self):
		return (str(self.__class__) + " " + self._identifier)


from abc import ABC, abstractmethod

class Weapon(ABC):
	"""
	Defines the interface for a Weapon object.
	"""
	def __init__(self, identifier: str):
		self._identifier = str(identifier)
		print("%s %s: base class object created" % (self.__class__.__bases__[0].__name__, self._identifier))

	@abstractmethod
	def aim(self):
		print("%s: aim() method called." % (self.__class__.__bases__[0].__name__))

	@abstractmethod
	def fire(self):
		pass

	@abstractmethod
	def __repr__(self):
		return "%s" % (str(self.__class__) + " " + self._identifier) 

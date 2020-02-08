from abc import ABC, abstractmethod
from powerplants.powerplant import PowerPlant
from weapons.weapon import Weapon


class Vessel(ABC):
	"""
	Defines the interface for a Weapon object.
	"""
	def __init__(self, identifier: str, weapon: Weapon, powerplant: PowerPlant):
		self._identifier = identifier
		self._weapon = weapon
		self._powerplant = powerplant
		print("%s %s: base class object created" % (self.__class__.__bases__[0].__name__, self._identifier))

	@abstractmethod
	def aim(self):
		print("%s: aim() method called..." % (self.__class__.__bases__[0].__name__))

	@abstractmethod
	def fire(self):
		pass

	@abstractmethod
	def lightoff_plant(self):
		pass

	@abstractmethod
	def shutdown_plant(self):
		pass

	@abstractmethod
	def __repr__(self):
		return "%s" % (self.__class__.__name__ + " " + self._identifier)

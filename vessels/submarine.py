from powerplants.nukeplant import NukePlant
from weapons.torpedo import Torpedo
from vessels.vessel import Vessel


class Submarine(Vessel):
	"""
	Extends Vessel and implements the concrete subclass Submarine.
	"""
	def __init__(self, identifier: str):
		super().__init__(identifier=identifier, weapon=Torpedo("MK-48 Advanced Capability"), powerplant=NukePlant("Liquid Metal"))
		print( "%s %s: object created" % (self.__class__.__name__, self._identifier))

	def __repr__(self):
		return (str(self.__class__.__name__) + " " + self._identifier)

	def aim(self):
		super().aim()
		self._weapon.aim()

	def fire(self):
		self._weapon.fire()

	def lightoff_plant(self):
		self._powerplant.lightoff_plant()

	def shutdown_plant(self):
		self._powerplant.shutdown_plant()


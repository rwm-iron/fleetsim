from powerplants.steamplant import SteamPlant
from weapons.fiveinchgun import FiveInchGun
from vessels.vessel import Vessel


class Destroyer(Vessel):
	"""
	Extends Vessel and implements the concrete subclass Destroyer.
	"""
	def __init__(self, identifier: str):
		super().__init__(identifier=identifier, weapon=FiveInchGun("MK45-Mod4"), powerplant=SteamPlant("1200PSI"))
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


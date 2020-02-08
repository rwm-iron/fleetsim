from weapons.weapon import Weapon

class FiveInchGun(Weapon):
	"""
	Extends Weapon and implements the concrete subclass FiveInchGun.
	"""

	def __init__(self, identifier: str):
		super().__init__(identifier)
		print("%s %s: object created" % (self.__class__.__name__, self._identifier))

	def __repr__(self):
		return (str(self.__class__) + " " + self._identifier)

	def aim(self):
		super().aim()
		print ("%s %s: Elevation set. Locked and loaded!" % (self.__class__.__name__, self._identifier))

	def fire(self):
		print ("%s %s: Blam!" % (self.__class__.__name__, self._identifier))

from weapons.weapon import Weapon

class Torpedo(Weapon):
	"""
	Extends Weapon and Implements a concrete subclass named Torpedo.
	"""

	def __init__(self, identifier: str):
		super().__init__(identifier)
		print("%s %s: object created" % (self.__class__.__name__, self._identifier))

	def __repr__(self):
		return (str(self.__class__) + " " + self._identifier)

	def aim(self):
		super().aim()
		print ("%s %s: The torpedo has the solution and is ready to fire." % (self.__class__.__name__, self._identifier))

	def fire(self):
		print ("%s %s: Swish! Torpedo away!" % (self.__class__.__name__, self._identifier))

from vessels.submarine import Submarine
from vessels.destroyer import Destroyer




def main():
	uss_norfolk = Submarine("USS Norfolk (SSN-714)")
	print('*' * 60)
	uss_norfolk.lightoff_plant()
	uss_norfolk.aim()
	uss_norfolk.fire()
	uss_norfolk.shutdown_plant()
	print('*' * 60)
	uss_johnpauljones = Destroyer("USS John Paul Jones (DDG-53)")
	uss_johnpauljones.lightoff_plant()
	uss_johnpauljones.aim()
	uss_johnpauljones.fire()
	uss_johnpauljones.shutdown_plant()
	


if __name__ == '__main__':
	main()
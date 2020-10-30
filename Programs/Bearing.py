from sense_hat import SenseHat


import time



while True:
	b = SenseHat().get_compass()

	print("\nBearing: {:.2f}deg to North".format(b))

	time.sleep(2)
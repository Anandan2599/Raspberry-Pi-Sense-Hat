from sense_hat import SenseHat
import time

SenseHat().clear()

color = [ 0, 0, 255]

while True:
    t = SenseHat().temperature
    temperature_disp = "{:.2f}*C".format(t)

    SenseHat().show_message( temperature_disp, text_colour = color)
    time.sleep(2)
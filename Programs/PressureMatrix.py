from sense_hat import SenseHat
import time

SenseHat().clear()

color = [ 0, 0, 255]

while True:
    p = SenseHat().pressure
    pressure_disp = "{:.3f}bar".format(p/1000)

    SenseHat().show_message( pressure_disp, text_colour = color)
    time.sleep(2)
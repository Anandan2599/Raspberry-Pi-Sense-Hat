from sense_hat import SenseHat
import time

SenseHat().clear()

color = [ 0, 0, 255]

while True:
    h = SenseHat().humidity
    humidity_disp = "{:.2f}%".format(h)

    SenseHat().show_message( humidity_disp, text_colour = color)
    time.sleep(2)
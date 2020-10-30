0from sense_hat import SenseHat
import time

SenseHat().set_imu_config( True, True, True)

while True:
    o = SenseHat().get_orientation()
    p = o["pitch"]
    y = o["yaw"]
    r = o["roll"]
    if p > 180:
        p = p - 360
    if y > 180:
        y = y - 360
    if r > 180:
        r = r - 360
    print("\nPitch(deg): {:.2f}\tYaw(deg): {:.2f}\tRoll(deg): {:.2f}" .format( p, y, r))
    time.sleep(2)
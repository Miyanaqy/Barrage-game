import math


def Angle(pos, epos):
    x = epos[0] - pos[0]
    y = epos[1] - pos[1]
    c = math.sqrt(x**2 + y**2)
    sina = y / c
    angle = math.asin(sina) * 180 / math.pi
    if x < 0:
        return (180 - angle)
    else:
        return angle

def Speed(angle):
    xsp = 6 * math.cos(angle * math.pi/180)
    ysp = 6 * math.sin(angle * math.pi/180)
    speed = [xsp, ysp]
    return speed

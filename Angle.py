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

def Speed(angle, s=6):
    xsp = s * math.cos(angle * math.pi/180)
    ysp = s * math.sin(angle * math.pi/180)
    speed = [xsp, ysp]
    return speed

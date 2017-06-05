import math
def distance(pos,opos):
    a = abs(opos[0] - pos[0])
    b = abs(opos[1] - pos[1])
    c = math.sqrt(a**2 + b**2)
    return c

def collision(sprite1,sprite2):
    dis = distance(sprite1.rect.center, sprite2.rect.center)
    if dis < (sprite1.rect.width/2 + sprite2.rect.width/2 ):
        return True
    else:
        return False

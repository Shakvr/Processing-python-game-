from math import*

def collision(p,o):
    if sqrt((o['x']-p['x'])**2+ (o['y']-p['y'])**2)>5 :
        return False
    else:
        return True
    

from random import randint


def position_depart():
    y_depart=[]
    taille_couloir=height/6
    y1=taille_couloir/2
    for i in range(0,6):
        y_depart.append(y1+i*taille_couloir)
    return y_depart
# y_depart=position_depart()
    
def obstacle():
    y_depart=position_depart()
    taille_couloir=height/6
    y1=taille_couloir/2
    for i in range(0,6):
        y_depart.append(y1+i*taille_couloir)
    b={}
    b['r']=20
    b['x']=width-b['r']
    b['y']=y_depart[randint(0,6)]   
    b['vx']=randint(1,9)
    b['vy']=randint(1,3)
    b['cr']=randint(0,255)
    b['cv']=randint(0,255)
    b['cb']=randint(0,255)
    return b

def avancer_obstacle(b):
    b['x']=b['x']-b['vx']
    
    
def afficher_obstacle(b,ob):
    image(ob,b['x'],b['y'])


def creer_obstacle():
    if keyPressed:
        if key==' ':
            return True
        
def atteint_limite(b):
    if b['x'] < 0-b['r']:
        return True 

from son import*

def accueil():
    global aim
    aim=loadImage("menu.png")
    background(aim)
    textSize(40)
    fill(255, 255, 255)
    text("negro ",width/2,height/2.75)
    textSize(32)
    if bouton(width/2,2*height/3,200,60,'Commencer'):
        play_sound()
        return "commencer"


def bouton(x,y,largeur,hauteur,texte):
    if  x-largeur/2< mouseX < x + largeur/2 and  y - hauteur/2< mouseY < y + hauteur/2 :
        fill (140,90,190)
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.2)
        if mousePressed :
            return True
    else:
        fill (100,70,170)
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.2)
    return False

def fin():
    global fim
    fim=loadImage("deathscreen .png")
    background(fim)   
    textSize(40)
    fill(255, 255, 255)
    text("Tu as perdu LOL",width/2,height/4)
    if bouton(width/2,2*height/4.5,200,60,'Rejouer'):
        return "Rejouer"
    if bouton(width/2,2*height/3,200,60,'Exit'):
        return "Exit"
    

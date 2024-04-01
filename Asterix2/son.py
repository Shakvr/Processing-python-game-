
add_library('minim')
from ddf.minim import Minim

def setup_sound():
    global player,minim,player2,player3
    minim = Minim(this)
    player = minim.loadFile("Sacrificial.mp3")
    player2=minim.loadFile("death.mp3")
    player3=minim.loadFile("jump.mp3")
     
def play_sound():
    player.play()

def stop_sound():
    player.close()
    
def play_sound2():
    player2.play()

def stop_sound2():
    player2.close()
    
def play_sound3():
    player3=minim.loadFile("jump.mp3")
    
    player3.play()
    
    player3.shiftGain(player3.getGain(),-150,2000)

def stop_sound3():
    player3.close()

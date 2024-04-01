def death_animation_sequence(sequence):
    c={'x':50,'y':275,'image':sequence,'index':0}
    return c

def afficher_death(c,fi):
    if fi %10==0: # sert a reduire la frequence d'incrementation 
        c['index']=c['index']+1
    
    #c['x']=c['x']+5
    
    if c['index']>=len(c['image']): #and c['x']<width-c['image'][indice].width/2:
        c['index']= 0
    image(c['image'][c['index']],c['x'],c['y'])
    

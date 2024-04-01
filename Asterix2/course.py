def nouvelle_course(sequence):
    c={'x':50,'y':275,'image':sequence,'index':0}
    return c

def afficher_personnage(c):
    c['index']=c['index']+1
    #c['x']=c['x']+5
    
    if c['index']>=len(c['image']): #and c['x']<width-c['image'][indice].width/2:
        c['index']= 0
    image(c['image'][c['index']],c['x'],c['y'])
    

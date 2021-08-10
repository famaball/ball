from genieCivilOuvrage2D import*
speed("fastest")
setup(1400,600)

# fonction pour les demi ellipses
def demiEllipse(x,y,rayon):
    pencolor("blue")
    width(3)
    penup()
    goto(x,y)
    pendown()
    for i in range(1):
        seth(90)
        circle(60,45)
        circle(rayon,90)
        circle(60,45)
        seth(0)
        fd(315)

    
# fonction pour tracer les traits verticaux
def traitVertical(x,y,z,a,b):
    pencolor("blue")
    width(3)
    goto(x,y)
    pendown()
    seth(90)
    rt(90)
    fd(a)
    backward(z)
    lt(90)
    fd(b)
    up()
    
# fonction pour les lignes obliques 
def ligneOblique(x,y,a,b):
    pencolor("blue")
    width(3)
    up()
    goto(x,y)
    pendown()
    seth(90)
    lt(a)
    fd(b)
    backward(b)
    up()
    
       
# Pour la construction du support
def supportPont(x,y,long,larg):
    begin_fill()
    up()
    goto(x,y)   
    rectangle(long,larg,"blue")
    end_fill()

def programmePrincipal():
    
    # dessin du support
    supportPont(-30,-25,75,25)
    supportPont(-60,-50,135,25)
    supportPont(290,-25,75,25)
    supportPont(260,-50,135,25)
    
    # dessin des demi ellipses
    demiEllipse(0,0,200)
    demiEllipse(321,0,200)
    demiEllipse(642,0,200)
    
    # Les traits verticaux pour la premiere demi ellipse      
    traitVertical(-20,0,300,50,67)
    traitVertical(0,0,280,50,85)
    traitVertical(20,0,260,50,95)
    traitVertical(40,0,240,50,98)
    traitVertical(60,0,220,50,95)
    traitVertical(80,0,200,50,77)
    traitVertical(100,0,180,50,53)
    
    # Traits verticaux pour la deuxieme demi ellipse
    traitVertical(140,0,150,50,58)
    traitVertical(160,0,130,50,80)
    traitVertical(180,0,110,50,95)
    traitVertical(200,0,90,50,100)
    traitVertical(220,0,70,50,95)
    traitVertical(240,0,50,50,85)
    traitVertical(260,0,30,50,60)
    
    # Traits verticaux pour la troisieme ellipse
    traitVertical(310,0,-10,50,65)
    traitVertical(330,0,-30,50,85)
    traitVertical(350,0,-50,50,95)
    traitVertical(370,0,-70,50,100)
    traitVertical(390,0,-90,50,95)
    traitVertical(410,0,-110,50,80)
    traitVertical(430,0,-130,50,55)
    
    # traits obliques pour la premiere demi ellipse
    ligneOblique(-270,0,45,50)
    ligneOblique(-270,0,-25,95)
    ligneOblique(-190,0,25,93)
    ligneOblique(-190,0,-22,105)
    ligneOblique(-110,0,22,105)
    ligneOblique(-110,0,-27,87)
    ligneOblique(-31,0,26,88)
    ligneOblique(-31,0,-45,36)
    
    # traits obliques pour la deuxieme deuxieme demi ellipse
    ligneOblique(40,0,45,40)
    ligneOblique(40,0,-26,95)
    ligneOblique(120,0,26,92)
    ligneOblique(120,0,-22,105)
    ligneOblique(200,0,22,105)
    ligneOblique(200,0,-26,92)
    ligneOblique(280,0,26,90)
    ligneOblique(280,0,-45,45)
    
    # traits obliques pour la troisieme demi ellipse
    ligneOblique(370,0,45,50)
    ligneOblique(370,0,-25,95)
    ligneOblique(450,0,25,93)
    ligneOblique(450,0,-22,105)
    ligneOblique(530,0,22,105)
    ligneOblique(530,0,-26,88)
    ligneOblique(610,0,26,89)
    ligneOblique(610,0,-45,36)
    


    
    
if __name__ == '__main__':
    
    programmePrincipal()
    


exitonclick()
done() 
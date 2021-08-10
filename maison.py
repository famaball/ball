from genieCivilOuvrage2D import*

# ça permet d'accélèrer le dessein
# speed("fastest")
speed("fast")
# ça permet de définir la taille de l'écran
setup(1400,800)


def porte(long, larg):    
    rectangle(long, larg, "Silver")

def twite(x,y):
    
    rectangle(180,60,"")
    penup()
    goto(x,y)
    pendown()
    triangle(110,100,181,"LightGreen")

def fenetre(long,larg,x,y):
    for i in range(2):
        penup()
        goto(x,y)
        pendown()
        rectangle(long,larg,"White")
        x = x + long

def grandTwite(couleur):
    fillcolor(couleur)
    begin_fill()
    left(152)
    penup()
    goto(-252, 203)
    pendown()
    forward(430)

    right(152)
    forward(110)
    right(28)
    forward(252)

    right(32)
    forward(100)
    end_fill()

def petitFenetre(x): 
    for i in range(2):
        penup()
        goto(x,90)
        pendown()
        rectangle(15,30,"Silver")
        x = x + 15

def programmePrincipale():
    penup()
    goto(-500,-300)
    pendown()
    rectangle(960,350,"GainsBoro")

    penup()
    goto(-500,-300)
    pendown()
    rectangle(960,10,"White")

    # Implémentation des trois portes à gauche
    penup()
    goto(-490,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,-485, -275)
    fenetre(43,80,-485, -195)
    fenetre(43,43,-485, -80)
    fenetre(43,43,-485, -37)


    penup()
    goto(-380,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,-375, -275)
    fenetre(43,80,-375, -195)
    fenetre(43,43,-375, -80)
    fenetre(43,43,-375, -37)

    penup()
    goto(-270,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,-265, -275)
    fenetre(43,80,-265, -195)
    fenetre(43,43,-265, -80)
    fenetre(43,43,-265, -37)
    

    # Implémentation du portes centrale et scallié
    penup()
    goto(-100,-290)
    pendown()
    rectangle(130,315,"")

    penup()
    goto(-92,-290)
    pendown()
    rectangle(115,88,"")

    penup()
    goto(-100,-202)
    pendown()
    rectangle(130,16,"")
    x = -80
    y = -290
    a = 85
    for i in range(0,7):
        penup()
        goto(x,y)
        pendown()
        rectangle(a,14,"")
        x = x + 5
        y = y + 15
        a = a - 10   

    penup()
    goto(-92,-186)
    pendown()
    rectangle(110,210,"")

    penup()
    goto(-80,-186)
    pendown()
    porte(88,210)
    #rectangle(88,210,"Silver")

    fenetre(33,48,-70, -185)
    fenetre(33,48,-70, -138)

    penup()
    goto(-5,-90)
    pendown()
    demiCercle(32,"Silver")

    penup()
    goto(-42,-40)
    pendown()
    cercle(9,"Black")

    fenetre(20,30,-55, -20)
    
    # Implémentation des trois portes à droite
    penup()
    goto(110,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,115, -275)
    fenetre(43,80,115, -195)
    fenetre(43,43,115, -80)
    fenetre(43,43,115, -37)

    penup()
    goto(220,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,225, -275)
    fenetre(43,80,225, -195)
    fenetre(43,43,225, -80)
    fenetre(43,43,225, -37)

    penup()
    goto(330,-285)
    pendown()
    porte(100,300)
    fenetre(43,80,335, -275)
    fenetre(43,80,335, -195)
    fenetre(43,43,335, -80)
    fenetre(43,43,335, -37)
    
    # Implémentation du "daale"
    penup()
    goto(-528,90)
    pendown()
    trapeze(1012,45,961,45,"GainsBoro")
    
    right(120)
    penup()
    goto(-127,25)
    pendown()
    rectangle(185,66,"White")
    
    #right(90)
    penup()
    goto(-350, 90)
    pendown()
    twite(-350,150)

    right(210)
    penup()
    goto(80,92)
    pendown()
    twite(80,150)

    grandTwite("LightGreen")
       
    right(145)
    petitFenetre(-330)
    petitFenetre(-280)
    petitFenetre(-230)
    
    petitFenetre(-157)
    petitFenetre(-100)
    petitFenetre(-60)
    petitFenetre(-20)
    petitFenetre(30)
    
    petitFenetre(100)
    petitFenetre(150)
    petitFenetre(200)
    
if __name__=="__main__":
    #Couleur du background
    #bgcolor("LightGrey")
    #appel du fonction principale
    programmePrincipale()
    
    done()
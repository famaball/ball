""" 
    Module de dessein intitulé genieCivilOuvrage2D.py de plusiers figure 
    géometrique à l'aide de du module turtle
"""

from turtle import *  
from math import *  

# Programme d'implémentation pour dessiner du carré
def carre(taille):
    for i in range(4):
        forward(taille)
        left(90)
    
# Programme d'implémentation pour dessiner un cercle
def cercle(taille,couleur):
    fillcolor(couleur)
    begin_fill()
    circle(taille)
    left(90)
    end_fill()
      

# Programme d'implémentation pour dessiner un demiCercle       
def demiCercle(taille,couleur):
    fillcolor(couleur)
    begin_fill()
    left(90)
    circle(taille,180)
    end_fill()
    
        
     
# Programme d'implémentation pour dessiner un triangle quelconque
# Selon le théorie de Al khasi
def triangle(a, b, c, couleur):
    
    fillcolor(couleur) 
    begin_fill()
    vare = degrees(acos(((b**2)+(c**2) - (a**2))/(2*c*b)))
    forward(c)
    left(180-vare)
        
    forward(b)
    vare = degrees(acos(((a**2)+(b**2) - (c**2))/(2*a*b)))
    left(180-vare)    
    forward(a)
    end_fill()
    
# Programme d'implémentation pour tester les fonctions 
def trapeze(grandBase,h1,petitBase,h2,couleur):
    fillcolor(couleur)
    begin_fill()
    forward(grandBase)
    right(120)
    forward(h1)
    right(60)
    forward(petitBase)
    right(60)
    forward(h2)
    end_fill()
 
# Programme d'implémentation pour dessiner un rectangle
def rectangle(long, larg, couleur):
    fillcolor(couleur) 
    begin_fill()
    for i in range(2):
    
        forward(long)
        left(90)
        forward(larg)
        left(90)
    end_fill()

# Programme d'implémentation pour dessiner un polygone       
def polygone(nombreCote, couleur):
    for i in range(nombreCote):
        fillcolor(couleur) 
        forward(100)
        left(360/7)
        end_fill()
        

# Programme d'implémentation pour dessiner un losange
def losange(couleur):
    fillcolor(couleur) 
    for i in range(4):
        forward(100)
        left(180/4)
    end_fill()
    
 
# Programme d'implémentation pour dessiner un ellipse
def ellipse(taille,couleur):
    fillcolor(couleur) 
    begin_fill()
    for i in range(2):
        circle(taille,90) 
        circle(taille//2,90)
    seth(-45) 
    end_fill()
  


# Par Tahiry NOURDINE
# Date de création: 24/09/2026
# Programme qui simule sur un repère cartésien la trajectoire d'une balle frappée en cloche
# V2
# Dernière MàJ: 15/10/2026
# Licence 3Dflamingo™

import math as m

import matplotlib.pyplot as plt

# definition de fonctions mathématiques

def calc_racine0(a,b): # si delta=0, il n'y a qu'une racine et est renvoyée par cette fonction
    racine0 = -b/(2*a)  
    return racine0

# si delta>0, il y a 2 points où la courbe atteint 0, ils sont renvoyés par les fonctions ci-dessous
def calc_racine1(a,b,d):
    racine1 = (-b - m.sqrt(d)) / (2*a)
    return racine1
def calc_racine2(a,b,d):
    racine2 = (-b + m.sqrt(d)) / (2*a)
    return racine2

def calc_y(a,b,c,x):
    y = (a*x**2) + (b*x) + c
    return y


# Implementation des valeurs donnees sur le sujet
def trajectoireBallon(a,b,c,d):



    # y n'admet aucune solution si d est negatif
    if d < 0:
        print("Δ < 0 : pas de racine réelle, le ballon ne touche jamais le sol")
        exit()

    # Sinon, on calcule alors les racines de delta
    # note: ces racines sont les valeurs de x pour lesquelles y=0
    elif d == 0:
        r0 = calc_racine0(a,b)
    else:
        r1 = calc_racine1(a,b,d)
        r2 = calc_racine2(a,b,d)
        # on conserve en variables le point de départ du ballon, et l'endroit où il retouche le sol
        x_depart = min(r1,r2)
        x_arrivee = max(r1,r2)

    # Question 2 : tracé entre les deux racines avec matplotlib

    n = 200
    pas = (x_arrivee-x_depart)/n

    x=[]
    y=[]

    sommet = (-b)/(2*a)

    # _valeurs de x_
    for i in range(n+1):
        nb_pas = i * pas
        val_x = x_depart + nb_pas
        x.append(val_x)

    # _valeurs de y_
    for val_x in x:
        val_y=calc_y(a,b,c,val_x)
        y.append(val_y)

    print("altitude maximale atteinte par la balle y = ",str(max(y)))
    print("en x = ",str(sommet))
    # tracer et afficher la courbe avec matplotlib
    plt.plot(x, y)
    plt.xlabel("x (distance)")
    plt.ylabel("y (altitude)")
    plt.savefig("courbe.png")
    plt.show()



# Section du code à executer (main)
a = float(input("Valeur de a: "))
b = float(input("Valeur de b: "))
c = float(input("Valeur de c: "))

# calcul de delta
d = b**2 - 4*a*c

trajectoireBallon(a,b,c,d)

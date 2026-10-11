import math as m

import matplotlib.pyplot as plt

# Implementation des valeurs donnees sur le sujet
a = -0.1
b = 2
c = 5

# calcul de delta
delta = b**2 - 4*a*c

# y n'admet aucune solution si delta est negatif
if delta < 0:
    print("Δ < 0 : pas de racine réelle, le ballon ne touche jamais le sol")
    exit()

# Sinon, on calcule alors les racines de delta
# note: ces racines sont les valeurs de x pour lesquelles y=0
elif delta == 0:
    r0 = -b/(2*a)
else:
    r1 = (-b - m.sqrt(delta)) / (2*a)
    r2 = (-b + m.sqrt(delta)) / (2*a)
    # on conserve en variables le point de départ du ballon, et l'endroit où il retouche le sol
    x_depart = min(r1,r2)
    x_arrivee = max(r1,r2)

# Question 2 : tracé entre les deux racines avec matplotlib

n = 100
pas = (x_arrivee-x_depart)/n

x=[]
y=[]

# _valeurs de x_
for i in range(n+1):
    nb_pas = i * pas
    val_x = x_depart + nb_pas
    x.append(val_x)

# _valeurs de y_
for val_x in x:
    

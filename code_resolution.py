import math as m

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
elif delta == 0:
    r0 = -b/(2*a)
    print("Pour x= ",str(r0)," on a y=0")
else:
    r1 = (-b - m.sqrt(delta)) / (2*a)
    r2 = (-b + m.sqrt(delta)) / (2*a)
    print("Pour x= ",str(r1)," on a y=0\nIci: python le joueur a frappe la balle")
    print("Pour x= ",str(r2)," on a y=0\nIci: la balle touche le sol")


    
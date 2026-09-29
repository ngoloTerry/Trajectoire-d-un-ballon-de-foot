# Bac à Sable pour tester et apprendre des éléments essentiels pour avancer
import math as m

import matplotlib.pyplot as plt

# On trace la courbe sur matplotlib
# mathplotlib, pour tracer une courbe sur un repère, a besoin de tableaux pour représenter les axes

# préparation des éléments à afficher

# On prépare les valeurs de a, b, c:

a=float(input("entrez la valeur de a:"))
b=float(input("entrez la valeur de b:"))
c=float(input("entrez la valeur de c:"))
delta = b**2-(4*a*c)
if(delta<0):
    print("Error Delta: valeur négative impossible")
    exit()
x=[] # toutes les valeurs en abscisse
y=[] # toutes les valeurs en ordonnées f(x)
pas = 99/99 # Division de 20 par 99 pour obtenir le nombre de points 
for i in range(100):
    x.append(i)
    f_x= (-1*b-m.sqrt(delta))/(2*a)
    y.append(f_x)


plt.plot(y) # trace la courbe X sur le repère
plt.xlabel("x") # étiquette sur le repère pour x
plt.ylabel("delta") # étiquette sur le repère pour y
plt.show()

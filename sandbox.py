import math as m

import matplotlib.pyplot as plt

a = float(input("entrez la valeur de a: "))
b = float(input("entrez la valeur de b: "))
c = float(input("entrez la valeur de c: "))

if a == 0:
    print("a=0 : ce n'est pas une équation du second degré")
    exit()

delta = b**2 - 4*a*c

if delta < 0:
    print("Δ < 0 : pas de racine réelle, le ballon ne touche jamais le sol")
    exit()
elif delta == 0:
    x_depart = x_arrivee = -b / (2*a)
else:
    r1 = (-b - m.sqrt(delta)) / (2*a)
    r2 = (-b + m.sqrt(delta)) / (2*a)
    x_depart, x_arrivee = min(r1, r2), max(r1, r2)

# Question 3 : sommet de la parabole
x_sommet = -b / (2*a)
y_max = a*x_sommet**2 + b*x_sommet + c
print(f"Altitude maximale : {y_max:.2f} en x = {x_sommet:.2f}")

# Question 2 : tracé entre les deux racines
N = 200
pas = (x_arrivee - x_depart) / N
x = [x_depart + i*pas for i in range(N + 1)]
y = [a*xi**2 + b*xi + c for xi in x]

plt.plot(x, y)
plt.xlabel("x (distance)")
plt.ylabel("y (altitude)")
plt.show()
# Par Tahiry NOURDINE
# Date de création: 24/09/2026
# Programme qui simule sur un repère cartésien la trajectoire d'une balle frappée en cloche
# V3
# Dernière MàJ: 25/10/2026
# Licence 3Dflamingo™

import math as m

import matplotlib.pyplot as plt
from tkinter import *



# __Méthodes sur la fenêtre__
# def submitA():
#     value = valeurA.get()
#     print("A : ",value)

# def submitB():
#     value = valeurB.get()
#     print("B : ",value)

# def submitC():
#     value = valeurC.get()
#     print("C : ",value)


# __definition de fonctions mathématiques__
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



# __Fonction qui trace la courbe__
def trajectoireBallon(a,b,c):

    if a >= 0:
        raise ValueError("a doit être négatif pour une trajectoire en cloche")

    d = b**2 - 4*a*c

    if d <= 0:
        raise ValueError("Δ ≤ 0 : le ballon ne touche pas le sol")

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
    # tracer et sauvegarder la courbe en png avec matplotlib
    plt.plot(x, y)
    plt.xlabel("x (distance)")
    plt.ylabel("y (altitude)")
    plt.savefig("courbe.png")
    plt.close()


def valider():
    global imageSelect
    try:
        a = float(valeurA.get().replace(",", "."))
        b = float(valeurB.get().replace(",", "."))
        c = float(valeurC.get().replace(",", "."))
    except ValueError:
        imageSelect = PhotoImage(file="error.png")
        labelImage.config(image=imageSelect)
        return
    
    try:
        trajectoireBallon(a,b,c)
        imageSelect = PhotoImage(file="courbe.png")
        labelImage.config(image=imageSelect)

    except ValueError as e:
        imageSelect = PhotoImage(file="error.png")
        labelImage.config(image=imageSelect)




# Création de la fenêtre
window = Tk() # pour déclarer l'objet "fenêtre"
window.title("3Dflamingo's First tkinter program") # changer le titre de la fenêtre
window.geometry("1000x900")

# éléments
icon = PhotoImage(file="flamingo.png")

titre = Label(text="Tracez votre parabole !",font=("Arial",50))

ecranNoir = PhotoImage(file="default.png")
labelImage = Label(window,
relief=RAISED,
bd=10,
padx=20,
pady=20,
image=ecranNoir)

labelA = Label(text="Valeur de A:")
valeurA = Entry()
valeurA.config(font=("Arial"))


labelB = Label(text="Valeur de B:")
valeurB = Entry()
valeurB.config(font=("Arial"))


labelC = Label(text="Valeur de C:")
valeurC = Entry()
valeurC.config(font=("Arial"))

buttonStart = Button(window, text="VALIDER", command=valider)

# labels = surface dans la fenêtre

# afficher
titre.pack()

labelImage.place(x=300,y=100)

labelA.place(x=50,y=100)
valeurA.place(x=50,y=125)
# buttonA.place(x=50,y=150)

labelB.place(x=50,y=300)
valeurB.place(x=50,y=325)
# buttonB.place(x=50,y=350)

labelC.place(x=50,y=500)
valeurC.place(x=50,y=525)
# buttonC.place(x=50,y=550)

buttonStart.place(x=500,y=800)
window.update()
window.iconphoto(True, icon)

# afficher la fenêtre
window.mainloop() 

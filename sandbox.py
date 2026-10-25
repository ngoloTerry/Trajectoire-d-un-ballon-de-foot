# tutoriel: https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T

from tkinter import *
# widgets = éléments de la fenêtre
# window = la fenêtre remplie de widgets

count = 0

# Méthodes
def click():
    global count
    count += 1
    compteur.config(text=count)

def submitA():
    value = entry.get()
    print("A : ",value)

def submitB():
    value = entry.get()
    print("B : ",value)

def submitC():
    value = entry.get()
    print("C : ",value)


# déclarations de paramètres et méthodes de la fenêtre
window = Tk() # pour déclarer l'objet "fenêtre"
window.title("3Dflamingo's First tkinter program") # changer le titre de la fenêtre
window.geometry("500x500")

# éléments
icon = PhotoImage(file="flamingo.png")

button = Button(window,text=("Frapper"), command=submit)
button.config(command=click)

# entry = Entry()
# entry.config(font=("Arial"))

valeurA = Entry()
valeurA.config(font=("Arial"))

valeurB = Entry()
valeurB.config(font=("Arial"))

valeurC = Entry()
valeurC.config(font=("Arial"))

# labels = surface dans la fenêtre
compteur = Label(window, text=count)




# afficher
compteur.pack()
button.pack()
# entry.pack()
valeurA.pack()
valeurB.pack()
valeurC.pack()
window.iconphoto(True,icon)

# afficher la fenêtre
window.mainloop() 
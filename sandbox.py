# tutoriel: https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T

from tkinter import *
# widgets = éléments de la fenêtre
# window = la fenêtre remplie de widgets

# valeurs constantes
W_HEIGHT = 700
W_WIDTH = 700
count = 0

# Méthodes
def submitA():
    value = valeurA.get()
    print("A : ",value)

def submitB():
    value = valeurB.get()
    print("B : ",value)

def submitC():
    value = valeurC.get()
    print("C : ",value)


# déclarations de paramètres et méthodes de la fenêtre
window = Tk() # pour déclarer l'objet "fenêtre"
window.title("3Dflamingo's First tkinter program") # changer le titre de la fenêtre
window.geometry("1000x900")

# éléments
icon = PhotoImage(file="flamingo.png")

titre = Label(text="Titre",font=("Arial",50))

courbe = PhotoImage(file="courbe.png")
labelImage = Label(window,
relief=RAISED,
bd=10,
padx=20,
pady=20,
image=courbe)

labelA = Label(text="Valeur de A:")
valeurA = Entry()
valeurA.config(font=("Arial"))
# buttonA = Button(window,text=("Valider"), command=submitA)


labelB = Label(text="Valeur de B:")
valeurB = Entry()
valeurB.config(font=("Arial"))
# buttonB = Button(window,text=("Valider"), command=submitB)


labelC = Label(text="Valeur de C:")
valeurC = Entry()
valeurC.config(font=("Arial"))
# buttonC = Button(window,text=("Valider"), command=submitC)

buttonStart = Button(window, text="VALIDER")

# labels = surface dans la fenêtre
compteur = Label(window, text=count)




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

window.iconphoto(True,icon)

# afficher la fenêtre
window.mainloop() 
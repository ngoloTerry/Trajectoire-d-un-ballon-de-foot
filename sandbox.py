# tutoriel: https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T

import tkinter as tkt

# widgets = éléments de la fenêtre
# window = la fenêtre remplie de widgets

# déclarations de paramètres et méthodes de la fenêtre
window = Tk() # pour déclarer l'objet "fenêtre"
window.geometry("500x500") # régler les dimensions
window.title("3Dflamingo's First Program") # changer le titre de la fenêtre

icon = PhotoImage(file="./flamingo.png")
window.iconphoto(True,icon)

# ajoute un contenu
label1 = Label(
    window,
    text="Bisou ? 😘",
    font=("Arial",40,"bold"),
    bg="grey",
    padx="20"
)
label2 = Label(
    window,
    text="Ouiii 💋💖",
    font=("Arial",25)
    
)

label1.pack() # pose par défaut dans le top-centre
label2.place(x=150,y=300)


# afficher la fenêtre
window.mainloop() 

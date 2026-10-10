  

  

# Calculer la Trajectoire du Ballon

  

  

  

  

## Objectifs

  

  

- Il faut développer un code qui simule la trajectoire d'un ballon selon certains paramètres d'entrée.

  

  

- Ce code utilisera la librairie Matplotlib, pour tracer une courbe sur un repère cathésien.

  

  

- Le repère cartésien doit afficher la trajectoire d'une balle de football, frappée du pied depuis le sol.  

  

  

## Maths: calculer Δ (Delta)

  

  

Formule polynôme de degré 2:

  

# $ax²+b²+c$ = 0
Pour trouver une solution, on cherche Δ (Delta) avec la formule suivante:

  

# $Δ=-b²-4ac$

  Il y a 3 racines, celles-ci s'expriment comme tel selont la valeur de Δ

<u>Les différentes conditions sont:</u>

  

  

- Si $Δ = 0$, la courbe touche l'axe des ordonnées en 1 point

  

  

- Si $Δ > 0$, la courbe touche l'axe des ordonnées en 2 points (ce qui nous intéresse pour la trajectoire du ballon).

## $x_{1}= \frac{(-b-\sqrt{Δ})}{2a}$

## $x_{2}= \frac{(-b+\sqrt{Δ})}{2a}$

  
  
  

- Si $Δ < 0$, alors il n'y a aucune solution pour

  

  

# Code: implémenter dans une courbe [numpy](https://numpy.org/doc/)

  

  

  
# interface: afficher la courbe dans une interface [TKinter](https://docs.python.org/3/library/tk.html)
# Téléversage: Récupérer l'affichage de la courbe avec [Canvas](https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html) (embeding)

# Versionnage:
    # - nom prénom de l'auteur
    # - Date de création
    # - Courte description
    # - n° de version
    # - Date de dernière mise à jour
    # - Licence

# Par Tahiry NOURDINE
# 24/09/2026
# Programme qui simule sur un repère cartésien la trajectoire d'une balle frappée en cloche
# V0
# 24/09/2026
# Licence 3Dflamingo™


import  math as m
import matplotlib.pyplot as plt

# Implémentation de la solution de l'équation du second degré telle que: y=-0.1x²+2x-5
# calcul de delta: b²-4ac
def trajectoire(a, b, c): 
    
    delta = b**2-(4*a*c)

    # si delta = 0, alors il n'y a qu'une solution
    if(delta == 0):
        racine0 = (-1*b)/(2*a)

    # si delta > 0, alors il y a 2 solutions
    # les deux racines se calculent avec:
    racine1 = (-b-m.sqrt(delta))/(2*a)
    racine2 = (-b+m.sqrt(delta))/(2*a)

    # - (-b-sqrt(delta))/(2*a)
    # - (-b+sqrt(delta)/(2*a))

    # 2 choses importantes : signe de a et signe de delta
    # pour a
    # si a > 0, alors la parabole fait ∪ -> a doit donc être négatif pour un arc possible physiquement
    # pour delta
    # si delta < 0: pas de solution (ne croise pas l'axe X, ou le sol)
    # si delta = 0: la balle ne peut partir qu'ailleur que 0 sur l'axe: or c'est ce qu'on recherche ?

    # DONC:
    # a est obligatoirement négatif
    # on fait reformuler à l'utilisateur si delta est négatif ?
    
    #






res = trajectoire(0.1,2,-5)


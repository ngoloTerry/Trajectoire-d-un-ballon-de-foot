


# Journal de bord


## 10/10/26
### - Ajout du journal de bord dans le projet.
J'ai décidé d'ajouter un carnet de bord pour annoter plus en détail les changements journaliers.

### -Révision du projet et de son découpage par Claude AI.

Après avoir passé quelques jours sans avancer, une remise en question devait se faire. Afin d'avancer, il fallait que je revois:

- Les problèmes "non sous-divisables" de ce projet
- L'ordre dans lequel tout préparer
 
J'ai donc passé les fichiers à cette étape du projet en lui demandant ceci:

```Ma tentative de segmentation du travail se trouve dans le readme.md
Je veux que tu me dises si mon découpage du travail est correct, efficace en terme de fatigue (est-ce que j'ai fait des tâches plus grosses que d'autres qui risquent de me fatiguer si j'essaye de la faire d'une seule traite)
Ce qu'il y a à améliorer, et quelles seraient les étapes que tu rajouterait, et une petite partie d'aide pour commencer chaque étape de ce projet.
```

Il m'a alors indiqué que:
- La section "Code numpy" est un monolithe, et qu'il faut absolument le sous-diviser. Il est vrai que je n'ai même pas pensé à réfléchir ici en quelles foctions ce code entier risque d'être sectionné.
- Il faut revoir ce qui est attendu que l'on comprenne, mathématiquement parlant, pour mieux améliorer sa résolution de problème.

En appliquant ces conseils, j'ai décidé de recommencer de 0 (ou plutôt de 1) écrivant et isolant le code de la question 1 (code_resolution.py).  
une fois fait, il fallait que je satisfasse la question 2 dans un autre fichier(traceCourbe), en réutilisant le code déjà tapé.

## 11/10/26
### découverte et application de la librairie MatPlotLib
Dans le sandbox, j'ai importé une version fonctionelle du code, que je découpe en morceau pour en comprendre le fonctionnement.
dans traceCourbe.py, j'essaye de le réécrire proprement d'une manière où je peux la faire fonctionner, avec des commentaires pour la relecture.
MatPlotLib, pour tracer une courbe, fait le lien entre des points renseignés sur un repère carthésien.
pour tracer une courbe il faut donc 2 tableaux de valeurs: un avec les valeurs en ordonnée, l'autre avec les abscisses.
pour remplir ces deux tableauxdes valeurs correspondantes, il nous faudra décider du nombre de valeurs, et calculer le pas entre chacun des points de coordonnées x[i]y[i]

### calcul du pas de la courbe matPlotLib
En divisant par le nombre n de points que l'on souhaite représenter sur le repère la soustraction de max(x_depart, x_arrivee) par min(x_depart, x_arrivee), on découpe en segments égaux l'intervalle sur la courbe qui représente le point de départ du ballon jusqu'à son arrivée.
Ainsi, on sait de combien incrémenter pour passer de x[i] à x[i+1] jusqu'à x[n].
Pour calculer la valeur de y par rapport à x, en voyant que l'écriture commençait à être chargée, je me suis dit qu'il serait logique de créer des fonctions qui allègeraient l'expression mathématique dans certaines variables.
Une fois le code matplotlib utilisé pour tracer et afficher la courbe en fonction de x et y, on a terminé la question 2.

### déterminer la hauteur max de la balle
Pour les valeurs de la consigne, si on regarde sur le graph tracé avec matplotlib, on peut voir que la valeur maximum de y=15 pour x=10.
L'exprimer par code revient donc à récupérer le maximum du tableau de y et sa valeur correspondante pour x.
Une expression mathématique existe pour calculer la valeur de x lorsqu'on atteint la valeur maximale de y:
$\frac{-b}{2a}$
Et de cette manière, on a répondu à la question 3

### Généralisation du problème et entrée utilisateur
En utilisant le code de traceCourbe, on peut reprendre sur TrajectoireBallon_v2.py notre code, et le modifier pour que ce code trace une courbe en fonction d'une donnée en entrée.

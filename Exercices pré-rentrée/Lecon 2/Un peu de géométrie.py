# Lecon 2 - Les structures conditionnelles
# Exercice "Un peu de géométrie"

# Imports des modules python complementaires
from math import *

# Definition des fonctions pour chacune des figures
def disque():
	rayon = float(input())
	print("Aire du disque =", pow(rayon, 2) * pi)

def triangle():
	base = float(input())
	hauteur = float(input())
	print("Aire du triangle =", base * hauteur / 2)

def rectangle():
        longueur = float(input())
        largeur = float(input())
        print("Aire du rectangle =", longueur * largeur)

# Dictionnaire des figures 
figures = {
        1 : disque,
        2 : triangle,
        3 : rectangle
}

figureChoisie = int(input()) # Choix de la figure a l'aide d'un numero fournit par l'utilisateur
# Verification du numero
# Si celui ci est present dans le dictionnaire des figures, on calcule l'aire
# Sinon, on affiche un message d'erreur
if figureChoisie in figures :
	figures[figureChoisie]()
else :
	print("Le numero ne correspond a aucune figure")


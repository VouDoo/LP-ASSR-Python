# Lecon 3 - Les fonctions
# Exercice "Aire d'un disque"

# Imports des modules python complementaires
from math import pi as Pi

def aireDisque(r) :
        """
        Calcul de l'aire d'un disque
        Entrees :
           r : rayon du disque
        Sorties :
           Aire du disque
        Mecanismes :
           Calcul de l'aire a l'aide de la formule suivante
           pi * rayon^2
        """
        return Pi * r ** 2

rayon = float(input())

print("L'aire d'un disque de rayon", rayon, "est", aireDisque(rayon))

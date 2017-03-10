# Lecon 3 - Les fonctions
# Exercice "Aire d'un triangle"

def aireTriangle(b, h) :
        """
        Calcul de l'aire d'un triangle
        Entrees :
           b : base du triangle
           h : hauteur du triangle
        Sorties :
           Aire du triangle
        Mecanismes :
           Calcul de l'aire a l'aide de la formule suivante
           base * hauteur / 2
        """
        return b * h / 2

base = float(input())
hauteur = float(input())

print("L'aire d'un triangle de base", base, "et de hauteur", hauteur, "est", aireTriangle(base, hauteur))

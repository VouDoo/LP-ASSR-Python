# Lecon 3 - Les fonctions
# Exercice "Carré"

def carre(carac, n) :
        """
        Dessine un carre avec un caractere choisi
        Entrees :
           carac : caractere utilise pour le dessin
           n : nombre entier (cote du carre)
        Sorties :
           Rien (void)
        Mecanismes :
           La fonction permet de dessiner un carre avec un caractere choisi sur n lignes et n colonnes
        """
        print((carac * n + "\n") * (n - 1) + (carac * n))

caractere = str(input()) # caractere pour le dessin
nbr = int(input()) # nombre de lignes et de colonnes

carre(caractere, nbr)

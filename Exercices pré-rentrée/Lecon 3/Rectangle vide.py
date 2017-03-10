# Lecon 3 - Les fonctions
# Exercice "Rectangle vide"

def rectangleVide(carac, l, c) :
        """
        Dessine un rectangle vide avec un caractere choisi par l'utilisateur
        Entrees :
           carac : caractere utilise pour le dessin
           l : nombre de lignes
           c : nombre de colonnes
        Sorties :
           Rien (void)
        """
        if l == 0 or c == 0 :
                return
        elif l <= 2 or c <= 2 :
                print((carac * c + "\n") * (l - 1) + carac * c)
                return
        else :
                print(carac * c + "\n" + (carac + " " * (c - 2) + carac + "\n") * (l - 2) + carac * c)
                return

caractere = str(input()) # caractere pour le dessin
nbrLignes = int(input()) # nombre de lignes
nbrColonnes = int(input()) # nombre de colonnes

rectangleVide(caractere, nbrLignes, nbrColonnes)

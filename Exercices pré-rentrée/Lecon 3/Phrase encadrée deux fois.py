#################################################
# Auteur : Grymonprez Maxence
# Date : 23/08/2016
#
# Lecon 3 - Les fonctions
# Exercice "Phrase encadree deux fois"
#################################################

def encadreDeuxFois(phrase, caracInt, caracExt) :
        """
        Encadre une phrase avec deux cadres de caracteres
        Entrees :
           phrase : phrase a encadrer
           caracInt : caractere utilise pour le cadre interieur
           caracExt : caractere utilise pour le cadre exterieur
        Sorties :
           Rien (void)
        """
        taillePhrase = len(phrase) # taille de la phrase a encadrer
        print(caracExt * (taillePhrase + 4))
        print(caracExt + caracInt * (taillePhrase + 2) + caracExt)
        print(caracExt + caracInt + phrase + caracInt + caracExt, sep = '')
        print(caracExt + caracInt * (taillePhrase + 2) + caracExt)
        print(caracExt * (taillePhrase + 4))

phraseAEncadrer = str(input()) # Phrase a encadrer
caractereInterieur = str(input()) # Caractere du cadre interieur
caractereExterieur = str(input()) # Caractere du cadre exterieur

encadreDeuxFois(phraseAEncadrer, caractereInterieur, caractereExterieur)

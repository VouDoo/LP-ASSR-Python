#################################################
# Auteur : Grymonprez Maxence
# Date : 23/08/2016
#
# Lecon 3 - Les fonctions
# Exercice "Phrase encadree deux fois"
#################################################


""" *** Objectif de l'exercice ***
Définir une fonction qui attend une phrase et deux caractères donnés, puis qui encadre la phrase avec un double cadre formé avec les deux caractères.
On ne laissera pas d'espace autour de la phrase.
Dans le programme principal, on entrera dans cet ordre la phrase et les caractères d'encadrement puis on affichera la phrase encadrée par appel à la fonction.
"""


### [Debut] Imports des modules Python complementaires ###
"""
Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###


### [Debut] Definition des fonctions ###

## Fonction "encadrerPhrDeuxFois"
def encadrerPhrDeuxFois(phr, caracInt, caracExt) :
        """
        Description : Encadre une ou chaine de caractere avec un cadre composé de deux caracteres : un caractere pour le cadre interieur, un autre pour le cadre exterieur
        Entrees :
                phr : phrase (ou chaine de caractere) a encadrer
                caracInt : caractere utilise pour le cadre interieur
                caracExt : caractere utilise pour le cadre exterieur
        Sorties :
        Rien (void)
        Mecanisme :
                On affiche directement par appel de la fonction la phrase encadree a l'aide de la fonction "print"
        """
        taillePhr = len(phr) # Taille de la phrase
        # Affichage de la phrase avec le cadre
        # Haut du cadre
        print(caracExt * (taillePhr + 4))
        print(caracExt + caracInt * (taillePhr + 2) + caracExt)
        # Centre du cadre contenant la phrase
        print(caracExt + caracInt + phr + caracInt + caracExt, sep = '')
        # Bas du cadre
        print(caracExt + caracInt * (taillePhr + 2) + caracExt)
        print(caracExt * (taillePhr + 4))

### [Fin] Definition des fonctions ###


### [Debut] Programme principal ###

# Message introductif
print("""\
*****************************
* Phrase encadree Deux fois *
*****************************\n
Ce programme permet d'encadrer une phrase avec deux caractere specifiquement choisi par l'utilisateur :\n
Le premier caractere sera utilise pour le cadre interieur et le deuxieme caractere pour le cadre exterieur.\n
Veuillez saisir les donnees suivantes :""")

# Premierement, l'utilisateur entre la phrase a encadrer puis le caractere d'encadrement
phrAEncadrer = str(input("\tPhrase a encadrer : ")) # Saisie de la phrase a encadrer
caracCadreInt = str(input("\tCaractere d'encadrement interieur : ")) # Saisie du caractere d'encadrement pour le cadre interieur
caracCadreExt = str(input("\tCaractere d'encadrement interieur : ")) # Saisie du caractere d'encadrement pour le cadre exterieur
print("\n") # Retour chariot pour un affichage clarifie

# Appel de la fonction "encadrerPhr" avec les parametres respectifs
# 1er parametre : la phrase a encadrer (la variable "phrAEncadrer")
# 2eme parametre : Le caractere d'encadrement interieur (la variable "caracCadreInt")
# 3eme parametre : Le caractere d'encadrement exterieur (la variable "caracCadreExt")
encadrerPhrDeuxFois(phrAEncadrer, caracCadreInt, caracCadreExt)

### [Fin] Programme principal ###

#################################################
# Auteur : Grymonprez Maxence
# Date : 23/08/2016
#
# Lecon 3 - Les fonctions
# Exercice "Phrase encadree"
#################################################


""" *** Objectif de l'exercice ***
Définir une fonction qui attend une phrase et un caractère, puis qui encadre la phrase avec le caractère donné en laissant des espaces autour de la phrase.
Dans le programme principal, on entrera dans cet ordre la phrase et le caractère d'encadrement puis on affichera la phrase encadrée par appel à la fonction.
"""


### [Debut] Imports des modules Python complementaires ###
"""
Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###


### [Debut] Definition des fonctions ###

## Fonction "encadrerPhrase"
def encadrerPhr(phr, carac) :
	"""
	Encadre une phrase (ou chaine de caractere) avec un cadre dessine avec un caractere donne
	Entrees :
	   phr : phrase (ou chaine de caractere) a encadrer
	   carac : caractere utilise pour le cadre
	Sorties :
	   Rien (void)
	Mecanisme :
		On affiche directement par appel de la fonction la phrase encadree a l'aide de la fonction "print"
	"""
	taillePhr = len(phr) # Taille de la phrase

	# Affichage de la phrase avec le cadre
	# Haut du cadre
	print(carac * (taillePhr + 4))
	print(carac, ' ' * taillePhr, carac)
	# Centre du cadre contenant la phrase
	print(carac, phr, carac)
	# Bas du cadre
	print(carac, ' ' * taillePhr, carac)
	print(carac * (taillePhr + 4))

### [Fin] Definition des fonctions ###


### [Debut] Programme principal ###

# Messsage introductif
print("""\
*******************
* Phrase encadree *
*******************\n
Ce programme permet d'encadrer une phrase avec un caractere specifiquement choisi par l'utilisateur\n
Veuillez saisir les donnees suivantes :""")

# Premierement, l'utilisateur entre la phrase a encadrer puis le caractere d'encadrement
phrAEncadrer = str(input("\tPhrase a encadrer : ")) # Saisie de la phrase a encadrer
caracCadre = str(input("\tCaractere d'encadrement : ")) # Saisie du caractere d'encadrement
print("\n") # Retour chariot pour un affichage clarifie

# Appel de la fonction "encadrerPhr" avec les parametres respectifs
# 1er parametre : la phrase a encadrer (la variable "phrAEncadrer")
# 2eme parametre : Le caractere d'encadrement (la variable "caracCadre")
encadrerPhr(phrAEncadrer, caracCadre)

### [Fin] Programme principal ###

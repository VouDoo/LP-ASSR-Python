#!/usr/bin/python3
# -*- coding: utf-8 -*-

##################################################
#
#	Auteur : 	Grymonprez Maxence
#
#	Titre : 	Triangle rectangle creux
#
##################################################


"""
Consigne :

Créer un programme qui attend un nombre N compris entre 4 et 10, n caractère C et qui affiche un triangle rectangle creux de N lignes à l'aide du caractère C comme dans l'exemple de session ci-dessous.

Attention :

l’affichage sera réalisé par l’appel d’une fonction «triangle» admettant en entrée les 2 paramètres saisis par l’utilisateur.
Comme le montrent les 2 premiers essais de l'utilisateur dans la session ci-dessus, la saisie de N sera blindée, c'est-à-dire que l'utilisateur sera contraint de saisir N jusqu'à ce que son choix soit valide (N compris entre 4 et 10).
"""


# Definition des fonctions

# Fonction "triangerectanglecreux"
def trianglerectanglecreux(nbLignes, caractere):
	"""
	Description :
		La fonction retourne le dessin d'un triangle rectangle dans une chaine de caracteres.
		Le triangle est defini en fonction d'un nombre de ligne et d'un caractere utilise pour son trace.
	entrees :
		nbLignes (integer) : nombre de ligne du triangle
		caractere (str) : caractere utilise pour le trace du triangle 
	sorties :
		chaine (str) : chaine de caractere contenant le dessin du triangle
	"""	
	
	# Initialisation des variables
	nbLignes = int(nbLignes)
	caractere = str(caractere)
	chaine = str()

	# Dessin du triangle affecte a la variable "chaine"
	for i in range(0, nbLignes):
		if i == 0:
			chaine += caractere + "\n"
		elif i == (nbLignes - 1) :
			chaine += caractere * nbLignes + "\n"
		else:
			chaine += caractere + " " * (i - 1) + caractere + "\n"
	
	return chaine
	

# [Fin] Definition des fonctions


# Programme principal

# Saisie du nombre de ligne du triangle
verif = False
while not verif: # Verification du nombre de lignes (entre 4 et 10)
	nbLignes = int(input("Nombre de lignes (entre 4 et 10) : "))
	if nbLignes >= 4 and nbLignes <= 10:
		verif = True
	else:
		print("On attend un nombre entre 4 et 10")

# Saisie du caractere pour le trace du triangle
verif = False
while not verif: # Verification de la saisie d'un unique caractere
	caractere = str(input("Caractère de dessin : "))
	if len(caractere) == 1:
		verif = True
	else:
		print("Veuillez re-saisir un caractère (taille limitée a un 1)")

# Appel de la fonction pour dessiner le triangle rectangle creux dont la nombre de lignes et le caractere d'affichage ont ete definis precedement
print(trianglerectanglecreux(nbLignes, caractere))

# [Fin] Programme principal

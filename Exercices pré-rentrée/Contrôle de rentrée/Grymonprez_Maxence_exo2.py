#!/usr/bin/python3
# -*- coding: utf-8 -*-

#########################################################
#
#	Auteur : 	Grymonprez Maxence
#
#	Titre : 	Afficher l'alphabet bizarrement
#
#########################################################


"""
Consigne :

Écrire un programme qui :
	demande à l'utilisateur s'il veut afficher l'alphabet en majuscule ou en minuscule ;
	demande à l'utilisateur un entier N compris entre 3 et 5 ;
	affiche l'alphabet à partir de a ou A mais en ne retenant qu'une lettre sur N.

Attention : 

là aussi les deux saisies seront "blindées", c'est-à-dire que l'utilisateur est contraint de saisir jusqu'à ce que son choix soit valide :
	M ou m pour Majuscule/minuscule
	3, 4 ou 5 pour l'écart.
"""


# Import des modules complementaires Python

import string

# [Fin] Import des modules complementaires Python


# Programme principal

# Alphabet en minuscule dans une liste 
alphabet = list(string.ascii_lowercase)

# Saisie du format majuscule ou minuscule
verif = False
while not verif: # Verification de la saisie ("M" ou "m")
	formatLettre = str(input("Majuscule ou minuscule M/m : "))
	if formatLettre in ["M","m"]: # La saisie est bien "M" ou "m"
		verif = True
	else: 
		print("On attend M ou m")

# Saisie de l'ecart entre les lettre
verif = False
while not verif:
	ecart = int(input("Une lettre sur combien (entre 3 et 5) : ")) 
	if ecart >= 3 and ecart <= 5:
		verif = True
	else: 
		print("On attend un écart entre 3 et 5")

# Affichage de l'alphabet en fonction du format des lettres et de l'ecart
i = 0
chaineResultat = str()
while i < len(alphabet):
	if formatLettre == "M": # Affichage en majuscule
		chaineResultat += alphabet[i].upper()
	else: # Affichage en minuscule
		chaineResultat += alphabet[i]
	i += ecart
print(chaineResultat)

# [Fin] Programme principal

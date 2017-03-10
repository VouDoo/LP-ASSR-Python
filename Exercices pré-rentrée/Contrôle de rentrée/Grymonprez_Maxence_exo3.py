#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
#
#	Auteur : 	Grymonprez Maxence
#
#	Titre : 	Concaténer trois listes en alternant
#
##############################################################


"""
Consigne :

Écrire un programme qui concatène 3 listes en alternant leurs éléments puis affiche la liste concaténée.

Par exemple si :
	L1 = [ "homer" ,  "bart" ,  "marge" ,  "liza" ]
	L2 = [ 1 , 2 , 3 , 5 , 8 , 13 , 21 , 44 ]
	L3 = [ 1.0 , 1.11 , 1.222 , 1.3333 , 1.44444 , 1.555555 ]
Alors la liste concaténée est :
	[ 'homer' , 1 , 1.0 , 'bart' , 2 , 1.11 , 'marge' , 3 , 1.222 , 'liza' , 5 , 1.3333 , 8 , 1.44444 , 13 , 1.555555 , 21 , 44 ]

Les 3 listes L1, L2 et L3 ci-dessus seront écrites en dur en tête de programme. Inutile de demander à l'utilisateur d'en saisir d'autres.
"""


# Programme principal

print("### Concatenation de listes ###")

# Initialisation des listes
listes = ["homer", "bart", "marge", "liza"], [1, 2, 3, 5, 8, 13, 21, 44], [1.0, 1.11, 1.222, 1.3333, 1.44444, 1.555555] # Listes a traiter
listeConcatenee = list() # Liste resultante

# Affichage des listes initiales
print("\nAffichage des listes initiales :")
for liste in listes:
	print(liste)

# Definition de la liste la plus grande
maxLongueur = 0
for liste in listes:
	if len(liste) > maxLongueur:
		maxLongueur = len(liste)

# Concatenation de la liste
for i in range(0, maxLongueur):
	for liste in listes:
		if liste:
			listeConcatenee.append(liste.pop(0))

# Affichage de la liste concatenee
print("\nAffichage de la liste concatenée :\n", listeConcatenee)

# [Fin] Programme principal
		
		

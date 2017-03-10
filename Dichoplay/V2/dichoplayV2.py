# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title:		Dichoplay V2
# Author:      	Grymonprez Maxence
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

from random import randint
import os

# Functions

def recapitulatif(nomNiveau, nbMin, nbMax, nbEssais):
	"""
		Affiche le recapitulatif de la partie de dichoplay.
		
		Utilise la fonction "print()" pour afficher le recapitulatif dans un format specifique.
		
		:param nomNiveau: 	Nom du niveau de la partie
		:param nbMin:		Nombre minimum de la plage
		:param nbMax:		Nombre maximum de la plage
		:param nbEssais:	Nombre d'essais pour trouver le nombre
		
		:type nomNiveau:	string
		:type nbMin:		int
		:type nbMax:		int
		:type nbEssais:		int
		
		:return:			(null)
		
		:Example:
		
		>>> recapitulatif("Facile", 0, 100, 10)
		#------------ Récapitulatif ------------#
		Niveau : Facile
		Nombre compris entre 0 et 100
		Nombre d'essais disponibles : 10
		#---------------------------------------#
	"""
	
	print(
"""#------------ Récapitulatif ------------#
Niveau : {}
Nombre compris entre {} et {}
Nombre d'essais disponibles : {}
#---------------------------------------#""".format(nomNiveau, nbMin, nbMax, nbEssais))

def clear():
	"""
		Effacer les entrees de la console.
		
		S'adapte aux systèmes Linux ou Windows.
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

# Main

if __name__ == '__main__':
	print(
"""Auteur : Grymonprez Maxence\n
*******************
*    DICHOPLAY    *
*******************""")
	
	# Definition du dictionnaire des plages pour les niveaux de jeu
	plagesNiv = {
		1: {
			'niv': "Facile",
			'min': 0,
			'max': 100
		},
		2: {
			'niv': "Normal",
			'min': 0,
			'max': 500
		},
		3: {
			'niv': "Difficile",
			'min': 0,
			'max': 1000
		},
		4: {
			'niv': "\"It's over 9000\"", 
			'min': 0, 
			'max': 9000
		},
		5: {
			'niv': "Bienvenue en Enfer",
			'min': 666,
			'max': 666666
		}
	}
	
	# Affichage des plages existantes dans le dictionnaire
	print("\nPlages disponibles pour la génération du nombre :")
	for k in plagesNiv.keys():
		print("\tPlage ", k, " : ", plagesNiv.get(k)['niv'], " (", plagesNiv.get(k)['min'], "-", plagesNiv.get(k)['max'], ")", sep='')
	
	# Choix d'une plage par l'utilisateur
	niveau = int(input("\nEntrez le numero de la plage : "))
	while not niveau in plagesNiv: # Si la plage saisie ne fait pas partie du dictionnaire
		niveau = int(input("Incorrect, re-entrez le numero de la plage : "))
	
	# Generation du nombre aleatoire
	minRand = plagesNiv[niveau]['min']
	maxRand = plagesNiv[niveau]['max']
	nbAleaObjectif = randint(minRand, maxRand)
	
	# Choix du nombre d'essais par l'utilisateur
	nbEssais = int(input("\nVeuillez choisir un nombre d'essais : "))
	while not nbEssais > 0:
		print("Le nombre doit être strictement superieur à zéro")
		nbEssais = int(input("Veuillez re-choisir un nombre d'essais : "))
	
	# Deroulement du jeu
	nb, encInf, encSup = int(), int(), int()
	res = str()
	for i in range(0, nbEssais):
		# Affichage du recapitulatif
		clear()
		recapitulatif(plagesNiv[niveau]['niv'], minRand, maxRand, nbEssais)

		# Affiche l'essai precedent (sauf pour le premier essai)
		if nb and res:
			# Affiche le nombre precedent
			print("\nChoix précédement :", nb)
			# Affiche un commentaire sur ce nombre
			print("\t\\__", res)
			# Affiche l'encadrement du nombre
			if encSup:
				print("\nEncadrement actuel du nombre :", "[{} - Objectif - {}]".format(encInf, encSup))
			else:
				print("\nEncadrement actuel du nombre :", "[{} - Objectif - {}]".format(encInf, maxRand))
		
		# Saisie d'un nombre par l'utilisateur
		print("\n--- Essai n°", i + 1, " ---", sep='')
		nb = int(input("\nEntrez un nombre : "))
		while not nb in range(minRand, maxRand + 1):
			nb = int(input("Nombre hors plage, re-entrez un nombre : "))
		if nb < nbAleaObjectif: # Nombre saisi plus petit que le nombre a trouver
			if encInf:
				if (nbAleaObjectif - nb) < (nbAleaObjectif - encInf):
					encInf = nb
			else:
				encInf = nb
			res = "Le nombre est trop PETIT"
		elif nb > nbAleaObjectif: # Nombre saisi plus grand que le nombre a trouver
			if encSup:
				if (nb - nbAleaObjectif) < (encSup - nbAleaObjectif):
					encSup = nb
			else:
				encSup = nb
			res = "Le nombre est trop GRAND"
		else: # Nombre saisi identique au nombre a trouver
			clear()
			if i == 0: # Nombre trouve en un essai
				print("Quelle chance ! Vous avec trouvé le nombre du premier coup !")
			else: # Nombre trouve en plusieurs essais
				print("Bravo ! Vous avec trouvé le nombre", nbAleaObjectif, "en", i + 1, "coups")
			break
		# Si le nombre n'a pas ete trouve au dernier essai, on affiche un message
		if i == nbEssais - 1:
			clear()
			print("Vous avez echoué... Le nombre était", nbAleaObjectif)

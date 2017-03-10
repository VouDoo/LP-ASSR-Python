# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title:		Dichoplay V1
# Author:      	Grymonprez Maxence
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

from random import randint

if __name__ == '__main__':
	nbrToFind = randint(0,100)
	print("Vous devez trouver le nombre en dix essais maximum")
	for i in range(0, 10):
		print("\nEssai", i + 1)
		nbr = int(input("\tEntrez un nombre:"))
		if nbr < nbrToFind:
			print("Le nombre entré est trop PETIT")
		elif nbr > nbrToFind:
			print("Le nombre entré est trop GRAND")
		else:
			print("\nVous avec trouvé le nombre en", i + 1, "coups !")
			break
		if i == 9:
			print("\nVous avez echoué... Le nombre était", nbrToFind)

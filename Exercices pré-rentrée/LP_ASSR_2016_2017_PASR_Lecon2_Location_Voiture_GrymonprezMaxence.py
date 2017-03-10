#################################################
# Auteur : Grymonprez Maxence
# Date : 23/08/2016
#
# Lecon 2 - Les structures conditionnelles
# Exercice "Location de voitures"
#################################################


""" *** Objectif de l'exercice ***
Un organisme de location de voitures propose à ses clients 2 tarifs :
	tarif essence :
		location : 40 Euros / jour
		kilométrage : 15 cts / km
	tarif diesel :
		location : 50 Euros / jour
		kilométrage : 10 cts / km
On entrera dans cet ordre la distance à parcourir et la durée de la location. Ce sont deux entiers.
Puis le programme produira un état de sortie détaillé indiquant le meilleur choix.
"""


### [Debut] Imports des modules Python complementaires ###
"""
    Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###


### [Debut] Programme principal ###

# Messsage introductif
print("""\
************************
* Location de voitures *
************************\n
Ce programme permet de comparer deux tarifs diponibles dans un agence de location de voitures\n
Veuillez saisir les donnees suivantes afin d'effectuer la comparaison tarifaire :""")

# Premierement, l'utilisateur entre le nombre de kilometres et le nombre de jours
# Remarque : ces deux valeurs sont des nombres entiers
distance = int(input("\tNombre de kilometres : ")) # Saisie du nombre de kilometres
nbrJours = int(input("\tNombre de jours : ")) # Saisie du nombre de jours

# On affiche la phrase qui recapitule les saisies de l'utilisateur
print("\nPour", nbrJours, "jours et", distance, "km")

# Calcul "tarif essence"
"""
Rappel :
	location : 40 Euros / jour
	kilométrage : 15 cts / km
"""
tarifEssence = 40 * nbrJours # Le prix pour le nombre de jours souuhaite pour un vehicule a essence
tarifEssence += 0.15 * distance # On additionne au resultat precedent le prix pour le nombre de kilometres souuhaite (toujours pour un vehicule a essence)

# Calcul "tarif diesel"
"""
Rappel :
	location : 50 Euros / jour
	kilométrage : 10 cts / km
"""
tarifDiesel = 50 * nbrJours # Le prix pour le nombre de jours souuhaite pour un vehicule diesel
tarifDiesel += 0.10 * distance # On additionne au resultat precedent le prix pour le nombre de kilometres souuhaite (toujours pour un vehicule diesel)

# On affiche les valeurs trouvees des calculs des deux tarifs proposes
print("avec un véhicule à essence :", tarifEssence)
print("avec un véhicule diesel :", tarifDiesel)

# On compare les valeurs des deux tarifs afin de conseiller l'utilisateur
if tarifEssence < tarifDiesel : # Tarif essence plus aventageux
	print("Véhicule à essence conseillé")
elif tarifDiesel < tarifEssence : # Tarif diesel plus aventageux
	print("Véhicule diesel conseillé")
else : # Les deux tarifs au meme prix
	print("Véhicule diesel et essence au même prix")

### [Fin] Programme principal ###

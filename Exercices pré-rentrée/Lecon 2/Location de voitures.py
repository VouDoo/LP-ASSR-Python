# Lecon 2 - Les structures conditionnelles
# Exercice "Location de voitures"

distance = int(input()) # Saisie du nombre de kilometres
nbrJours = int(input()) # Saisie du nombre de jours

print("Pour", nbrJours, "jours et", distance, "km")

# Calcul tarif essence
tarifEssence = 40 * nbrJours + 0.15 * distance
print("avec un véhicule à essence :", tarifEssence)

# Calcul tarif diesel
tarifDiesel = 50 * nbrJours + 0.10 * distance
print("avec un véhicule diesel :", tarifDiesel)

if tarifEssence < tarifDiesel : # Tarif essence plus aventageux
	print("Véhicule à essence conseillé")
elif tarifDiesel < tarifEssence : # Tarif diesel plus aventageux
	print("Véhicule diesel conseillé")
else : # Les deux tarifs au meme prix
	print("Véhicule diesel et essence au même prix")

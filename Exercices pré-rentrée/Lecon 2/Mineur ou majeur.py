# Lecon 2 - Les structures conditionnelles
# Exercice "Mineur ou majeur"

ageUtilisateur = int(input())

print("Vous avez", ageUtilisateur, "ans.", end = ' ')
if ageUtilisateur < 18 :
	print("Vous êtes mineur.")
else :
	print("Vous êtes majeur.")

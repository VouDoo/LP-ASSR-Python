# Lecon 1 - Afficher, saisir, variables, calculs
# Exercice "Soldes"
# Version 2

# Imports des modules python complementaires
from decimal import *

# Saisies des donnees par l'utilisateur : prix initial de l'article et son pourcentage de solde
prixInitial = Decimal(input())
pourcentageSolde = int(input())
print("Pour un article à un prix initial de", prixInitial, "€ et soldé à", pourcentageSolde, "% :")

# Calcul du pourcentage de reduction
montantReduction = Decimal(prixInitial * pourcentageSolde / 100).quantize(Decimal('.01'), rounding=ROUND_DOWN)
print("Le montant de la réduction est", montantReduction, "€.")

# Calcul du prix solde
prixSolde = Decimal(prixInitial - montantReduction).quantize(Decimal('.01'), rounding=ROUND_DOWN)
print("Le prix soldé est", prixSolde, "€.")

# Lecon 1 - Afficher, saisir, variables, calculs
# Exercice "Soldes"
# Version 1

# Saisies des donnees par l'utilisateur : prix initial de l'article et son pourcentage de solde
prixInitial = float(input())
pourcentageSolde = int(input())
print("Pour un article à un prix initial de", prixInitial, "€ et soldé à", pourcentageSolde, "% :")

# Calcul du pourcentage de reduction
montantReduction = int(prixInitial * pourcentageSolde) / 100
print("Le montant de la réduction est", montantReduction, "€.")

# Calcul du prix solde
prixSolde = int((prixInitial - montantReduction) * 100) / 100
print("Le prix soldé est", prixSolde, "€.")



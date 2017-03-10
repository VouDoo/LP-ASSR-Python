# Lecon 2 - Les structures conditionnelles
# Exercice "Assurance auto"

# Saisie du montant des reparations
montantRep = float(input())

# Calcul de la franchise de l'assure et du remboursement de l'assureur
pourcentFranch = 10 # Pourcentage de la franchise (ici 10%)
franchAsr = montantRep * pourcentFranch / 100 # Franchise de l'assure
if montantRep <= 150 : # Si le montant est inferieur ou egal a 150 euros, l'assuré paye la totalite des reparations
	franchAsr = montantRep
	rembAsr = float(0)
else : # Sinon on calcule le remboursement de l'assurance
	if franchAsr < 150 : # Si la franchise est inferieure a 150 euros, on la fixe a 150 euros
		franchAsr = 150
	elif franchAsr > 450 : # Si la franchise est superieure a 450 euros, on la fixe a 450 euros
		franchAsr = 450
	rembAsr = montantRep - franchAsr # calcul du remboursement de l'assureur a l'aide de la franchise calculee precedement

# Affichage du montant des reparations
print("Montant des réparations :", montantRep)
# Affichage de la franchise de l'assure
print("Franchise assuré :", franchAsr)
# Affichage du remboursement de l'assureur
print("Remboursement assureur :", rembAsr)

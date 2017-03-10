# Lecon 2 - Les structures conditionnelles
# Exercice "Changement de casse"

# Saisie du caractere par l'utilisateur
carac = str(input())
caracASCII = ord(carac) # Code ASCII du caractere

if caracASCII >= ord("A") and caracASCII <= ord("Z") : # majuscule
	print("Vous avez saisi la lettre majuscule ", carac, ".", sep="")
	print("Après transformation en minuscule, on obtient la lettre ", carac.lower(), ".", sep ='')

elif caracASCII >= ord("a") and caracASCII <= ord("z") : # minuscule
	print("Vous avez saisi la lettre minuscule ", carac, ".", sep="")
	print("Après transformation en majuscule, on obtient la lettre ", carac.upper(), ".", sep='')	

else :
	print("Vous avez saisi le caractère ", carac, ", ce n'est pas une lettre.", sep ='')
	

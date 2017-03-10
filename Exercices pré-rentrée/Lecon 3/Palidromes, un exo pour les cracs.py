###############################
# Lecon 3 - Les fonctions
# Exercice "Palidromes, un exo pour les cracs...."
# Auteur : Grymonprez Maxence
###############################

""" 'Palidromes, un exo pour les cracs.py' : Ce programme permet de saisir une chaine de caractere et de savoir si cette derniere est un palindrome ou non """

# Imports des modules Python complementaires
"""	
	Aucun module a importer
"""

### Definition des fonctions ###

def palindrome (chaineATester) : 
	"""
	Cette fonction permet de savoir si une chaine de caractere (ou mot) est un palindrome ou non
	Entrees :
	   chaineATester : chaine de caractere (ou mot) a tester
	Sorties :
	   Booleen ("True" ou "False")
	Mecanismes :
	   Fonction dite "recursive"
	"""
	if len(chaineATester) < 2 : # Si le reste de lettre a tester est strictement inferieur a 2, le mot est un palindrome
		return True
	else :
		if chaineATester[0] == chaineATester[-1]] : # Si la premiere et la derniere lettre de la chaine de caractere sont identiques
			return palindrome(chaineATester[1:-1]) # Appel de la meme fonction (fonction "recursive"), on passe en parametre la chaine de caractere en suprimant les deux lettres deja testees auparavant (premiere lettre et derniere lettre de la chaine de caractere sont supprimees)
		else : # Sinon, La chaine de caractere n'est pas un palindrome
			return False 

### [Fin] Definition des fonction ###

### Programme principal ###

# Saisie de la chaine de caracteres a tester
chaineDeCarac = str(input()) # Variable de chaine de caractere affectee suite a la saisie de l'utilisateur

# Test de la chaine de caracteres
testPalindrome = palindrome (chaineDeCarac) # Variable affectee suite a l'appel de la fonction "palindrome"
if testPalindrome is True : # La chaine de caracteres testee est un palindrome
	print(chaineDeCarac, "est un palindrome")
else : # La chaine de caracteres testee n'est pas un palindrome
	print(chaineDeCarac, "n'est pas un palindrome")

### [Fin] Programme principal ###

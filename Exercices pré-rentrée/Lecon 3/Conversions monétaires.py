# Lecon 3 - Les fonctions
# Exercice "Conversions monétaires"

def convert(somme, devise) :
	somme = float(somme)
	euroToDollar = 1.11595 # (au 12/8/2015)
	euroToLivre = 0.715135 # (au 12/8/2015)
	if devise == '€' :
		euro = somme
		dollar = euro * euroToDollar
		livre = euro * euroToLivre
	elif devise == '$' : # Si la devise est en dollar
		dollar = somme
		euro = dollar / euroToDollar
		livre = euro * euroToLivre
	elif devise == '£' :
		livre = somme
		euro = livre / euroToLivre
		dollar = euro * euroToDollar
	else :
		print("Erreur : devise inconnue")
		return "(devise Inconnue)"
	return euro, dollar, livre

somme = float(input())
devise = str(input())
euro, dollar, livre = convert(somme, devise)

print("Euro :", euro)
print("Dollar :", dollar)
print("Livre :", livre)


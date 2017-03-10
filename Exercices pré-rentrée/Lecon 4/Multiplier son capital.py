#################################################
# Auteur : Grymonprez Maxence
# Date : 30/08/2016
#
# Lecon 3 - Les boucles
# Exercice "Multiplier son capital !!!"
#################################################


""" *** Objectif de l'exercice ***
Ecrire un programme qui attend dans cet ordre :
    Un capital initial C0
    Un taux d'intérêt annuel T
    Un coefficient multiplicateur M
Le programme retourne le nombre d'années N nécessaires pour que le capital soit multiplié par M ainsi que le capital obtenu après ces N années.
"""


### [Debut] Imports des modules Python complementaires ###
"""
Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###


### [Debut] Definition des fonctions ###

# Fonction "multiCapital"
def multiCapital(capitalInit, taux, coeff) :
    """
    Description :
        La fonction retourne le nombre d'années nécessaires pour que le capital soit multiplié par un coefficient donne ainsi que le capital obtenu après ces années.
    Entrees :
        - capitalInit (integer) : Capital initial
        - taux (float) : Taux d'intérêt annuel
        - coeff (integer) : Coefficient multiplicateur
    Sorties :
	- nbAnnees (integer) : Nombre d'années nécessaires pour que le capital (var. "capital") soit multiplié par le coefficient (var. "coeff")
        - capitalResult (integer) : Capital obtenu après ces années (var. "nbAnnees")
    """

    # Initialisation des variables
    capitalInit = int(capitalInit)
    taux = float(taux)
    coeff = int(coeff)
    nbAnnees = 0 # Nombre d'annees necessaires afin d'obtenir le capital initial multiplié par le coefficient souhaite
    capitalResult = capitalInit # Capital resultant de ce meme nombre d'annees ecoulees

    # Calcul du nombre d'annees afin d'obtenir le capital multiplie par le coefficient souhaite
    while capitalResult < capitalInit * coeff : # Tant que le capital resultant est inferieur au capital initial multiplie par le coefficient
        nbAnnees += 1 # Ajout d'une annee
        capitalResult += capitalResult * taux # Calcul du nouveau capital de l'annee suivante avec le taux d'interet

    # Retour des resultats obtenus
    return int(nbAnnees), int(capitalResult)

### [Fin] Definition des fonctions ###


### [Debut] Programme principal ###

# Saisie par l'utilisateur des differentes informations necessaires au calcul
capitalInit = int(input()) # Saisie du capital initial
tauxInteret = float(input()) # Saisie du taux d'intérêt annuel
coeffMutlti = int(input()) # Saisie du coefficient multiplicateur

# Appel de la fonction "multiCapital" avec en parametre le capital initial, le taux d'intérêt annuel et le coefficient multiplicateur
nbAnnees, capitalResult = multiCapital(capitalInit, tauxInteret, coeffMutlti) # On stocke les resultats dans deux variables

# Affichage du recapitulatif des saisies de l'utilisateur ainsi que des resultats obtenus suite a l'appel de la fonction "multiCapital"
print('''\
Capital initial : {}
Taux : {} %
Apres {} ans, votre capital aura été multiplié par {}
Vous disposerez alors de {}\
'''.format(capitalInit, tauxInteret * 100, nbAnnees, coeffMutlti, capitalResult)) # Remarque : Affichage du taux d'interet en pourcentage (%)

### [Fin] Programme principal ###

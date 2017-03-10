#############################################################
# Auteur : Grymonprez Maxence
# Date : 04/09/2016
#
# Lecon 5 - Les listes
# Exercice "Supprimer les mots contenant une voyelle donnee"
#############################################################


""" *** Objectif de l'exercice ***
Ecrire un programme qui attend une liste L de chaines de caractères et une voyelle V et qui supprime de la liste L toutes les chaines contenant la voyelle V.
On entrera successivement :
    le nombre de valeurs de la liste,
    les valeurs de la liste,
    la voyelle V.
Puis le programme affichera la liste finale au format habituel.
On attend simplement l'instruction print (L)
"""


### [Debut] Imports des modules Python complementaires ###
"""
Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###


### [Debut] Definition des fonctions ###

## Fonction "majusculerListe"
def majusculerListe(listeInit) :
    """
    Description :
        Cette fonction permet de majusculer tous les elements d'une liste
    Entrees :
        listeInit (Liste de chaines de caracteres) : Liste des chaines de caracteres a majusculer
    Sorties :
        listeResult (Liste de chaines de caracteres) : Liste modifiee suite a la mise en majuscule des elements de la liste initiale
    """
    
    # Initialisation des variables
    listeResult = [] # Initialisation de la liste pour le resultat de la majusculisation
    
    for element in listeInit : # Pour chaque element de la liste initiale ...
        listeResult.append(element.upper()) # On l'ajoute dans la nouvelle liste sous forme majuscule
    
    return listeResult

## Fonction "verifierVoyelle"
def verifierVoyelle(lettre) :
    """
    Description :
        Cette fonction permet de verifier si une lettre est une voyelle
    Entrees :
        lettre (Chaine de caracteres) : Lettre a verifier
    Sorties :
        (Booleen) : La lettre est une voyelle ou non (valeur egale a "True" ou "False")
    Mecanismes :
        On verifie si la lettre appartient a l'ensemble des voyelles minuscules et majuscules
    """
    
    # Definition des ensembles pour les voyelles de l'alphabet
    ensVoy = set(["a", "e", "i", "o", "u", "y"]) # Ensemble des voyelles (par defaut en minuscule)
    ensVoyMaj = set(majusculerListe(ensVoy)) # Ensemble des voyelles en majuscule
    
    if lettre in ensVoy | ensVoyMaj : # Si la lettre appartient a l'ensemble des voyelles minuscule et des voyelles majuscules (union des deux ensembles) ...
        return True # La lettre est une voyelle
    else : # Sinon ...
        return False # La lettre n'est pas une voyelle

## Fonction "saisirVoyelle"
def saisirVoyelle() :
    """
    Description :
        Cette fonction permet de saisir une voyelle
    Entrees :
        (Aucune)
    Sorties :
        lettre (Liste de chaines de caracteres) : Voyelle saisie et verifiee
    Mecanismes :
        On appelle la fonction "verifVoyelle" pour verifier si la la saisie de la voyelle est correcte
        Une fois que la lettre saisie est verifiee, on la retourne
    """
    
    # Saisie de la lettre par l'utilisateur
    lettre = str(input("Veuillez entrer une voyelle : "))
    # Verification si la lettre saisie est une voyelle
    verifVoy = verifierVoyelle(lettre)
    
    while verifVoy != True : # Tant que la lettre saisie n'est pas une voyelle
        # Affichage d'un message d'erreur
        print("Erreur : Vous n'avez pas saisie une voyelle ...")
        # Demande a nouveau la saisie de la voyelle a l'utilisateur
        lettre = str(input("Veuillez entrer a nouveau une voyelle : "))
        # Verification si la lettre saisie precedement est une voyelle
        verifVoy = verifierVoyelle(lettre)
    
    return lettre

## Fonction "supprVoyListe"
def supprVoyListe(listeInit, voyelle) :
    """
    Description :
        Cette fonction permet de supprimer les chaines de caracteres d'une liste contenant une voyelle specifique
    Entrees :
        listeInit (Liste de chaines de caracteres) : Liste de chaines de caracteres a traiter
        voyelle (chaine de caracteres) : voyelle utile au traitement de la liste
    Sorties :
        listeResult (Liste de chaines de caracteres) : Liste traitee suite a la suppression des mots contenant la voyelle
    Mecanismes :
        On parcourt la liste dans le sens inverse en commencant par la fin et on supprime les chaines de caracteres (ou elements) de la liste contenant la voyelle specifique
    """
    
    # Initialisation des variables
    i = len(listeInit) # L'indice i prend la valeur du nombre d'elements de la liste initiale
    listeResult = list(listeInit) # Copie de la liste initiale

    while i != 0 : # Tant que indice i est superieur a 0
        if voyelle.lower() in listeResult[i - 1] or voyelle.upper() in listeResult[i - 1] : # Si la voyelle (minuscule ou majuscule) est contenue dans la chaine de caracteres de l'element ... 
            del listeResult[i - 1] # On supprime l'element
        i -= 1 # On decremente l'indice pour passer a l'element suivant (element positionne avant dans la liste)
        
    return listeResult # Retour de la liste sans les mots contenant la voyelle

### [Fin] Definition des fonctions ###


### [Debut] Programme principal ###

# Message introductif
print("""\
***************************************************
* Supprimer les mots contenant une voyelle donnee *
***************************************************\n
Ce programme permet de supprimer toutes les chaines de caracteres d'une liste contenant une voyelle specifique\n
Veuillez saisir les donnees suivantes afin de proceder a l'operation :\n""")

# Initialisation des variables
listeInitiale = [] # Initialisation de la liste initiale (liste vide)

# Saisies de l'utilisateur
nbValListe = int(input("Taille de la liste de chaines de caracteres initiale : ")) # Saisie du nombre de valeurs de la liste
print("Valeur des elements de la liste : ")
for i in range(0, nbValListe) :
    print("\t", i + 1, ": ", end = '')
    listeInitiale.append(str(input())) # Saisie des chaines de caracteres a importer dans la liste
voyelle = saisirVoyelle() # Saisie de la voyelle par appel de la fonction "saisirVoyelle"

# Appel de la fonction "supprVoyelle()"
listeFinale = supprVoyListe(listeInitiale, voyelle) # On stocke la nouvelle liste dans la variable "listeFinale"

# Affichage de la liste initiale
print("\nListe initiale :\n", ", ".join(listeInitiale), sep='', end='\n\n')
# Affichage de la liste finale
print("Liste obtenue suite a la suppression des mots contenant la voyelle \"", voyelle, "\" :\n", ", ".join(listeFinale), sep='', end='\n\n')
# Affichage du nombre d'elements supprimes
print("Nombre d'elements supprimes :", len(listeInitiale) - len(listeFinale))

### [Fin] Programme principal ###

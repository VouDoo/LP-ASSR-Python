#################################################
# Auteur : Grymonprez Maxence
# Date : 22/08/2016
#
# Lecon 1 - Afficher, saisir, variables, calculs
# Exercice "La recette des crepes"
# 'LP_ASSR_2016_2017_PASR_Lecon1_Recette_Crepes_GrymonprezMaxence.py' : Ce programme permet d'afficher la recette des crepes en fonction d'un nombre de personne fourni par l'utilisateur
#################################################

""" --- Objectif de l'exercice ---
Ecrire un programme qui adapte la recette des crepes a un nombre de personnes quelconque.
Le programme attendra ce nombre de personnes et affichera la liste des ingredients.
"""

### Imports des modules Python complementaires ###
"""
    Aucun module a importer
"""
### [Fin] Imports des modules Python complementaires ###

### Programme principal ###

# Messsage introductif
print("""\
*************************
* La Recette des crepes *
*************************\n""")

# Saisie du nombre de personnes par l'utilisateur
nbr_personnnes = int(input("Nombre de personne : ")) # Nombre entier

if nbr_personnnes == 0 : # Si la valeur entree par l'utilisateur est nulle, on affiche un message d'erreur

    print("Erreur de saisie : Le nombre de personnes ne peut pas etre nul !")

else : # Sinon, on precede aux calculs et a l'affichage de la recette

    # Definition des quantites des ingredients
    """
    Pour une personne, la recette doit comporter les quantites suivantes :
       31,25 g de farine
       1 oeuf (On prend 0,5 oeufs pour effectuer le calcul pour deux personnes ou plus)
       6.25 cl de lait
       1 pincee de sel (invariable selon le nombre de personne)
       6.25 g de beurre
       1.25 g de sucre vanillé
       1 cl de rhum (On prend 0.625 cl de rhum pour effectuer le calcul pour deux personnes ou plus)

    Remarque : en utilisant des integers (int), on arrondi a l'inferieur et a l'unite les nombres calcules.
    """
    qte_farine = int(nbr_personnnes * 31.25)
    qte_oeufs = int(nbr_personnnes * 0.5)
    if qte_oeufs < 1 :
        qte_oeufs = 1 # un oeuf minimum pour la recette
    qte_lait = int(nbr_personnnes * 6.25)
    qte_sel = 1 # "La pincee de sel sera immuable !"
    qte_beurre = int(nbr_personnnes * 6.25)
    qte_sucreVanille = int(nbr_personnnes * 1.25)
    nbr_sachetSucreVanille = qte_sucreVanille // 10 + 1
    qte_rhum = int(nbr_personnnes * 0.625)
    if qte_rhum < 1 :
        qte_rhum = 1 # un "cl de rhum" minimum pour la recette

    # Affichage de la recette avec les quantites calculees precedement
    print("\nPour", nbr_personnnes, "personnes il faut :")
    print(qte_farine, "g de farine")
    print(qte_oeufs, "oeufs")
    print(qte_lait, "cl de lait")
    print(qte_sel, "pincée de sel")
    print(qte_beurre, "g de beurre")
    print(qte_sucreVanille, "g de sucre vanillé")
    print(qte_rhum, "cl de rhum")

### [Fin] Programme principal ###

# Lecon 1 - Afficher, saisir, variables, calculs
# Exercice "Le motif Python dessine avec un caractere quelconque"

# Variable contenant le mot PYTHON
motPython = """\
****  *   *  *****  *   *  *****  *   *
*  *   * *     *    *   *  *   *  **  *
****    *      *    *****  *   *  * * *
*       *      *    *   *  *   *  *  **
*       *      *    *   *  *****  *   *"""

# Saisie d'une chaine de caracteres par l'utilisateur
caractereSelectionne = str(input())

"""
    On effectue une verification sur la taille de la chaine de caracteres saisie par l'utilisateur
    Si cette derniere est nulle (soit egale a zero), on affiche un message d'erreur et on clot le programme
    Sinon, on effectue l'affichage du mot "PYTHON" avec le caractere choisi
"""
if len(caractereSelectionne) == 0 :
    print("Aucun caractere n'a ete saisi par l'utilisateur")
else :
    caractereSelectionne = caractereSelectionne[0] # On prend le premier caractere de la chaine de caracteres entree par l'utilisateur
    print(motPython.replace('*', caractereSelectionne)) # On affiche le mot PYTHON avec le caractere choisi

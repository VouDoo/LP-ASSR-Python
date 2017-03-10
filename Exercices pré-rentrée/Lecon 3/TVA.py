# Lecon 3 - Les fonctions
# Exercice "TVA"

def calcPTTC(pht, tva) :
        """
        Calcul le prix TTC d'un article
        Entrees :
           pht : prix HT de l'article
           tva : taux TVA
        Sorties :
           Prix TTC de l'article
        """
        return float(pht * tva / 100 + pht)

prixHT = float(input()) # Prix HT de l'article
tauxTVA = float(input()) # taux de TVA

print("Le prix TTC d'un article de prix HT", prixHT, "au taux de TVA", tauxTVA, "% est", float(calcPTTC(prixHT, tauxTVA)))

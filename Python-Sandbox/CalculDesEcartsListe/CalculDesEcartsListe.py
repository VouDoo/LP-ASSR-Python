# Liste en desordre
listeDesordre = [500, 84, 56, 78, 98, 453, 1235, 95, 97, 99, 100]
print("Liste desordre : ", listeDesordre, " (taille : ", len(listeDesordre), ")", sep ='')
# Triage de la liste (du plus petit au plus grand) 
listeTriee = sorted(listeDesordre)
print("Liste triee : ", listeTriee, " (taille : ", len(listeTriee), ")", sep ='')
# Calcul des ecarts entre chaque element
listeDesEcarts = [listeTriee[i+1]-listeTriee[i] for i in range(len(listeTriee)-1)]
print("Liste des ecarts :", listeDesEcarts, " (taille : ", len(listeDesEcarts), ")", sep ='')
# Definition du plus grand et du plus petit ecart
print("Ecart maximum :", max(listeDesEcarts))
print("Ecart minimum :", min(listeDesEcarts))


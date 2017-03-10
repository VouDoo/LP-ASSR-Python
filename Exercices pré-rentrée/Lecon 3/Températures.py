# Lecon 3 - Les fonctions
# Exercice "Températures"

def statsTemperatures(temp) :
        """
        Etudie une liste de temperatures
        Entrees :
           phrase : liste de temperature
        Sorties :
           Rien (void)
        """
        minTemp = temp[0]
        maxTemp = temp[0]
        indMaxTemp = 0
        indMinTemp = 0
        sommeDesTemp = temp[0]

        # Determination du maximum et du minimum des temperatures et de la moyenne globale
        for i in range (1, len(temp)) :
                sommeDesTemp += temp[i]
                if temp[i] > maxTemp :
                        maxTemp = temp[i]
                        indMaxTemp = i
                if temp[i] < minTemp :
                        minTemp = temp[i]
                        indMinTemp = i
        moyGlobale = sommeDesTemp / (len(temp))
        print("Mini : ", minTemp, "\nMaxi : ", maxTemp, "\nMoyenne : ", moyGlobale, sep = '')

        # Determination de la moyenne corrigee des temperatures
        moyCorrigee = (sommeDesTemp - temp[indMaxTemp] - temp[indMinTemp]) / (len(temp) - 2)
        print("Moyenne corrigée :", moyCorrigee)

temperatures = [] # Liste des temperatures de la semaine a midi
for i in range (0, 7) :
        temperatures.append(int(input()))

statsTemperatures(temperatures)

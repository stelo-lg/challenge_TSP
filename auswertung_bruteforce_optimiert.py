#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from klassen import City, distanz

#TRAVELING SALESPERSON PROBLEM - HOW TO FIND THE SHORTEST WAY

df = pd.read_csv('msg_standorte_deutschland.csv')

#Überblick über den Datensatz verschaffen
#display (df)


#sns.set()
#ax = sns.scatterplot(x="Breitengrad", y="Längengrad", data=df)


# Die Daten aus der Tabelle (Pandas Datenframe) werden genutzt um für jede Stadt eine Klasse City zu erzeugen, die die Kooridinaten und die Nummer der Stadt enthält.

cities = []

# Permutation von 21 Städten ist schon nicht mehr möglich, da es einfach ewig dauert
# daher wird das Skript an dieser Stelle nur mit weniger Datensätzen getestet
#df2 = df.iloc[:4]

for row in df.itertuples():
    new = City(row.Längengrad, row.Breitengrad, row.Nummer, row.msg_Standort)
    cities.append(new)

# # All Tours Algorithm
# Es werden mittels Permutation alle möglichen Wege und deren Strecke berechnet. Anschließend wird der Weg mit der kleinsten Strecke ausgesucht. 
# Dabei handelt es sich um einen Lösungsweg, der zwar definitiv die kürzeste Strecke ermitteln wird, aber sehr ineffizient und langsam ist, insbesondere für große Datensätze. 


#Bei der Permutation wird die erste Stadt ausgelassen, da dort immer gestartet wird
#OPTIMIERUNG: Die Permutationen werden nicht alle in einer Liste gespeichert, sondern so wie von itertools zurück gegeben
#anschließend kann über alle Permutationen iteriert werden, ohne alle gleichzeitig in einer Liste zu speichern, somit wird ein MEMORY ERROR vermieden, die Laufzeit aber stark erhöht
permutation = itertools.permutations(cities[1:])

#es werden nun alle einzelnen Permutationen durchlaufen und die Distanz berechnet um das Minimum zu finden
optimum = []
#minimale Entfernung maximal groß setzen
min_entfernung = float("inf")
i = 0

for tour in permutation:
    i += 1
    print (str(i)+". Tour:")
    tour = (cities[0], ) + tour
    entfernung = 0
    for i in range(0, len(tour)):
    # wenn die letzte Stadt in der Liste erreicht ist, wird die Distanz zur Startstadt berechnet
        if i == len(tour)-1:
            entfernung += distanz(tour[i], tour[0])
        else:
            entfernung += distanz(tour[i], tour[i+1])
    #wenn eine neue minimale Entfernung gefunden wurde, wird dieser gespeichert
    print (str(round(entfernung, 2)))
    if entfernung < min_entfernung:
        print("Neues Optimum gefunden.")
        min_entfernung = entfernung
        optimum = list(tour)

print ("#########################################")
print ("Die kürzste Wegstrecke: " + str(min_entfernung))
#für die bessere Ausgabe an die Liste hinten noch mal die Startstadt anfügen

optimum.append(cities[0])

for city in optimum:
    print ((city.nummer, city.name))


plt.plot([p.x for p in optimum], [p.y for p in optimum], "bo-")
plt.savefig('optimum.png')




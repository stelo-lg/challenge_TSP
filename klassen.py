import math
import geopy.distance

#für jede Stadt wird eine Instanz der Klasse City angelegt die alle wichtigen Infos entählt
class City:
    def __init__(self, x, y, nummer, name):
        self.x = x
        self.y = y
        self.nummer = nummer
        self.name = name

#die Entfernung zwischen zwei Koordinaten in km berechnen
def distanz_km(stadt1, stadt2):
    coordinate1 = (stadt1.y, stadt1.x)
    coordinate2 = (stadt2.y, stadt2.x)
    
    return geopy.distance.distance(coordinate1, coordinate2).km

#Euklidische Berechnung des Abstands um den nearest neighbour zu finden
def distanz(stadt1, stadt2):
    #Berechnung des Abstands zwischen zwei Städten mit dem Satz des Pythagoras
    return math.sqrt((stadt1.x - stadt2.x)**2 + (stadt1.y - stadt2.y)**2 )


def neighbour(stadt, liste):
    #Berechnet die Entfernung einer Stadt zu allen in der liste aufgezählten Städte und gibt die mit der geringsten Entfenrung zurück
    entfernung = float("inf")
    for city in liste:
        #Distanz wird mit Satz des Pythaogras im Koordinatensystem berechnet
        nachbarschaft = distanz(stadt, city)
        if nachbarschaft < entfernung:
            entfernung = nachbarschaft
            nachbar = city
    return nachbar


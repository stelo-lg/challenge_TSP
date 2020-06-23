import math

class City:
    def __init__(self, x, y, nummer, name):
        self.x = x
        self.y = y
        self.nummer = nummer
        self.name = name
        
def distanz(stadt1, stadt2):
    #Berechnung des Abstands zwischen zwei Städten mit dem Satz des Pythagoras
    return math.sqrt((stadt1.x - stadt2.x)**2 + (stadt1.y - stadt2.y)**2 )

def neighbour(stadt, liste):
    #Berechnet die Entfernung einer stadt zu allen in der liste aufgezählten Städte und gibt die mit der geringsten Entfenrung zurück
    entfernung = float("inf")
    for city in liste:
        nachbarschaft = distanz(stadt, city)
        if nachbarschaft < entfernung:
            entfernung = nachbarschaft
            nachbar = city
    return nachbar, entfernung
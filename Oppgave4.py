# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:19:54 2025

@author: EMM
"""

data = {
        "Norge":["Oslo",0.634],
        "England:": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

sLandInn = input("Skriv inn landet du vil ha informasjon om: " )
if sLandInn in data:
    sHovedstad = data[sLandInn][0]
    fInnbyggere = data[sLandInn][1]
    print(sHovedstad, "er hovedstaden i", sLandInn, "og det er", fInnbyggere, "mill. innbyggere i", sHovedstad )
else:
    print("Data for", sLandInn, "er ikke oppgitt" )

sNyttLandInn = input("Skriv inn navn på landet du vil legge til: " )
sNyHovedstad = input("Skriv inn navn på hovedstaden i " + sNyttLandInn + ": ")
fNyInnbyggere = float(input("Skriv antall millioner innbyggere i " + sNyHovedstad + ": "))

data[sNyttLandInn] = [sNyHovedstad,fNyInnbyggere]
print(data[sNyttLandInn][0], "er hovedstaden i", sNyttLandInn, "og det er", data[sNyttLandInn][1], "mill. innbyggere i", data[sNyttLandInn][0] )




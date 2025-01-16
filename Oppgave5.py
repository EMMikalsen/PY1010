# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:39:39 2025

@author: EMM
"""
import numpy as np
from math import sqrt

def ArealOgOmkrets (fSide1, fSide2):
    """
    Beregning av areal og omkrets av en figur bestående av 
    en halvsirkel og en rettvinklet trekant
    
    fSide1 er diameteren i halvsirkelen og ene siden av trekanten
    fSide2 er den andre siden av trekanten
    
    """
    fArealSirkelDel = (np.pi * (fSide1/2)**2)/2
    fArealTrekant = (fSide1 * fSide2)/2
    fArealFigur = fArealSirkelDel + fArealTrekant
    
    fOmkretsHalvsirkel = fSide1 * np.pi
    fOmkretsTrekantDel = fSide2 + sqrt(fSide1**2 + fSide2**2)
    fOmkretsFigur = fOmkretsHalvsirkel + fOmkretsTrekantDel
    
    return [fArealFigur, fOmkretsFigur]

a = 2
b = 5

fAreal = ArealOgOmkrets(a, b)[0]
fOmkrets = ArealOgOmkrets(a, b)[1]

print("Arealet av figuren er", round(fAreal,2), "og omkretsen er", round(fOmkrets,2))

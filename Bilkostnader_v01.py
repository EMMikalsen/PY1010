# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:20:10 2024

@author: EMM
"""

iKjørelengde = 8000
iForsikringElBil = 5000
iForsikringBensinBil = 7500
fTrafikkforsikringPrÅr = 8.38*365
fDrivstoffBensinBil = 1.00*iKjørelengde
fDrivstoffElBil = 0.2*2.00*iKjørelengde
fBompengerElBil = 0.1*iKjørelengde
fBompengerBensinBil = 0.3*iKjørelengde
fKostnadElBil = iForsikringElBil + fTrafikkforsikringPrÅr + fDrivstoffElBil + fBompengerElBil
fKostnadBensinBil = iForsikringBensinBil + fTrafikkforsikringPrÅr + fDrivstoffBensinBil + fBompengerBensinBil
print("Årlige kostnader ElBil {0:.2f}".format(fKostnadElBil), "kroner")
print("Årlige kostnader BensinBil {0:.2f}".format(fKostnadBensinBil), "kroner")


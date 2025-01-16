# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:00:44 2025

@author: EMM
"""

import math

antall_elever = int(input('Skriv inn antall elever: ' ))

iAntallPizza = antall_elever / 4

print("Det må kjøpes", math.ceil(iAntallPizza), "pizzaer" )

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:10:07 2025

@author: EMM
"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet: ' ))
v_rad = v_grad*np.pi/180
print(v_grad, "grader er", round(v_rad,2), "radianer")

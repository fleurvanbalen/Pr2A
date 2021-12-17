## Importeren
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import os

## Functies
def TM(l,a,n):
    return np.exp(-a*(l/100)**n)

## Data
os.chdir('/home/thomasbaks/Documents/GitHub/Pr2A/A11')

Data = pd.read_excel('Data folder/3-4/Transmission_values_no_Cu_Al.xlsx')

print(Data)
nlpm = Data['n&l / pm'].values.tolist()
T_1 = Data['T_1 / %'].values.tolist()
T_2 = Data['T_2 / %'].values.tolist()

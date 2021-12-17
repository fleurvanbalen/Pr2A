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

print(max(T_1))
max_T_1 = 60
print(max_T_1)
print(nlpm[50])

## Fitten


a = 26
b = 57

c = 35
d = 50
cf_T1, covariance_T1 = curve_fit(TM, nlpm[c:d] ,T_1[c:d]) # R_func fitten (lineaire fit)
T1_cf = TM(nlpm_lin,cf_T1[0],cf_T1[1]) # Functie invullen voor lineaire fit


nlpm_lin = np.linspace(50,70)
## Plotten
plt.close()
plt.rcParams['figure.dpi'] = 100
plt.plot(nlpm,T_1,".",label = "Data")
plt.plot(nlpm_lin,T1_cf, label = 'FIT: $e^{-a(\\frac{l}{100})^n}$')
plt.xlabel(" $\\lambda \\cdot n$ (in pm)")
plt.ylabel("Transmission (in %)")
plt.legend()
plt.grid()
plt.show()
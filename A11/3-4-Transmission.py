## Importing Libarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import os

## Functions
def TM(l,a,n):
    return np.exp(-a*(l/100)**n) *100

## Data
os.chdir('/home/thomasbaks/Documents/GitHub/Pr2A/A11') #Changing the working directory

Data = pd.read_excel('Data folder/3-4/Transmission_values_no_Cu_Al.xlsx') #Fetching the Data


# Deviding the data
nlpm = Data['n&l / pm'].values.tolist()
T_1 = Data['T_1 / %'].values.tolist()
T_2 = Data['T_2 / %'].values.tolist()


## Curvefit

nlpm_lin = np.linspace(50,80)

a = 26 #The place in the vector at which T_1 nlpm equals 50
b = 57 #The place in the vector at which T_1 nlpm equals 80

#Check
#print(nlpm[a],nlpm[b])

cf_T1, covariance_T1 = curve_fit(TM, nlpm[a:b] ,T_1[a:b]) #Fitting T1 to TM
cf_T2, covariance_T2 = curve_fit(TM, nlpm[a:b] ,T_2[a:b]) #Fitting T2 to TM

T1_cf = TM(nlpm_lin,cf_T1[0],cf_T1[1]) #With found values: Continious T1
T2_cf = TM(nlpm_lin,cf_T2[0],cf_T2[1]) #With found values: Continious T2

#Priting found values in curvefit
print("Gevonden waarden:")
print("a_T_1 =", cf_T1[0])
print("n_T_1 =", cf_T1[1])
print()
print("a_T_2 =", cf_T2[0])
print("n_T_2 =", cf_T2[1])

## Graphs

#Boundaries of the Data points:
c = a
d = b

plt.close() #Closing the previous opend plot
plt.rcParams['figure.dpi'] = 100
plt.plot(nlpm[a:b],T_1[a:b],".",label = "Transmissie Al") #Plotting RAW data T1
plt.plot(nlpm[a:b],T_2[a:b],".",label = "Transmissie Cu") #Plotting RAW data T2
plt.plot(nlpm_lin,T1_cf, label = 'FIT $T_{Al}$: $e^{-a(\\frac{l}{100})^n}$') #Plotting curvefit T1
plt.plot(nlpm_lin,T2_cf, label = 'FIT $T_{Cu}$ : $e^{-a(\\frac{l}{100})^n}$') #Plotting curvefit T2
plt.xlabel(" $\\lambda \\cdot n$ (in pm)") #Plotting the x-axis
plt.ylabel("T (in %)") #Plotting the y-axis
plt.legend()
plt.grid()
plt.show()
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


## Calculating the erros

#Importing data
csv = pd.read_csv("Data folder/3-3/Bragg_data_emmissiespectrum.csv")

golflengte = csv['Golflengte'].values.tolist()
Inofilter = csv['Nofilter'].values.tolist()
Icu = csv['Cu'].values.tolist()
Ial = csv['Al'].values.tolist()
Ibackground = np.ones(len(Inofilter))*0.157

# error in Transmission
def function_eT(R,R0,R1):
    eT = []
    eR = eR0 = eR1 = 1
    for i in (range(len(R))):
        eT_i = np.sqrt( (eR1/(R0[i]-R[i]))**2 + (((R1[i]-R0[i])*eR)/(R0[i]-R[i])**2)**2 + (((R[i]-R1[i])*eR0)/(R0[i]-R[i])**2)**2  )
        eT.append(100*eT_i)
    return eT

#elambda = np.sqrt(-100(np.log(1/T))**(1/n)*(ea)**2/(n*a**(1+1/n)) + 100*T/(n*a**1/n)*(eT)**2 *log(1/T)**(1/n -1))


T_1_error = function_eT(Ibackground, Inofilter, Icu)
T_2_error = function_eT(Ibackground, Inofilter, Ial)

#print(T_1_error[26:57])

#error in Lambda

def function_el(l):
    el = []
    theta = []
    for i in range(len(l)):
        d = 5.6402 * 10**(-10)
        theta_i = np.arcsin(l[i]*10**(-12)/(2*d))
        etheta = 0.1 * np.pi/180
        el_i = np.sqrt((2*d*np.cos(theta_i)*etheta)**2)
        el.append(el_i*10**(12))
    return el

nlpm_error = function_el(golflengte)

print(nlpm_error)
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
print("a_T_1_Cu =", cf_T1[0])
print("n_T_1_Cu =", cf_T1[1])
print()
print("a_T_2_Al =", cf_T2[0])
print("n_T_2_Al =", cf_T2[1])

## Graphs

#Boundaries of the Data points:
c = a
d = b


plt.close() #Closing the previous opend plot
plt.rcParams['figure.dpi'] = 100
plt.errorbar(nlpm[a:b],T_1[a:b],T_1_error[a:b],nlpm_error[a:b],fmt='.', alpha = 0.5, ecolor = 'grey',label = "Transmissie Cu") #Plotting RAW data T1
plt.errorbar(nlpm[a:b],T_2[a:b],T_2_error[a:b],nlpm_error[a:b], fmt='.',alpha = 0.5, ecolor = 'grey',label = "Transmissie Al") #Plotting RAW data T2
plt.plot(nlpm_lin,T1_cf, label = 'FIT $T_{Cu}$: $e^{-a(\\frac{l}{100})^n}$') #Plotting curvefit T1
plt.plot(nlpm_lin,T2_cf, label = 'FIT $T_{Al}$ : $e^{-a(\\frac{l}{100})^n}$') #Plotting curvefit T2
plt.xlabel(" $\\lambda \\cdot n$ (in pm)") #Plotting the x-axis
plt.ylabel("T (in %)") #Plotting the y-axis
plt.legend()
plt.grid()
plt.show()
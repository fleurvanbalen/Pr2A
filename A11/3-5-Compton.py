## Importing
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import os

## Functions
def Dlambda(a,n,R0,R,R1,R2):
    return 100*(((np.log(R0-R)-np.log(R2-R))/(a))**(1/n)-((np.log(R0-R)-np.log(R1-R))/(a))**(1/n))

def Lambda(a, n, R0,R,Ri):
    return 100*((np.log(R0-R)-np.log(Ri-R))/(a))**(1/n)

me = 9.1 * 10**(-31) #kg
h  = 6.63 * 10**(-34) #J/Hz
c  = 2.9 * 10**8
def theory(theta):
    return h/(me*c) * (1-np.cos(theta))

## Data
os.chdir('/home/thomasbaks/Documents/GitHub/Pr2A/A11') #Just to be sure: Changing directories

#Found data
R0 = 15.22 #mean hits with no filter
Bg = 0.157 #mean hits with no cristal

    #With filters (R1 = filter on collimator, R2 = filter on GM-Tube)
Cu_R2 = np.array([1.367,1.581])
Cu_R1 = 2.476

Al_R2 = np.array([1.350,1.624])
Al_R1 = 4.302

## Results (Calculating the values of Dlambda, lambda_before adn Lambda_after
#Values n and n (To be copied from 3-4 Transmission.py
a_T_1_Cu = 5.2687599841178185
n_T_1_Cu = 2.956282083665764

a_T_2_Al = 4.5251433961793435
n_T_2_Al = 3.403781466979703

Dlambda_Cu = Dlambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R1,Cu_R2[1])
lambda_Cu_before = Lambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R1)
lambda_Cu_after = Lambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R2[1])

Dlambda_Al = Dlambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R1,Al_R2[1])
lambda_Al_before = Lambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R1)
lambda_Al_after = Lambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R2[1])

Dlambda_th = theory(145*np.pi/180)

## Printing the found values

print("Values Cu:")
print("Dlamda:", Dlambda_Cu)
print("Lambda_before:",lambda_Cu_before)
print("Lambda after:",lambda_Cu_after)

print()

print("Values Al:")
print("Dlamda:", Dlambda_Al)
print("Lambda_before:",lambda_Al_before)
print("Lambda after:",lambda_Al_after)

print()

print("Theory:")
print("Dlamda:", Dlambda_th*10**(12))





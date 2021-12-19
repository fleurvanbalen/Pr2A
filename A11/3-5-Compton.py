## Importing
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import os

## Functions

#equation 6
def Dlambda(a,n,R0,R,R1,R2):
    return 100*(((np.log(R0-R)-np.log(R2-R))/(a))**(1/n)-((np.log(R0-R)-np.log(R1-R))/(a))**(1/n))

#equation 6 but only for 1 lambda
def Lambda(a, n, R0,R,Ri):
    return 100*((np.log(R0-R)-np.log(Ri-R))/(a))**(1/n)

#with equation 5 in the document
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

#Values a and n (To be copied from 3-4 Transmission.py)
a_T_1_Cu = 5.2687599841178185
ea_T_1_Cu = 0.1231016287838336
n_T_1_Cu = 2.956282083665764
en_T_1_Cu = 0.046775022054326994

a_T_2_Al = 4.5251433961793435
ea_T_2_Al = 0.1393175309494889
n_T_2_Al = 3.403781466979703
en_T_2_Al = 0.06650362164438307


## Results (Calculating the values of Dlambda, lambda_before and Lambda_after)

Dlambda_Cu = Dlambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R1,Cu_R2[1])
lambda_Cu_before = Lambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R1)
lambda_Cu_after = Lambda(a_T_1_Cu, n_T_1_Cu,R0,Bg,Cu_R2[1])

Dlambda_Al = Dlambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R1,Al_R2[1])
lambda_Al_before = Lambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R1)
lambda_Al_after = Lambda(a_T_2_Al, n_T_2_Al,R0,Bg,Al_R2[1])

Dlambda_th = theory(145*np.pi/180)

## Calculating the errors

#Using the standerd formula for the calculation of a error of a value depended on other errorbounded values and using one lambda of formula 6
def function_el(a,ea,n,en,R0,R1):
    eR = eR0 = eR1 = 0.1
    eR1 = 0.1
    R = Bg = 0.157
    el = np.sqrt( (100*np.log(R0-R)**(1/n-1)/(a**(1/n)*(R0-R)*n))**2 * eR0**2 + (100*(np.log(R0-R)-np.log(R1-R))**(1/n-1)*(1/(R1-R)-1/(R0-R))/(a**(1/n)*n))**2 * eR**2 + (-100*np.log(R1-R)**(1/n-1)/(a**(1/n)*(R1-R)*n))**2 * eR1**2 + (100*(np.log(R0-R)-np.log(R1-R))**(1/n)/(a**(1/n+1)*-n))**2 * (ea)**2 + (100*((np.log(R0-R)-np.log(R1-R))/a)**(1/n)*np.log((np.log(R0-R)-np.log(R1-R))/a))**2 * en**2)
    return el

#error in equation 6
def function_eDl(el1,el2):
    eDl = np.sqrt(el2**2 + el1**2)
    return eDl

#Using equation 8 in the document
def function_el2(n,T):
    el2 = 2*np.sqrt(n/T)
    return el2
"""
el1_Cu = function_el2(Cu_R1,420)
el2_Cu = function_el2(Cu_R2[1],420)

el1_Al = function_el2(Al_R1,420)
el2_Al = function_el2(Al_R2[1],420)

eDl_Cu = function_eDl(el1_Cu,el2_Cu)
eDl_Al = function_eDl(el1_Al,el2_Al)
"""

#hoe zit het met die picometer?
###Test omgeving

def function_el(a,ea,n,en,R0,R1):
    R = Bg = 0.157
    T = 420
    eR = 2*np.sqrt(R/T)
    eR0 = 2*np.sqrt(R0/T)
    eR1 = 2*np.sqrt(R1/T)
    el = np.sqrt( (100*np.log(R0-R)**(1/n-1)/(a**(1/n)*(R0-R)*n))**2 * eR0**2 + (100*(np.log(R0-R)-np.log(R1-R))**(1/n-1)*(1/(R1-R)-1/(R0-R))/(a**(1/n)*n))**2 * eR**2 + (-100*np.log(R1-R)**(1/n-1)/(a**(1/n)*(R1-R)*n))**2 * eR1**2 + (100*(np.log(R0-R)-np.log(R1-R))**(1/n)/(a**(1/n+1)*-n))**2 * (ea)**2 + (100*((np.log(R0-R)-np.log(R1-R))/a)**(1/n)*np.log((np.log(R0-R)-np.log(R1-R))/a))**2 * en**2)
    return el



## Printing the found values


#Test for the found equation for the error
el1_Cu = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Cu_R1)
el2_Cu = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Cu_R2[1])
el1_Al = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Al_R1)
el2_Al = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Al_R2[1])

eDl_Cu = function_eDl(el1_Cu,el2_Cu)
eDl_Al = function_eDl(el1_Al,el2_Al)


print("Values Cu:")
print("Dlambda  = %1.00f \u00B1 %1.00f pm" %(Dlambda_Cu,eDl_Cu))
print("Lambda_before  = %1.00f \u00B1 %1.00f pm" %(lambda_Cu_before,el1_Cu))
print("Lambda_after  = %1.00f \u00B1 %1.00f pm" %(lambda_Cu_after,el2_Cu))

print()

print("Values Al:")
print("Dlambda  = %1.00f \u00B1 %1.00f pm" %(Dlambda_Al,eDl_Al))
print("Lambda_before  = %1.00f \u00B1 %1.00f pm" %(lambda_Al_before,el1_Al))
print("Lambda_after  = %1.00f \u00B1 %1.00f pm" %(lambda_Al_after,el2_Al))

print()

print("Theory:")
print("Dlamda:", Dlambda_th*10**(12))



###Backup

print("Backup")

'''
el1_Cu = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Cu_R1)
el2_Cu = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Cu_R2[1])
el1_Al = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Al_R1)
el2_Al = function_el(a_T_1_Cu,ea_T_1_Cu,n_T_1_Cu,en_T_1_Cu,R0,Al_R2[1])
'''


'''
print("Dlamda:", Dlambda_Cu,"\u00B1", )
print("Lambda_before:",lambda_Cu_before)
print("Lambda after:",lambda_Cu_after)

print("Dlamda:", Dlambda_Al)
print("Lambda_before:",lambda_Al_before)
print("Lambda after:",lambda_Al_after)
'''

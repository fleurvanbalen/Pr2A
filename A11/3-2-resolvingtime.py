## Importeren
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time


## Functies

def R_func(I,a,b):
    return a*I+b

def r_func(R,T):
    return R/(1+R*T)


## Resolving time
plt.close()

I = np.array([])
for i in range(11):
    I = np.append(I,i/100) #Array I maken
I_lin = np.linspace(0,10,50)/100


f = np.array([0.2,590.8,1054,1457,1810,2133,2465,2718,2979,3224,3451]) # Array gemeten waarden

cf_R, covariance_R = curve_fit(R_func, I[:4] ,f[:4]) # R_func fitten (lineaire fit)
R_cf = R_func(I_lin,cf_R[0],cf_R[1]) # Functie invullen voor lineaire fit


R = []
for i in range(11):
    R_i = R_func(I[i],cf_R[0],cf_R[1])
    R.append(R_i)

R_lin = np.linspace(min(R),max(R))


cf_r, covariance_r = curve_fit(r_func, R, f)
r_cf = r_func(R_lin,cf_r[0])

e1_alles = np.sqrt(abs(np.diag(covariance_r)))
e1_T = e1_alles[0]
print(e1_T)



#cf_r2, covariance_r = curve_fit(r_func, R[4:], f[4:])
#r_cf2 = r_func(R_lin,cf_r2[0])
#print(cf_r,cf_r2)

print("The resolvetime T =",cf_r[0])

plt.rcParams['figure.dpi'] = 100
plt.plot(I,f,".", color='black', label = "Data")
plt.plot(I_lin,R_cf, color='black', linestyle='dotted', label = 'FIT: $R = a \cdot I + b$')
plt.plot(I_lin,r_cf, color='red', label = 'FIT: $r = \\frac{R}{1+R \cdot T}$')
#plt.plot(I_lin,r_cf2, label = 'FIT: Non linear')
plt.xlabel("$I$ (in A)")
plt.ylabel("$R$ en $r$ (in counts/s)")
plt.legend()
plt.grid()
plt.show()
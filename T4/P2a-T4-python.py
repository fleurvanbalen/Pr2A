import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

### --------------------------------
### SF-59 Meting: "Extinction"
### --------------------------------

I_1 = np.array([0.98,    1.96,   3.94,   5.28])             # Stroom in ampere (A)
sI_1 = np.array([0.0128, 0.0226, 0.0694, 0.0828])           # Fout vd stroom

Delta_theta_1 = np.array([5, 5, 6, 10]) * (2/360) * np.pi   # Verschil van de hoek tot de beginpositie in radialen (rad)
sDelta_theta_1 = np.array(4*[4]) * (2/360) * np.pi          # afleesfout is 2 graden, delta = begin - eind dus fout delta = 2 * 2 = 4 graden

l_1 = np.array(4 * [10.2]) * 10**-2                         # Lengte van staaf in meter (m)
sl_1 = np.array(4 * [0.05]) * 10**-2

B_1 = 11.1 * I_1 * 10**(-3)                                 # Berekening van het B-veld in tesla (T)
sB_1 = B_1 * (sI_1/I_1)**2

v_1 = Delta_theta_1 / (B_1*l_1)
sv_1 = v_1 * ( (sDelta_theta_1/Delta_theta_1)**2 + (sB_1/B_1)**2 + (sl_1/l_1)**2 )
# De fout komt hoger uit sinds de hoek met minimale hoek theta veel moeilijker is te bepalen dan 2 graden

print("")
print("De v van SF-59 uit meting 1:")
print(v_1, '+-', sv_1)
print("Gemiddeld:") #TODO
print("")

## Fitten van de waardes
x = B_1
sx = sB_1
y = Delta_theta_1
sy = sDelta_theta_1

#Curve die we willen fitten
def curve(params, x):
    return x * params[0] * 0.102

# Voer optimalisatie uit (oftewel: het fitten)
gok = [20] # k, (Rl + Rc)
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("")
    print("De v van SF-59 uit meting 1 m.b.v. de fit:")
    print("{} +- {}".format(parameters[i], onzekerheden[i]))
    print("")

# Coordinaten van curve bepalen
curve_x = np.linspace(0, 0.07, 1000)
curve_y = curve(parameters, curve_x)
curve_theorie = [1/(x+162.015+43.822) * np.sqrt(1.2229/(0.329*10**-6)) for x in curve_x]

# Maak plot en laat zien
plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $\\theta= v B \\ell$')

plt.grid(True)
plt.xlim(0, 0.07)
plt.ylim(0, 0.3)   
plt.xlabel('$B$ (T)')
plt.ylabel('$\\theta$ (rad)')
plt.legend(loc="upper left")
plt.show()

### SF-59 Meting: "Returning to Fixed Intensity Value"
I_2 = np.array([0.97, 1.97, 3.93, 5.9])                     # Stroom in ampere (A)
Delta_theta_2 = np.array([1,2,5,7]) * (2/360) * np.pi

B_2 = 11.1 * I_2 * 10**(-3)
l_2 = np.array([10.2, 10.2, 10.2, 10.2]) * 10**-2

v_2 = Delta_theta_2 / (B_2*l_2)

print("v van SF-59 uit de returning meting is gelijk aan:",v_2)


### Metingen: "Dynamische meetmethode"
#Perspex
I_3 = 1.5
DU_RMS = 4.62
DU_MEAN = 434 *10**-3
Delta_theta_3 = (1/2) * (DU_MEAN * 10**(-2)) / (98*10**(-3))

B_3 = 11.1 * I_3 * 10**(-3)
l_3 = 10.2 * 10**-2

v_3 = Delta_theta_3 / (B_3*l_3)

print("v uit meeting 3 is gelijk aan:",v_3)

I_3b = 1.506
DU_RMS_3b = 52 *10**-3
DU_MEAN_3b = 47 *10 **-3
Multiplier = 5 * 10 * 50
Delta_theta_3b = (1/2) * (DU_MEAN_3b) / (98*10**(-3)*Multiplier)

B_3b = 11.1 * I_3b * 10**(-3)
l_3b = 10.2 * 10**-2

v_3b = Delta_theta_3b / (B_3b*l_3b)

print("v uit meeting 3b, Persplex, is gelijk aan:",v_3b)

#Fu-Si


#Perspex
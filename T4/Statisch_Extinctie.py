import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

### --------------------------------
### SF-59 Meting: "Extinction"
### Gewogen gemiddelde: 29   +- 9 (afleesfout 4 graden)
### Gewogen gemiddelde: 28.9 +- 2.1 (afleesfout 2 graden)
### m.b.v. fitten:      29   +- 5 
### --------------------------------

I_1 = np.array([0.98,    1.96,   3.94,   5.28])             # Stroom in ampere (A)
sI_1 = np.array([0.0393, 0.0496, 0.0694, 0.0828])           # Fout vd stroom

Delta_theta_1 = np.array([5, 5, 6, 10]) * (2/360) * np.pi   # Verschil van de hoek tot de beginpositie in radialen (rad)
sDelta_theta_1 = np.array(4*[np.sqrt(2*(3**2))])*(2/360)*np.pi  # afleesfout is 4 graden, delta = begin - eind dus fout delta = sqrt(4^2+4^2) graden

l_1 = np.array(4 * [10.2]) * 10**-2                         # Lengte van staaf in meter (m)
sl_1 = np.array(4 * [0.05]) * 10**-2

B_1 = 11.1 * I_1 * 10**(-3)                                 # Berekening van het B-veld in tesla (T)
sB_1 = B_1 * sI_1/I_1

v_1 = Delta_theta_1 / (B_1*l_1)
sv_1 = v_1 * np.sqrt( (sDelta_theta_1/Delta_theta_1)**2 + (sB_1/B_1)**2 + (sl_1/l_1)**2 )
# De fout komt eigenlijk hoger uit sinds de hoek met minimale intensiteit veel moeilijker is te bepalen dan 2 graden, dus als we voor het aflezen een fout van 4 nemen:

print("")
print("De v van SF-59 uit meting 1:")
print(v_1, '+-', sv_1)

G = 1/(sv_1)**2
v_gewogen = 0
gewichten_tot = 0
for i in range(4):
    v_gewogen += G[i]*v_1[i]
    gewichten_tot += G[i]
v_gemiddeld = v_gewogen/gewichten_tot
sv_gemiddeld = 1/(np.sqrt(gewichten_tot))
print("Gemiddeld:", v_gemiddeld, '+-', sv_gemiddeld)
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
plt.ylim(-0.05, 0.30)   
plt.xlabel('$B$ (T)')
plt.ylabel('$\\theta$ (rad)')
plt.legend(loc="upper left")
plt.show()
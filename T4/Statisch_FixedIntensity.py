import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

### --------------------------------
### SF-59 Meting: "Returning to Fixed Intensity Value"
### Gewogen gemiddelde: 18.5 +- 2.7 (afleesfout 2 graden)
### m.b.v. fitten:      18.4 +- 0.6 
### --------------------------------

I_2 = np.array([0.97, 1.97, 3.93, 5.9])                     # Stroom in ampere (A)
sI_2 = np.array([0.0393, 0.0496, 0.0694, 0.0828])   

Delta_theta_2 = np.array([1, 2, 5, 7]) * (2/360) * np.pi    # 
sDelta_theta_2 = np.array(4*[np.sqrt(2*(2**2))])*(2/360)*np.pi  # afleesfout is 2 graden, delta = begin - eind dus fout delta = sqrt(2^2+2^2) graden

l_2 = np.array(4 * [10.2]) * 10**-2                         # Lengte van staaf in meter (m)
sl_2 = np.array(4 * [0.05]) * 10**-2

B_2 = 11.1 * I_2 * 10**(-3)                                 # Berekening van het B-veld in tesla (T)
sB_2 = B_2 * (sI_2/I_2)**2

v_2 = Delta_theta_2 / (B_2*l_2)
sv_2 = v_2 * ( (sDelta_theta_2/Delta_theta_2)**2 + (sB_2/B_2)**2 + (sl_2/l_2)**2 )
# De fout komt hoger uit sinds de hoek met minimale hoek theta veel moeilijker is te bepalen dan 2 graden

print("")
print("De v van SF-59 uit meting returning to fixed intensity:")
print(v_2, '+-', sv_2)

G = 1/(sv_2)**2
v_gewogen = 0
gewichten_tot = 0
for i in range(4):
    v_gewogen += G[i]*v_2[i]
    gewichten_tot += G[i]
v_gemiddeld = v_gewogen/gewichten_tot
sv_gemiddeld = 1/(np.sqrt(gewichten_tot))
print("Gemiddeld:", v_gemiddeld, '+-', sv_gemiddeld)
print("")

## Fitten van de waardes
x = B_2
sx = sB_2
y = Delta_theta_2
sy = sDelta_theta_2

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
    print("De v van SF-59 uit meting 2 m.b.v. de fit:")
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
plt.ylim(-0.1, 0.30)   
plt.xlabel('$B$ (T)')
plt.ylabel('$\\theta$ (rad)')
plt.legend(loc="upper left")
plt.show()
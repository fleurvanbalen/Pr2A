from numpy import sqrt
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from fitcode import curve_fit

# Methode Delta frequentie
Qr100 = 4.565
Qr200 = 3.644
Qr400 = 2.676
Qr600 = 2.099
Qr800 = 1.723

x = [100, 200, 400, 600, 800] # weerstanden in Ohm
sx = [1, 2, 4, 6, 8]
y = [Qr100, Qr200, Qr400, Qr600, Qr800] # Q waardes
sy = 5 * [0.2]

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(x+params[1])

# Voer optimalisatie uit (oftewel: het fitten)
gok = [60, 200] # k, (Rl + Rc)
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(0, 1000, 1000)
curve_y = curve(parameters, curve_x)
curve_theorie = [1/(x+162.015+43.822) * np.sqrt(1.2229/(0.329*10**-6)) for x in curve_x]

# TODO: Onzekerheden toevoegen aan de metingen

# Maak plot en laat zien
plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $Q=\\frac{k}{R + R_C + R_L}$')
plt.plot(curve_x, curve_theorie, color='black', label='Theoretisch verband: $Q=\\frac{1}{R + R_C + R_L} \\cdot \\sqrt{\\frac{L}{C}}$')
# plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.grid(True)
plt.xlim(0, 1000)
plt.ylim(0, 10)   
plt.xlabel('$R$ ($\\Omega$)')
plt.ylabel('$Q$')
plt.legend(loc="upper right")

plt.show()

# -----

# csv = pd.read_csv("data-5-2-r100.csv")

# frequency = csv['Frequentie (Hz)'].values.tolist()
# voltage = csv['Spanning (V)'].values.tolist()
# phase = csv['Fase (degrees)'].values.tolist()

# amplMax = 0.125 # (V)
# amplDelta = amplMax * (sqrt(2)/2)
# print(amplDelta)
# freqDelta1 = 205 # (Hz)
# freqDelta2 = 305 # (Hz)

# plt.errorbar(frequency, voltage, fmt='.', color='black', label='Metingen') 
# plt.axvline(x=250.0, color='black', linestyle='dashed', label='$f_0 =$ 250.0 Hz')

# plt.axhline(y=amplDelta, color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}} =$ 0.231 Hz')
# plt.axvline(x=freqDelta1, color='black', linestyle='dotted', label='$f_1 =$ 205 Hz')
# plt.axvline(x=freqDelta2, color='black', linestyle='dotted', label='$f_2 =$ 305 Hz')

# plt.xscale('log')
# plt.grid(True)
# plt.xlim(100, 1000)
# plt.ylim(0, 0.5)   
# plt.xlabel('$f$ (Hz)')
# plt.ylabel('$v$ (V)')
# plt.legend(loc="upper left")

# plt.show()

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from fitcode import curve_fit

# Methode Delta frequentie
fc01 = 453.61
fc02 = 319.62
fc03 = 259.87
fc04 = 225.33
fc05 = 200.92

x = (10**(-6))*np.array([0.1, 0.2, 0.3, 0.4, 0.5]) # Capaciteiten in !micro!Farrad
sx = (10**-6)*np.array([0.005, 0.01, 0.015, 0.02, 0.025])
y = [fc01, fc02, fc03, fc04, fc05] # Q waardes
sy = 5 * [10]

#Curve die we willen fitten
def curve(params, x):
    return params[0]/np.sqrt(x)

# Voer optimalisatie uit (oftewel: het fitten)
gok = [2000] # k''
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(0.05*10**-6, 0.6*10**-6, 1000)
curve_y = curve(parameters, curve_x)
curve_theorie = [1/(2*np.pi*np.sqrt(1.2229)) * np.sqrt(1/(x)) for x in curve_x]

# Maak plot en laat zien
plt.errorbar(x, y, sy, sx, fmt='o', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $f_0=\\frac{k\'\'}{\\sqrt{C}}$')
plt.plot(curve_x, curve_theorie, color='black', label='Theoretisch verband: $f_0=\\frac{1}{2 \\pi \\sqrt{L \\cdot C}}$', linestyle='--')
# plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.grid(True)
plt.xlim(0.05*10**-6, 0.6*10**-6)
#plt.ylim(0, 0.5)   
plt.xlabel('$C$ (F)')
plt.ylabel('$f_0$ (Hz)')
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

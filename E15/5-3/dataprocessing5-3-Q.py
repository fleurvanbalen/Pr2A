from numpy import sqrt
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from fitcode import curve_fit

# Methode Delta frequentie
Qc01 = 3.214
Qc02 = 2.721
Qc03 = 2.405
Qc04 = 2.181
Qc05 = 2.035

x = [0.1, 0.2, 0.3, 0.4, 0.5] # Capaciteiten in !micro!Farrad
sx = None
y = [Qc01, Qc02, Qc03, Qc04, Qc05] # Q waardes
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(x+params[1])

# Voer optimalisatie uit (oftewel: het fitten)
gok = [2000] # k'
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)
curve_theorie = [1/(x+162.015+43.822) * np.sqrt(1.2229/(0.329*10**-6)) for x in curve_x]

# Maak plot en laat zien
plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $Q=\\frac{k}{R + R_C + R_L}$')
plt.plot(curve_x, curve_theorie, color='black', label='Theoretisch verband')
# plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.grid(True)
#plt.xlim(100, 1000)
#plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
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

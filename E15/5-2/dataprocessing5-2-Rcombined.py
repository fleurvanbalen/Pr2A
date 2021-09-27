import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fitcode import curve_fit
import math

# ----- R100

csv = pd.read_csv("data-5-2-r100.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

x = frequency # frequenties in Hz
sx = None
y = voltage # amplitudes in mV
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(np.sqrt(1+(params[1]**2)*((x/params[2])-(params[2]/x))**2))

# Voer optimalisatie uit (oftewel: het fitten)
gok = [0.125, 5, 245] # maxAmpl, Q, f0
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.figure(1, figsize=(30, 5))
plt.subplot(1, 5, 1)

plt.title("R = 100 $\\Omega$")

plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $v=\\frac{v_{max}}{\\sqrt{1+Q^2\left(\\frac{f}{f_0}-\\frac{f_0}{f}\\right)^2}}$')

plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper right")

# ----- R200

csv = pd.read_csv("data-5-2-r200.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

x = frequency # frequenties in Hz
sx = None
y = voltage # amplitudes in mV
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(np.sqrt(1+(params[1]**2)*((x/params[2])-(params[2]/x))**2))

# Voer optimalisatie uit (oftewel: het fitten)
gok = [0.125, 5, 245] # maxAmpl, Q, f0
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.subplot(1, 5, 2)

plt.title("R = 200 $\\Omega$")

plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $v=\\frac{v_{max}}{\\sqrt{1+Q^2\left(\\frac{f}{f_0}-\\frac{f_0}{f}\\right)^2}}$')

plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper right")

# ----- R400

csv = pd.read_csv("data-5-2-r400.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

x = frequency # frequenties in Hz
sx = None
y = voltage # amplitudes in mV
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(np.sqrt(1+(params[1]**2)*((x/params[2])-(params[2]/x))**2))

# Voer optimalisatie uit (oftewel: het fitten)
gok = [0.125, 5, 245] # maxAmpl, Q, f0
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.subplot(1, 5, 3)

plt.title("R = 400 $\\Omega$")

plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $v=\\frac{v_{max}}{\\sqrt{1+Q^2\left(\\frac{f}{f_0}-\\frac{f_0}{f}\\right)^2}}$')

plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper right")

# ----- R600

csv = pd.read_csv("data-5-2-r600.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

x = frequency # frequenties in Hz
sx = None
y = voltage # amplitudes in mV
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(np.sqrt(1+(params[1]**2)*((x/params[2])-(params[2]/x))**2))

# Voer optimalisatie uit (oftewel: het fitten)
gok = [0.125, 2, 245] # maxAmpl, Q, f0
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.subplot(1, 5, 4)

plt.title("R = 600 $\\Omega$")

plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $v=\\frac{v_{max}}{\\sqrt{1+Q^2\left(\\frac{f}{f_0}-\\frac{f_0}{f}\\right)^2}}$')

plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper right")

# ----- R800

csv = pd.read_csv("data-5-2-r800.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

x = frequency # frequenties in Hz
sx = None
y = voltage # amplitudes in mV
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0]/(np.sqrt(1+(params[1]**2)*((x/params[2])-(params[2]/x))**2))

# Voer optimalisatie uit (oftewel: het fitten)
gok = [0.125, 2, 245] # maxAmpl, Q, f0
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(100, 1000, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.subplot(1, 5, 5)

plt.title("R = 800 $\\Omega$")

plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Metingen') 
plt.plot(curve_x, curve_y, color='red', label='Fit: $v=\\frac{v_{max}}{\\sqrt{1+Q^2\left(\\frac{f}{f_0}-\\frac{f_0}{f}\\right)^2}}$')

plt.axhline(y=parameters[0]/math.sqrt(2), color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}}$')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper right")

# -----

plt.show()
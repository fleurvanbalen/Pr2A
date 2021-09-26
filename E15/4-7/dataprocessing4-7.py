import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("data4-7.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

plt.errorbar(frequency, phase, fmt='.', color='black', label='Metingen') 
plt.axvline(x=251.1, color='black', linestyle='dotted', label='$f_0 =$ 251.1 Hz')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(-90, 90)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('Fasehoek tussen $v$ en $i$ (graden)')
plt.legend(loc="upper left")

plt.show()

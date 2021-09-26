from numpy import sqrt
import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("p5r100.csv")

frequency = csv['Frequentie (Hz)'].values.tolist()
voltage = csv['Spanning (V)'].values.tolist()
phase = csv['Fase (degrees)'].values.tolist()

amplMax = 0.125 # (V)
amplDelta = amplMax * (sqrt(2)/2)
print(amplDelta)
freqDelta1 = 205 # (Hz)
freqDelta2 = 305 # (Hz)

plt.errorbar(frequency, voltage, fmt='.', color='black', label='Metingen') 
plt.axvline(x=250.0, color='black', linestyle='dashed', label='$f_0 =$ 250.0 Hz')

plt.axhline(y=amplDelta, color='black', linestyle='dotted', label='$\\frac{v_{max}}{\\sqrt{2}} =$ 0.231 Hz')
plt.axvline(x=freqDelta1, color='black', linestyle='dotted', label='$f_1 =$ 205 Hz')
plt.axvline(x=freqDelta2, color='black', linestyle='dotted', label='$f_2 =$ 305 Hz')

plt.xscale('log')
plt.grid(True)
plt.xlim(100, 1000)
plt.ylim(0, 0.5)   
plt.xlabel('$f$ (Hz)')
plt.ylabel('$v$ (V)')
plt.legend(loc="upper left")

plt.show()

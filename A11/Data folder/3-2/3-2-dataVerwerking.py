import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("Plateau_data.csv")

voltage = csv['Voltage'].values.tolist()
counts = csv['Counts'].values.tolist()

plt.errorbar(voltage, counts, fmt='.', color='black', label='Metingen') 
plt.axvline(x=475, color='red', linestyle='dotted', label='Start plateau')
plt.axvline(x=775, color='red', linestyle='dotted', label='Eind plateau')

# plt.xscale('log')
plt.grid(True)
plt.xlim(275, 800)
plt.ylim(0, 3000)
plt.xlabel('$\\lambda$ (?)')
plt.ylabel('Counts/s')
plt.legend(loc="upper left")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("Data folder/3-2/Plateau_data.csv")

voltage = csv['Voltage'].values.tolist()
counts = csv['Counts'].values.tolist()

plt.errorbar(voltage, counts, fmt='.', color='black', label='Metingen') 
plt.axvline(x=475, color='red', linestyle='dotted', label='Start en eind plateau')
plt.axvline(x=675, color='red', linestyle='dotted')

# plt.xscale('log')
plt.grid(True)
plt.xlim(275, 700)
plt.ylim(0, 3000)
plt.xlabel('Spanning over de GM-buis $U_{GM}$ (in V)')
plt.ylabel('Intensiteit (in counts/s)')
plt.legend(loc="upper left")

plt.show()

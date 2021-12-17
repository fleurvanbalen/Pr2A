import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("Data folder/3-3/Bragg_data_emmissiespectrum.csv")

golflengte = csv['Golflengte'].values.tolist()
Inofilter = csv['Nofilter'].values.tolist()
Icu = csv['Cu'].values.tolist()
Ial = csv['Al'].values.tolist()

plt.plot(golflengte, Inofilter)
plt.errorbar(golflengte, Inofilter, fmt='.', color='black', label='Metingen') 
plt.plot(golflengte, Icu)
plt.plot(golflengte, Ial)
# plt.axvline(x=475, color='red', linestyle='dotted', label='Start en eind plateau')
# plt.axvline(x=675, color='red', linestyle='dotted')

# plt.xscale('log')
plt.grid(True)
# plt.xlim(275, 700)
# plt.ylim(0, 3000)
plt.xlabel('Spanning over de GM-buis $U_{GM}$ (in V)')
plt.ylabel('Intensiteit (in counts/s)')
plt.legend(loc="upper left")

plt.show()

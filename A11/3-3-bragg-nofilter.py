import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("Data folder/3-3/Bragg_data_emmissiespectrum.csv")

golflengte = csv['Golflengte'].values.tolist()
Inofilter = csv['Nofilter'].values.tolist()
Icu = csv['Cu'].values.tolist()
Ial = csv['Al'].values.tolist()

plt.plot(golflengte, Inofilter, color='black', label='Geen filter')
plt.errorbar(golflengte, Inofilter, fmt='.', color='black', alpha=0.4) 
plt.plot(golflengte, Icu, color='green', label='Koper (Cu)')
plt.errorbar(golflengte, Icu, fmt='.', color='green', alpha=0.4) 
plt.plot(golflengte, Ial, color='red', label='Aluminium (Al)')
plt.errorbar(golflengte, Ial, fmt='.', color='red', alpha=0.4) 
# plt.axvline(x=475, color='red', linestyle='dotted', label='Start en eind plateau')
# plt.axvline(x=675, color='red', linestyle='dotted')

# plt.xscale('log')
plt.grid(True)
# plt.xlim(275, 700)
# plt.ylim(0, 3000)
plt.xlabel('$\lambda$ (in pm)')
plt.ylabel('R (in counts/s)')
plt.legend(loc="upper left")

plt.show()

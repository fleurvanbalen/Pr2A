# %%
## Importeren
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import pandas as pd
# from fitcode import curve_fit

# %%
## Functies

def M_func(t,M0,T1):
    return M0*(1-np.exp(-t/T1))

def B(f,gamma):
    return f*2*np.pi/gamma

def M_func2(t,M0,T2):
    return M0*(np.exp(-t/T2))

def A_func(t,A0,T2):
    return A0*np.exp(-t/T2)

# # %%
# ## Opdracht 4

#     #Data
# B_aarde_groote = 65 * 10**(-6) #T
# B_aarde = B_aarde_groote * np.array([0,0,1])
# f = np.array([2.110,2.120,2.093,2.086,2.100,2.100,2.109,2.137,2.123,2.103,2.127,2.128,2.139,2.105,2.134,2.135,2.116,2.105,2.090,2.098])

#     #Berekeningen
# Gem_f = np.mean(f)
# gamma_proton = 2.675*10**8 #Ckg^-1 , s^-1 T^-1
# B_opdr4 = B(Gem_f,gamma_proton)


#     #Printen
# print("Gemiddelde frequentie uit 10 meetingen:", Gem_f)
# print("Het magneetisch veld met de gemiddelde frequentie is", B_opdr4)

# %%
# ## Opdracht 5

    #Data
M = np.array([0.624,1.12,1.48,1.80,1.92,2.10,2.18,2.36,2.46,2.44])
sM = 0.04 * np.ones(10)
I = 3 #A
st = None

    #t berekenen + linspace t
t_magnetisatie = []
for i in range(10):
    t_magnetisatie.append(i+1)
t_grafiek = 160 * 10**(-3) * np.ones(len(M)) #s
t = t_magnetisatie + t_grafiek #s
t_lin = np.linspace(min(t)-2,max(t)+1) #s

    #Curvefitten
cf, covariance = curve_fit(M_func,t,M)
M_cf = M_func(t_lin,cf[0],cf[1])

    #Waardes printen
print("T1 =", cf[1], "s")
print('fout',  covariance,)
print("M0 =", cf[0])

    #Plotten
plt.rcParams['figure.dpi'] = 100
# plt.plot(t,M,".",label = "Data", color='black')
plt.errorbar(t,M,sM,st,".",label = "Data", color='black')
plt.plot(t_lin,M_cf, label = 'FIT: $M = M_0(1-e^{-\\frac{t}{T_1}})$', color='red')
plt.xlabel("t (s)")
plt.ylabel("M (V)")
plt.xlim(0, 11)
plt.ylim(0, 2.6)
plt.legend(fontsize=14)
plt.grid()
plt.show()

# %%
## Opdracht 6

# I = np.array([2.81,2.60,2.37,2.14,1.92,1.69,1.49,1.26,1.04,0.82,0.60]) # A
# t = (160* 10**(-3)+10) * np.ones(10)

# %%
## Opdracht 7
from fitcode import curve_fit
os.chdir("/Users/fleurvanbalen/Documents/GitHub/Pr2A/A12")

csv = pd.read_csv("ALL0004/data7fit2.csv")
csvNotFit = pd.read_csv("ALL0004/data7.csv")

time = csv['Time (s)'].values.tolist()
amplitude = csv['Amplitude (V)'].values.tolist()

timeNotFit = csvNotFit['Time (s)'].values.tolist()
amplitudeNotFit = csvNotFit['Amplitude (V)'].values.tolist()

x = time # time in s
sx = None
y = amplitude # amplitudes in V
sy = None

#Curve die we willen fitten
def curve(params, x):
    return params[0] * np.e**(-(x)/params[1])

# Voer optimalisatie uit (oftewel: het fitten)
gok = [3, 2] # M0, T2, t_offset
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(0, 5, 1000)
curve_y = curve(parameters, curve_x)

# %%
# Maak plot en laat zien
plt.errorbar(timeNotFit, amplitudeNotFit, fmt='.', color='grey', label='Data not included in fit')
plt.errorbar(x, y, sy, sx, fmt='.', color='black', label='Data') 
plt.plot(curve_x, curve_y, color='red', label='FIT: $M_{xy}(t)=M_{xy}(0) \\cdot e^{-\\frac{t}{T_2^{\\ast}}}$')


plt.grid(True)
plt.xlim(-0.1, 4.1)
plt.ylim(0, 4)   
plt.xlabel('$t$ (s)')
plt.ylabel('$M_{xy}$ (V)')
plt.legend(loc="upper right", fontsize=14)

plt.show()


# %%
## Opdracht 8

### sub opdracht 1

    #Instellingen
delay_t = 500 * 10**(-3) #s
pola_t  = 5 #s
A       = 10 #V
n       = range(2,20+1) # aantal golven

    #Data
V_echo = np.array([0.040,0.042,0.068,0.116,0.152,0.194,0.258,0.314,0.384,0.452,0.520,0.628,0.656,0.760,0.832,0.864,0.904,0.904,0.880]) #V

V_echo_fout_1 = 2.0 * 10**(-3) #V
V_echo_fout_2 = 4.0 * 10**(-3) #V
V_echo_fout_3 = 8.0 * 10**(-3) #V
delay_t_fout  =  70 * 10**(-3) #s

V_echo_fout   = []
V_echo_fout_tussen = np.append(V_echo_fout_1*np.ones(8),V_echo_fout_2*np.ones(4))
V_echo_fout   = np.append(V_echo_fout_tussen, V_echo_fout_3*np.ones(7))


    #Plotten
plt.rcParams['figure.dpi'] = 100
plt.errorbar(n,V_echo,V_echo_fout,None, '.', color = 'grey',ecolor = 'red', label = "Data")
#plt.plot(n,V_echo,".",label = "Data")
plt.xlabel("$n$")
plt.ylabel("$V_{echo}$ (V)")
plt.legend()
plt.grid()
plt.show()

# %%
### sub opdracht 2

    #Instellingen
n       = 30
A       = []
for i in range(1,21):
    A.append(i/2)

    #Data
V_echo = np.array([0.0128,0.0140,0.0156,0.0368,0.0560,0.0792,0.104,0.109,0.150,0.156,0.200,0.210,0.252,0.252,0.264,0.266,0.256,0.256,0.214,0.158]) #V

V_echo_fout_1 = 0.4 * 10**(-3) #V
V_echo_fout_2 = 0.8 * 10**(-3) #V
V_echo_fout_3 = 2.0 * 10**(-3) #V

V_echo_fout   = []
V_echo_fout_tussen = np.append(V_echo_fout_1*np.ones(5),V_echo_fout_2*np.ones(3))
V_echo_fout   = np.append(V_echo_fout_tussen, V_echo_fout_3*np.ones(12))



    #Plotten
plt.rcParams['figure.dpi'] = 100
plt.errorbar(A,V_echo,V_echo_fout,None, '.', color = 'grey',ecolor = 'red', label = "Data")
plt.xlabel("$A$ (V)")
plt.ylabel("$V_{echo}$ (V)")
plt.legend(loc = 'upper left')
plt.grid()
plt.show()



# %%
### sub opdracht 3

    #Instellingen
n       = 18 # Aantal golven
A       = 7.5 #V
delay_t = [] #s
for i in range(1,21):
    delay_t.append(i/10)

print(delay_t)

delay_t_lin = np.linspace(0,2.1)
    #Data
V_echo = np.array([0.696,0.656,0.616,0.560,0.536,0.472,0.424,0.400,0.376,0.344,0.320,0.280,0.272,0.248,0.216,0.192,0.192,0.184,0.168,0.168]) #V

V_echo_fout = 8 * 10**(-3) * np.ones(20) #V
delay_t_fout = 70 * 10**(-3) * np.ones(20) #s

    #Gewogen Curvefit
cf, covariance = curve_fit(A_func,delay_t,V_echo)
A_cf = A_func(delay_t_lin,cf[0],cf[1])

    #Plotten
plt.rcParams['figure.dpi'] = 100
plt.errorbar(delay_t,V_echo,V_echo_fout,delay_t_fout, '.', color = "blue", ecolor = 'grey', label = "Data")
plt.plot(delay_t_lin,A_cf, label = 'FIT: $A_0e^{-\\frac{t}{T_1}}$')
plt.xlabel("$delay time$ (s)")
plt.ylabel("$V_{echo}$ (V)")
plt.legend()
plt.grid()
plt.show()

print(cf[1])
# %%

# %%

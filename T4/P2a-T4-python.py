import numpy as np


### SF-59 Meting: "Extinction"
I_1 = np.array([0,0.98,1.96,3.94,5.28])
Delta_theta_1 = np.array([0,5,5,6,10]) * 2* np.pi

B_1 = 11.1 * I_1 * 10**(-3)
l_1 = np.array([10.2,10.2,10.2,10.2,10.2]) *10**-2

v_1 = Delta_theta_1 / (B_1*l_1)

print("De v van SF-59 uit meting 1:")
print(v_1)


### SF-59 Meting: "Returning to Fixed Intensity Value"
I_2 = np.array([0.97,1.97,3.93,5.9])
Delta_theta_2 = np.array([1,2,5,7]) * 2* np.pi

B_2 = 11.1 * I_2 * 10**(-3)
l_2 = np.array([10.2,10.2,10.2,10.2]) *10**-2

v_2 = Delta_theta_2 / (B_2*l_2)

print("v van SF-59 uit de returning meting is gelijk aan:",v_2)


### Metingen: "Dynamische meetmethode"
#Perspex
I_3 = 1.5
DU_RMS = 4.62
DU_MEAN = 434 *10**-3
Delta_theta_3 = (1/2) * (DU_MEAN * 10**(-2)) / (98*10**(-3))

B_3 = 11.1 * I_3 * 10**(-3)
l_3 = 10.2 * 10**-2

v_3 = Delta_theta_3 / (B_3*l_3)

print("v uit meeting 3 is gelijk aan:",v_3)

I_3b = 1.506
DU_RMS_3b = 52 *10**-3
DU_MEAN_3b = 47 *10 **-3
Multiplier = 5 * 10 * 50
Delta_theta_3b = (1/2) * (DU_MEAN_3b) / (98*10**(-3)*Multiplier)

B_3b = 11.1 * I_3b * 10**(-3)
l_3b = 10.2 * 10**-2

v_3b = Delta_theta_3b / (B_3b*l_3b)

print("v uit meeting 3b, Persplex, is gelijk aan:",v_3b)

#Fu-Si


#Perspex
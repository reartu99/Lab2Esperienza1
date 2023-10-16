import matplotlib.pyplot as plt
import moduloanalisi as mm
import numpy as np
import scipy as sp

# La resistenza del primo punto vale 220 Ohm con voltaggio a sorgente 10
# La resistenza del secondo punto vale 2200 Ohm con voltaggio a sorgente 15


def line(x, a, b):
    return a * np.array(x) + b


Amperaggio = [7, 8, 9, 10, 11, 12, 14, 17, 21, 28, 29, 30, 31, 32, 33, 34, 36, 37, 39, 40]  # milliamp
Amperaggio = np.array(Amperaggio)*0.001
Voltaggio = [8.21, 8.05, 7.86, 7.64, 7.36, 7.0, 6.52, 5.87, 4.91, 3.363, 3.145, 2.92, 2.679, 2.422, 2.146, 1.85, 1.53,
             1.182, 0.803, 0.402]  # Questo in volt

ErrVolt = mm.incertezzadigitale(1, np.array(Voltaggio), 3, 0.001)
# L'errore del voltaggio si calcola prendendo il massimo. Fondo scala = 50mA
# Ogni tacca quindi vale 1mA e quindi divisa rad(3) viene 0.577
EAmp = 0.6

popt, pcov = sp.optimize.curve_fit(line, Amperaggio, Voltaggio)
plt.errorbar(Amperaggio, Voltaggio, EAmp, ErrVolt, fmt="o", markersize=4)
print(popt, pcov)
plt.plot(Amperaggio, line(Amperaggio, popt[0], popt[1]))
plt.show()


Amperaggio2 = [23, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 37, 39, 42, 44, 47, 50]
Amperaggio2 = np.array(Amperaggio2)*0.001
Voltaggio2 = [4.9, 4.82, 4.73, 4.63, 4.53, 4.41, 4.29, 4.17, 4.02, 3.87, 3.7, 3.527, 3.325, 3.099, 2.847, 2.566,
              2.248, 1.886]
ErrVolt2 = mm.incertezzadigitale(1, np.array(Voltaggio2), 3, 0.001)
# L'errore del voltaggio si calcola prendendo il massimo. Fondo scala = 50mA
# Ogni tacca quindi vale 1mA e quindi divisa rad(3) viene 0.577
popt2, pcov2 = sp.optimize.curve_fit(line, Amperaggio2, Voltaggio2)
plt.errorbar(Amperaggio2, Voltaggio2, EAmp, ErrVolt2, fmt="o", markersize=4)
print(popt2, pcov2)
plt.plot(Amperaggio2, line(Amperaggio2, popt2[0], popt2[1]))
plt.show()

Vt = 1/2 * 15
R0 = 220*220/440

print(Vt, R0)

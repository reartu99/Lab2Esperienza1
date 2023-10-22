import matplotlib.pyplot as plt

import moduloanalisi
import moduloanalisi as mm
import numpy as np
import scipy as sp

V0 = 16
R1_valore = 100.3
R2_valore = 2 * R1_valore

ER1 = moduloanalisi.incertezzadigitale(1.2, R1_valore, 2, 0.1)
ER2 = 2 * ER1

Alfa = (2 * R2_valore) / (2 * R2_valore + R1_valore + np.sqrt(R1_valore ** 2 + 4 * R1_valore * R2_valore))

derivata_alfa_R1 = ((2 * R2_valore * (1 - (2 * R1_valore + R2_valore) /
                                      np.sqrt(R1_valore ** 2 + 4 * R1_valore * R2_valore))) /
                    (2 * R2_valore + R1_valore + np.sqrt(R1_valore ** 2 + 4 * R1_valore * R2_valore)) ** 2)

derivata_alfa_R2 = (2 / (2 * R2_valore + R1_valore + np.sqrt(R1_valore ** 2 + 4 * R1_valore * R2_valore))
                    - (4 * R2_valore) / (np.sqrt(R1_valore ** 2 + 4 * R1_valore * R2_valore) *
                                         (2 * R2_valore + R1_valore + np.sqrt(
                                             R1_valore ** 2 + 4 * R1_valore * R2_valore)) * 2))

Ealfa = np.sqrt((derivata_alfa_R1 * ER1) * 2 + (derivata_alfa_R2 * ER2) * 2)
EV0 = 0.01 / np.sqrt(3)

Vn = [15.96, 7.92, 3.96, 1.98, 0.99]
Nstadi = [1, 2, 3, 4, 5]

ErrVn = mm.incertezzadigitale(0.8, np.array(Vn), 1, 0.001)


def line(x, a, b):
    return a * np.array(x) + b


# Crea il grafico a dispersione (scatter plot) dei dati
plt.scatter(Nstadi, Vn, label='Dati', color='b', marker='o')
plt.errorbar(Nstadi, Vn, ErrVn, 0, fmt="o", markersize=4)
# Mostra il grafico
plt.show()

log_Vn = np.log(Vn)
DeltaY = ErrVn / Vn

popt, pcov = sp.optimize.curve_fit(line, Nstadi, log_Vn)
plt.errorbar(Nstadi, log_Vn, DeltaY, 0, fmt="o", markersize=4)
print(popt, pcov)
plt.plot(Nstadi, line(Nstadi, popt[0], popt[1]))
plt.show()

TDC1 = moduloanalisi.tdc(popt[0], Alfa, pcov[0][0], Ealfa)
print(TDC1)
TDC2 = moduloanalisi.tdc(popt[1], V0, pcov[1][1], EV0)
print(TDC2)

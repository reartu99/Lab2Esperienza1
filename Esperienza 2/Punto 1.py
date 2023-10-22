import matplotlib.pyplot as plt

import moduloanalisi
import moduloanalisi as mm
import numpy as np
import scipy as sp

# La resistenza del primo punto vale 220 Ohm con voltaggio a sorgente 10
# La resistenza del secondo punto vale 2200 Ohm con voltaggio a sorgente 15


def line(x, a, b):
    return a * np.array(x) + b


Ev0 = 0 # valore errore del generatore
Amperaggio = [7, 8, 9, 10, 11, 12, 14, 17, 21, 28, 29, 30, 31, 32, 33, 34, 36, 37, 39, 40]  # milliamp
Amperaggio = np.array(Amperaggio)*0.001
Voltaggio = [8.21, 8.05, 7.86, 7.64, 7.36, 7.0, 6.52, 5.87, 4.91, 3.363, 3.145, 2.92, 2.679, 2.422, 2.146, 1.85, 1.53,
             1.182, 0.803, 0.402]  # Questo in volt

ErrVolt = mm.incertezzadigitale(1, np.array(Voltaggio), 3, 0.001)
# L'errore del voltaggio si calcola prendendo il massimo. Fondo scala = 50mA
# Ogni tacca quindi vale 1mA e quindi divisa rad(3) viene 0.577
EAmp = 0.6*0.001  # Ampere

popt, pcov = sp.optimize.curve_fit(line, Amperaggio, Voltaggio)
plt.errorbar(Amperaggio, Voltaggio, ErrVolt, EAmp, fmt="o", markersize=2)
print("I valori del fit per il primo punto sono: " + str(popt))
print("La matrice di covarianza per il primo punto è: " + str(pcov))
print("")
plt.plot(Amperaggio, line(Amperaggio, popt[0], popt[1]))
plt.ylabel("Vr (V)")
plt.xlabel("Ir (A)")
plt.legend(["Retta di fit lineare", "Punti misurati"])
plt.grid()
plt.show()

# I valori predetti dal teorema di thevenin per il primo punto sono:
Vt1 = 10  # Volt
# 0) tdc con il valore nominale del generatore
TDC00 = moduloanalisi.tdc(Vt1, popt[1], 0, pcov[0][0])
print("Il valore dato dal tdc con il valore nominale del voltaggio è: " + str(TDC00))

# Poi le resistenze sono dispiegate nei seguenti casi:

# 1) tdc con il valore misurato della resistenza
R01 = 215.4  # Ohm

ER01 = moduloanalisi.incertezzadigitale(1.2, R01, 2, 0.1)

TDC11 = moduloanalisi.tdc(R01, -1*popt[0], ER01, pcov[1][1])
print("Il valore dato dal tdc con il valore misurato della resistenza è: " + str(TDC11))

# 2) tdc con il valore nominale della resistenza
R011 = 220  # Ohm
ER011 = 0.1*R011/np.sqrt(3)

TDC22 = moduloanalisi.tdc(R011, -1*popt[0], ER011, pcov[1][1])
print("Il valore dato dal tdc con il valore nominale della resistenza è: " + str(TDC22))


# Seconda parte primo punto
Amperaggio2 = [23, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 37, 39, 42, 44, 47, 50]
Amperaggio2 = np.array(Amperaggio2)*0.001
Voltaggio2 = [4.9, 4.82, 4.73, 4.63, 4.53, 4.41, 4.29, 4.17, 4.02, 3.87, 3.7, 3.527, 3.325, 3.099, 2.847, 2.566,
              2.248, 1.886]
ErrVolt2 = mm.incertezzadigitale(1, np.array(Voltaggio2), 3, 0.001)
# L'errore del voltaggio si calcola prendendo il massimo. Fondo scala = 50mA
# Ogni tacca quindi vale 1mA e quindi divisa rad(3) viene 0.577
popt2, pcov2 = sp.optimize.curve_fit(line, Amperaggio2, Voltaggio2)
plt.errorbar(Amperaggio2, Voltaggio2, ErrVolt2, EAmp, fmt="o", markersize=2)
print("")
print("I valori del fit per il secondo punto sono: " + str(popt2))
print("La matrice di covarianza per il secondo punto è: " + str(pcov2))
print("")
plt.plot(Amperaggio2, line(Amperaggio2, popt2[0], popt2[1]))
plt.ylabel("Vr (V)")
plt.xlabel("Ir (A)")
plt.legend(["Retta di fit lineare", "Punti misurati"])
plt.grid()
plt.show()

# I valori predetti dal teorema di Thevenin per la seconda parte sono
Er = 0.1*2200/np.sqrt(3)
Vt = 1/2 * 15
Evt = 1/2*Ev0
R0 = 2200*2200/4400
ER0 = np.sqrt(np.power(1100*Er, 2))

# TDC tra valore misurato e predetto da Thevenin voltaggio
TDC31 = moduloanalisi.tdc(popt2[0], pcov[0][0], Vt, Evt)
print("Il valore dato dal tdc con il valore misurato e quello di Thevenin per il voltaggio è: " + str(TDC31))

# TDC valore misurato con quello di Thevenin resistenza
TDC32 = moduloanalisi.tdc(popt[1], R0, pcov[1][1], ER0)
print("Il valore dato dal tdc con il valore misurato e quello di Thevenin per la resistenza è: " + str(TDC32))

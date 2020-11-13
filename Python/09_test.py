# test_09.py
''' GRÁFICAS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' La generación de gráficos En Python requiere módulos adicionales.
Los vectores se pueden generar a partir de datos contenidos en listas o arrays.
la operación numérica es posible  con NumPy y la generación de estos gráficos con Matplotlib. '''
# Importar módulos instalados
import numpy as np
from numpy import exp, pi
from math import sqrt
import matplotlib.pyplot as plt
# Periodo
amplitud_max = 10
coeficiente_de_amortiguamiento = 0.07
# Periodo
longitud = 10
gravedad = 9.8
periodo = 2 * pi * sqrt(longitud/gravedad)
# frecuencia
frecuencia = 1 / periodo
angular = 2 * pi * frecuencia
# Vector de tiempo
tiempo = np.linspace(0, 60, 256, endpoint=True)
# Vectores de posición
K = amplitud_max * exp(-coeficiente_de_amortiguamiento * tiempo)
position = K * np.cos(angular * tiempo)
velocidad = K * np.sin(angular * tiempo)
# Gráficas
plt.plot(tiempo, position, label="Posición(\u03B8)")
plt.plot(tiempo, velocidad, label="Velocidad(\u03B8)")
plt.legend()
# Propiedades de las gráficas - Texto
plt.title("Posición y Velocidad del Péndulo Simple")
plt.xlabel("tiempo [sg]")
plt.ylabel("amplitud [grados]")
plt.xlim(0, 60)
# Lineas de división
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.yticks([-1.5 * amplitud_max, 0, 1.5 * amplitud_max])
# Expresiones matemáticas con látex
plt.text(35, -8, r'$T=2\pi\sqrt{\frac{l}{g}}=$' + f"{periodo:2.2f} sg", fontsize=9)
plt.text(35, -10, r'$f=\displaystyle\frac{l}{T}=$' + f"{frecuencia:2.2f} hz", fontsize=9)
plt.text(35, -12, r'$\omega=2\pi f=$' + f"{angular:2.2f} radianes/sg", fontsize=9)
# Salida en pantalla via Qt
plt.show()
# Salida estándar por consola
print("----------------------------------------------------")

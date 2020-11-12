# test_09.py
''' GRÁFICAS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Las funciones en Python se definen con la palabra clave def, seguida del nombre de la función.
Sus parámetros se escriben entre parentesis y pueden incluir valores por defecto.
Otra forma de escribir funciones, aunque menos utilizada, es con la palabra clave lambda.
El valor devuelto en las funciones con def será el dado con la instrucción return. '''
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
frecuencia = 2 * pi / periodo
# Vector de tiempo
tiempo = np.linspace(0, 60, 256, endpoint=True)
# Vectores de posición
K = amplitud_max * exp(-coeficiente_de_amortiguamiento * tiempo)
position = K * np.cos(frecuencia * tiempo)
velocidad = K * np.sin(frecuencia * tiempo)
# Gráficas
plt.plot(tiempo, position, label="Posición(\u03B8)")
plt.plot(tiempo, velocidad, label="Velocidad(\u03B8)")
# Propiedades de las gráficas
plt.title("Gráficas Trigonométricas")
plt.xlabel("tiempo [sg]")
plt.ylabel("amplitud [grados]")
plt.xlim(0, 60)
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.yticks([-1.5 * amplitud_max, 0, 1.5 * amplitud_max])

plt.legend()
plt.show()
# Salida estándar
print("----------------------------------------------------")

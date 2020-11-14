# test_09.py
''' GRÁFICAS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' La generación de gráficos en Python requiere módulos adicionales.
Existe una gran variedad de módulos para hacer gráficos de todo tipo con Python.
Asi como el estándar de facto en ciencia para la operación numérica es NumPy,
Matplotlib hace posible la generación de estos gráficos a partir de datos contenidos en listas o arrays. '''

# Importar módulos incluidos en Python por defecto
from sys import version as Py_version
from time import gmtime as time
from math import sqrt

# Importar módulos que deben ser instalados
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, pi

# Declaración de variables
amplitud_max = 4
coeficiente_de_amortiguamiento = 0.07
longitud = 10
gravedad = 9.8

# Asignaciones y llamado a funciones
periodo = 2 * pi * sqrt(longitud/gravedad) 
frecuencia = 1 / periodo
angular = 2 * pi * frecuencia

# Construcción del vector de tiempo en NumPy
tiempo = np.linspace(0, 60, 256, endpoint=True)

# Operación con vectores en NumPy de posición
K = amplitud_max * exp(-coeficiente_de_amortiguamiento * tiempo)
position = K * np.cos(angular * tiempo)
velocidad = K * np.sin(angular * tiempo)

# Gráficas
plt.plot(tiempo, position, label="Posición x(\u03B8)")
plt.plot(tiempo, velocidad, label="Velocidad v(\u03B8)")
plt.legend()

# Propiedades de las gráficas - Texto
plt.title("Posición y Velocidad del Péndulo Simple")
plt.xlabel("tiempo [sg]")
plt.ylabel("amplitud [grados]")

# Propiedades de las gráficas - Limites
plt.xlim(0, 60)
limites_x = plt.xlim()

# Lineas de división
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.yticks([-1.5 * amplitud_max, 0, 1.5 * amplitud_max])

# Expresiones matemáticas con MathTex (Matplotlib)
plt.text(35, -8, r'$T=2\pi\sqrt{\frac{l}{g}}=$' + f"{periodo:2.2f} sg", fontsize=9)
plt.text(35, -10, r'$f=frac{l}{T}=$' + f"{frecuencia:2.2f} hz", fontsize=9)
plt.text(35, -12, r'$\omega=2\pi f=$' + f"{angular:2.2f} radianes/sg", fontsize=9)
plt.text(1, -1.45 * amplitud_max, f"Metodos Numéricos (Ortiz, {time().tm_year})", fontsize=5)

# Salida en pantalla via TK
plt.show()

# Salida estándar por consola
print("----------------------------------------------------")
print(f" Matplotlib importado con éxito")
print("----------------------------------------------------")
print(f" Versión Python:        {Py_version.split(' ')[0]}")
print(f" Versión NumPy:         {np.__version__}")
print(f" Version Matplotlib:    {matplotlib.__version__}")
print(f" Backend gráfico:       {matplotlib.get_backend()}")
print("----------------------------------------------------")

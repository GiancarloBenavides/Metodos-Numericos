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
import matplotlib.pyplot as pl

x = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
y1 = np.cos(x)
y2 = np.sin(x)

pl.plot(x,y1)
pl.plot(x,y2)
pl.show()

# Salida estándar
print("----------------------------------------------------")
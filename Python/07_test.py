# test_06.py
''' IMPORTAR MÓDULOS NO INCLUIDOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Los módulos que no están incluidos deben instalarse para poder importarse.
Los módulos de Python están disponibles para instalar con cualquier administrador de paquetes.
Los administradores de paquetes son herramientas como pip de Pypi o conda de Anaconda
EJEMPLO:
→ D:\> pip install numpy.
→ D:\> conda install numpy.
NOTAS:
→ Anaconda administra las dependencias y permite instalar software no Python. 
→ Pypi es un repositorio que hace disponible mas de 270K paquetes. '''

# Importar módulos instalados
import sys
import math as m
from math import pi, e
import numpy as np

# Operaciones con números
n1 = (1+m.sqrt(5))/2
n2 = e
n3 = pi

# Operaciones con el modulo
numero_de_redondeos = 5
x1, y1, z1 = round(n1, 3), round(n2, 3), round(n3, 3)
x2, y2, z2 = int(n1), int(n2), int(n3)
x3, y3, z3 = m.floor(n1), m.floor(n2), m.floor(n3)
x4, y4, z4 = m.ceil(n1), m.ceil(n2), m.ceil(n3)
x5, y5, z5 = m.trunc(n1), m.trunc(n2), m.trunc(n3)

# Salida estándar
print(f"----------------------------------------------------")
print(f" NumPy importado con éxito")
print(f" Versión Python: {sys.version.split(' ')[0]}")
print(f" Versión NumPy:  {np.__version__}")
print(f"----------------------------------------------------")
print(f' Número áureo:       {n1}')
print(f' Número de euler:    {n2}')
print(f' Número pi:          {n3}')
print(f"----------------------------------------------------")
print(f" Redondeo \ Número    |  áureo  |  euler  |    pi    |")
print(f"----------------------------------------------------")
print(f' Redondeo con round() |   {x1} |  {y1}  |   {z1}  |')
print(f' Redondeo con int()   |   {x2}     |  {y2}      |   {z2}      |')
print(f' Redondeo con floor() |   {x3}     |  {y3}      |   {z3}      |')
print(f' Redondeo con ceil()  |   {x4}     |  {y4}      |   {z4}      |')
print(f' Redondeo con trunc() |   {x5}     |  {y5}      |   {z5}      |')
print("----------------------------------------------------")

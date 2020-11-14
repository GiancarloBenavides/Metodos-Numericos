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

# Importar módulos de la biblioteca estándar (incluidos)
from sys import version as Py_version
from time import localtime, strftime
from math import floor, ceil, trunc, sqrt, pi, e
from matplotlib.pyplot import xlim

# Importar módulos que necesitan ser instalados
import numpy as np

# Asignaciones y operaciones con números
n1 = (1+sqrt(5))/2
n2 = e
n3 = pi

# Asignaciones y llamado a funciones de módulos incluidos en Python por defecto
numero_de_redondeos = 5
x1, y1, z1 = round(n1, 3), round(n2, 3), round(n3, 3)
x2, y2, z2 = int(n1), int(n2), int(n3)
x3, y3, z3 = floor(n1), floor(n2), floor(n3)
x4, y4, z4 = ceil(n1), ceil(n2), ceil(n3)
x5, y5, z5 = trunc(n1), trunc(n2), trunc(n3)

# Asignaciones y llamado a funciones de módulos incluidos en NumPy
au = np.array([n1, x1, x2, x3, x4, x5]) # Asignación de los redondeos del número áureo en un vector  
eu = np.array([n2, y1, y2, y3, y4, y5]) # Asignación de los redondeos del número euler en un vector  
pi = np.array([n3, z1, z2, z3, z4, z5]) # Asignación de los redondeos del número pi en un vector  

# Salida estándar
print(f"-----------------------------------------------------")
print(f" Fecha: {strftime('%b %d de %Y a las %I:%M:%S %p', localtime())}")
print(f" NumPy importado con éxito")
print(f" Versión Python: {Py_version.split(' ')[0]}")
print(f" Versión NumPy:  {np.__version__}")
print(f"-----------------------------------------------------")
print(f' Número áureo:       {au[0]}')
print(f' Número de euler:    {eu[0]}')
print(f' Número pi:          {pi[0]}')
print(f"-----------------------------------------------------")
print(f" Redondeo \ Número    |  Áureo  |  Euler  |    Pi    |")
print(f"-----------------------------------------------------")
print(f' Redondeo con round() |   {au[1]:.3f} |  {eu[1]:.3f}  |   {pi[1]:.3f}  |')
print(f' Redondeo con int()   |   {au[2]:.3f} |  {eu[2]:.3f}  |   {pi[2]:.3f}  |')
print(f' Redondeo con floor() |   {au[3]:.3f} |  {eu[3]:.3f}  |   {pi[3]:.3f}  |')
print(f' Redondeo con ceil()  |   {au[4]:.3f} |  {eu[4]:.3f}  |   {pi[4]:.3f}  |')
print(f' Redondeo con trunc() |   {au[5]:.3f} |  {eu[5]:.3f}  |   {pi[5]:.3f}  |')
print("-----------------------------------------------------")

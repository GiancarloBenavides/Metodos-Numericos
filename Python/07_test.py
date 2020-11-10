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
import math as m
from math import pi, e
import numpy as np

# Operaciones con números
x1=(1+m.sqrt(5))/2
x2=e
x3=pi

# Operaciones con el modulo
y1=round(x3,3)
y2=m.floor(x3)
y3=m.ceil(x3)

# Salida estándar
print("----------------------------------------------------")
print(f"NumPy importado con éxito en su version:  {np.__version__}")
print("----------------------------------------------------")
print(f'Número áureo:       {x1}')
print(f'Número de euler:    {x2}')
print(f'Número pi:          {x3}')
print(f'redondear:          {y1}')
print(f'redondear:          {y2}')
print(f'redondear:          {y3}')

'''
def runpete ():
    """ Esto es una prueba """
    return ("ok")

if(True):
    k=-1
else:
    k=1

runpete()'''

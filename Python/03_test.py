# test_01.py 
''' para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Importando módulos biblioteca estandar
import math
from math import pi

# Entrada estandar
radio = input("Elige el radio del circulo [cm]:    ")
radio = int(radio)
area=pi*pow(radio, 2)

# Salida estándar
print("-----------------------------------------")
print(f"El area del circulo: {area:7.2f} cm")
print("-----------------------------------------")
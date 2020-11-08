# test_01.py
''' para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Importando módulos biblioteca estándar
"""
La mayor parte del poder de un lenguaje de programación está en sus bibliotecas.
Un programa debe importar un módulo de biblioteca para poder usarlo.
Use help() para conocer el contenido de un módulo de biblioteca.
"""

# Entrada estándar
import math as m        # Alias para una biblioteca
from math import pi     # Elementos específicos
radio = input("Elige el radio del circulo [cm]:    ")

radio = int(radio)
diametro = 2 * radio
area = m.pi * pow(radio, 2)
circunferencia = 2 * pi * radio

# Salida estándar
print("-----------------------------------------")
print(f"El diámetro del circulo es:        {diametro:5.1f} cm")
print(f"La circunferencia del circulo es:  {circunferencia:5.1f} cm")
print(f"El área aproximada del circulo es: {area:5.1f} cm\u00b2")
print("-----------------------------------------")

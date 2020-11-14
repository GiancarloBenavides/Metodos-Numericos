# test_05.py
''' BIBLIOTECA ESTÁNDAR 
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Importando módulos biblioteca estándar
""" La mayor parte del poder de un lenguaje de programación está en sus bibliotecas.
Un programa debe importar un módulo de biblioteca para poder usarlo.
Use help() para conocer el contenido de un módulo de biblioteca. """

# Biblioteca Estándar incluida "Built-in"
import os               # Importar toda la biblioteca para manejo del sistema operativo
import sys              
import time
import math as m        # Alias para una biblioteca estándar de funciones matemáticas Math
from math import pi     # Elementos específicos

# Mensaje de bienvenida por salida estándar
print("----------------------------------------------")
print(f"  Plataforma Tipo {str(os.name).upper()} de {os.cpu_count( )} núcleos")
print(f"  Python {sys.version.split(' ')[0]} funcionando correctamente")
print(f"  Usuario:  {os.getlogin()}")
print(f"  Fecha:    {time.strftime('%b %d de %Y a las %I:%M:%S %p', time.localtime())}")
print("----------------------------------------------")

# Entrada estándar
radio = input("Elige el radio del circulo [cm]:    ")

# Asignaciones y funciones estándar
radio = int(radio)
diámetro = 2 * radio
area = m.pi * pow(radio, 2)
circunferencia = 2 * pi * radio

# Salida estándar
print("----------------------------------------------")
print(f"El diámetro del circulo es:        {diámetro:5.1f} cm")
print(f"La circunferencia del circulo es:  {circunferencia:5.1f} cm")
print(f"El área aproximada del circulo es: {area:5.1f} cm\u00b2")
print("----------------------------------------------")

# test_04.py
''' CONSTRUCCIÓN Y ASIGNACIÓN DE VARIABLES"
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Operadores y formato de tipos numéricos
""" En programación, un constructor es una subrutina cuya misión es iniciar un objeto.
El proceso incluye la operación de asignación de un valor inicial a la variable.
Python reserva una palabra para los constructores de cada uno de los tipos de datos. """

# Importando funcionalidad al script 
from math import ceil
from typing import FrozenSet, List
import colorama
colorama.init(autoreset=True)
Números = colorama.Fore.YELLOW
Secuencias = colorama.Fore.CYAN
Colecciones = colorama.Fore.MAGENTA
Diccionarios = colorama.Fore.GREEN

# Entrada estándar
x1 = int(input("Elige un número entero [1-9]:    "))
Entero_1 = x1

# Iniciar variables usando constructores
Entero_2 = int("10")
Lógico = bool(Entero_1)
Real = float(Entero_1)
Complejo = complex(Entero_1, Real)
Cadena = str(Real)
Rango = range(Entero_1, Entero_2)
Lista = list(Rango)
Tupla = tuple(Lista)

# Iniciar variables usando constructores y asignación Multiple
a, b, c = 1 , 2, 3    # Asignación literal y multiple
Colección, Colección_inmutable = set(Rango), frozenset(Rango)

# Iniciar variables con asignación Literal
Diccionario = {'Entero':Entero_1,'Nombre':'Metodos', 'lista':Lista[0:2] ,'a':a,'b':b }

# El "=" es el operador de asignación básica, pero se puede conbinar con otros operadores.
# Este tipo de asignaciones permiten obtener distintos resultados.
# --------------------------------------------------------------------
# Asignación y suma:                  x+=a   equivalente a   x=x+a 
# Asignación y resta:                 x-=a   equivalente a   x=x-a 
# Asignación y multiplicación:        x*=a   equivalente a   x=x*a 
# Asignación y division:              x/=a   equivalente a   x=x/a
# --------------------------------------------------------------------
Tu = 9
Tu += 2; Tu -= 3; Tu *= 4; Tu /= 5          # x = ? 6.4
Tu = ceil(Tu)                               # x = ? 7  
# --------------------------------------------------------------------
# Asignación y modulo:                x%=a   equivalente a   x=x%a 
# Asignación y division entera:      x//=a   equivalente a   x=x//a 
# Asignación y potencia:             x**=a   equivalente a   x=x**a 
# --------------------------------------------------------------------
Numero = Tu
Numero %= 4; Numero //= 3; Numero **= 2     # x = ? 1
# --------------------------------------------------------------------
# Asignación y and lógico:            x&=a   equivalente a   x=x&a 
# Asignación y or lógico:             x|=a   equivalente a   x=x|a 
# Asignación y xor lógico:            x^=a   equivalente a   x=x^a 
# --------------------------------------------------------------------
Binario = Numero
Binario &= 2; Binario |= 3; Binario ^= 4    # x = ? 7
# --------------------------------------------------------------------
# Asignación y desplazamiento derecha:    x>>=a  equivalente a  x = x + a 
# Asignación y desplazamiento izquierda:  x<<=a  equivalente a  x = x + a 
# --------------------------------------------------------------------
Es = Binario
Es >>= 2; Es <<= 1                          # x = ? 2
# --------------------------------------------------------------------

# Salida estándar
print("-----------------------------------------------")
print("               NÚMEROS EN PYTHON               ")
print("-----------------------------------------------")
print(f"Un numero entero:           ", end=""); print(Números + f"{Entero_1}")
print(f"Un numero lógico:           ", end=""); print(Números + f"{Lógico}")
print(f"Un numero real:             ", end=""); print(Números + f"{Real}")
print(f"Un numero complejo:         ", end=""); print(Números + f"{Complejo}")
print("-----------------------------------------------")
print("              SECUENCIAS EN PYTHON             ")
print("-----------------------------------------------")
print(f"Una cadena:                 ", end=""); print(Secuencias + f"'{Cadena}'")
print(f"Una rango:                  ", end=""); print(Secuencias + f"{Rango}")
print(f"Una lista:                  ", end=""); print(Secuencias + f"{Lista}")
print(f"Una tupla:                  ", end=""); print(Secuencias + f"{Tupla}")
print("-----------------------------------------------")
print("             COLECCIONES EN PYTHON             ")
print("-----------------------------------------------")
print(f"Una colección:              ", end=""); print(Colecciones + f"{Colección}")
print(f"Una colección inmutable:    ", end=""); print(Colecciones + f"{Colección_inmutable}")
print("-----------------------------------------------")
print("             DICCIONARIOS EN PYTHON            ")
print("-----------------------------------------------")
print(f"Los diccionarios son pares clave-valor:")
print(Diccionarios + f"\n{Diccionario}")
print("-----------------------------------------------")
print(f"Tu Número Binario es:   {Tu}{Numero}{Binario}{Es} ")
print("-----------------------------------------------")

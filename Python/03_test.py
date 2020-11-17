# test_03.py
''' VARIABLES Y TIPOS DE DATOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Tipos de datos estándar de python 3
""" En programación, los tipos de datos definen los valores que puede tomar una variable.
En Python existen 14 tipos de datos básicos con sus operaciones asociadas.
Todo valor que pueda ser asignado a una variable tiene asociado un tipo de dato.
En Python todos los tipos de datos son objetos que heredan de una meta-clase. """

# Árbol de Tipos 
print("-------------------------")
print(" TIPOS DE DATOS EN PYTHON")
print("-------------------------")
print(f" OBJETOS")

# Tipos numéricos
print(f"  \u251c\u2500 NÚMEROS")
_Entero = int(5)
_Lógico = bool(5)
_Real = float(5)
_Complejo = complex(1, 5)
print(f"      \u251c\u2500 Entero ------- {_Entero}")
print(f"      \u251c\u2500 Lógico ------- {_Lógico}")
print(f"      \u251c\u2500 Real --------- {_Real}")
print(f"      \u2514\u2500 Complejo ----- {_Complejo}\n")

# Tipos de secuencias
print(f"  \u251c\u2500 SECUENCIAS")
_Cadena = str("Esto es una cadena")
_Unicode = str(U"\u01e4\u03af\u03b1\u03b7c\u03b1rl\u03c3")
_Lista = list([1, 2, 3, '...'])
_Octeto = bytearray('esto es un byte', 'utf-8')
_Octetos = bytes('esto es un byte', 'utf-8')
_Tupla = tuple(_Lista)
_Rango = range(3)
print(f"      \u251c\u2500 MUTABLES")
print(f"          \u251c\u2500 Lista ----------------- {_Lista}")
print(f"          \u2514\u2500 Secuencia de Bytes ---- {_Octeto}")
print(f"      \u2514\u2500 INMUTABLES")
print(f"          \u251c\u2500 Bytes ----------------- {_Octetos}")
print(f"          \u251c\u2500 Cadena de caracteres - '{_Cadena}'")
print(f"          \u251c\u2500 Tupla ----------------- {_Tupla}")
print(f"          \u2514\u2500 Rango ----------------- {_Rango}\n")

# Tipos de colecciones
print(f"  \u251c\u2500 COLECCIONES")
_Set = set(_Lista)
_Frozenset = frozenset(_Lista)
print(f"      \u251c\u2500 MUTABLES")
print(f"          \u2514\u2500 Set -------- {_Set}")
print(f"      \u2514\u2500 INMUTABLES")
print(f"          \u2514\u2500 Frozenset -- {_Frozenset}\n")

# Tipos de mapeos
print(f"  \u2514\u2500 MAPEOS")
_Diccionario = {'Llave': 'valor', '...': '...'}
print(f"      \u2514\u2500 Diccionarios --- {_Diccionario}\n")
print(f"                                                '{_Unicode}'")

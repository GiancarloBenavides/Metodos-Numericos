# test_03.py
''' TIPOS DE DATOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Entrada y salida estándar de python 3
""" En programación, los flujos estándar son canales de comunicación de entrada y salida.
Estos canales conectan el programa de computadora y su entorno.
Permiten introducir y recibir datos desde el programa. """
print("-------------------------")
print(" TIPOS DE DATOS EN PYTHON")
print("-------------------------")
print(f" OBJETOS")
print(f"  \u251c\u2500 NÚMEROS")
# Tipos numéricos
_Entero = int(5)
_Lógico = bool(5)
_Real = float(5)
_Complejo = complex(1, 5)
print(f"      \u251c\u2500 Entero ------- {_Entero}")
print(f"      \u251c\u2500 Lógico ------- {_Lógico}")
print(f"      \u251c\u2500 Real --------- {_Real}")
print(f"      \u2514\u2500 Complejo ----- {_Complejo}\n")
print(f"  \u251c\u2500 SECUENCIAS")
# Tipos de secuencias
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
print(f"  \u251c\u2500 COLECCIONES")
# Tipos de colecciones
_Set = set(_Lista)
_Frozenset = frozenset(_Lista)
print(f"      \u251c\u2500 MUTABLES")
print(f"          \u2514\u2500 Set -------- {_Set}")
print(f"      \u2514\u2500 INMUTABLES")
print(f"          \u2514\u2500 Frozenset -- {_Frozenset}\n")
print(f"  \u2514\u2500 MAPEOS")
# Tipos de mapeos
_Diccionario = {'Llave': 'valor', '...': '...'}
print(f"      \u2514\u2500 Diccionarios --- {_Diccionario}\n")
print(f"                                                '{_Unicode}'")

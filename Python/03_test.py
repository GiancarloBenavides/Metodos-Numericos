# test_03.py
''' VARIABLES Y TIPOS DE DATOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Tipos de datos estándar de python 3
""" En programación, los tipos de datos definen los valores que puede tomar una variable.
En Python existen 14 tipos de datos básicos con sus operaciones asociadas.
Todo valor que pueda ser asignado a una variable tiene asociado un tipo de dato.
En Python todos los tipos de datos son objetos que heredan de una meta-clase. """

# Identificadores
""" En programación los identificadores son nombres que hacen referencia a los objetos que componen un programa.
Estos pueden ser constantes, variables, funciones, clases, etc...
En Python existen una reglas para usar identificadores:
> El primer carácter debe ser una letra o el carácter de subrayado [a-z, A-Z, _]
> El segundo y siguientes pueden ser dígitos, letras o carácteres de subrayado [a-z, A-Z, 1-9, _]
> No pueden utilizarse espacios en blanco, símbolos de puntuación o palabras reservadas del lenguaje
> Python distingue mayúsculas y minúsculas. """

# El ámbito
""" En programación, el ámbito es el contexto que pertenece un identificador dentro de un programa.
Esto es util cuando se requiere definir dos variable con el mismo identificador en diferentes partes del programa.
En python las variables definidas en una función son locales a la función y no existen fuera de ella.
Las funciones dentro de los script son globales y cualquier sentencia puede modificarla. """

# Estilo de identificadores - La legibilidad cuenta
CONSTANTE = 1           # Mayúsculas - Por convención constante    
VARIABLE = 2
Variable = 3
_Privado = 4            # Un subrayado simple - Por convención privado
__Privado = 5           # Un subrayado doble - Marcados para renombrar en una clase
__Privado__ = 6_000     # Dos subrayados doble - Especiales
Lista = [CONSTANTE, VARIABLE, Variable, _Privado, __Privado, __Privado__]


# Árbol de Tipos 
print("-------------------------")
print(" TIPOS DE DATOS EN PYTHON")
print("-------------------------")
print(f" OBJETOS")

# Tipos numéricos
print(f"  \u251c\u2500 NÚMEROS")
_Entero = 5
_Lógico = True
_Real = 5.0
_Complejo = 1.7 + 5j
print(f"      \u251c\u2500 Entero ------- {_Entero}")
print(f"      \u251c\u2500 Lógico ------- {_Lógico}")
print(f"      \u251c\u2500 Real --------- {_Real}")
print(f"      \u2514\u2500 Complejo ----- {_Complejo}\n")

# Tipos de secuencias
print(f"  \u251c\u2500 SECUENCIAS")
_Cadena = "Esto es una cadena"
_Unicode = U"\u01e4\u03af\u03b1\u03b7c\u03b1rl\u03c3"
_Lista = [1, 2, 3, '...']
_Octeto = bytearray('esto es un array de bytes', 'utf-8')
_Octetos = b'esto es una cadena de bytes'
_Tupla = (1, 2, 3, '...')
_Rango = range(0, 3)
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
_Set = {1, 2, 3, '...'}
_Frozenset = frozenset({1, 2, 3, '...'})
print(f"      \u251c\u2500 MUTABLES")
print(f"          \u2514\u2500 Set -------- {_Set}")
print(f"      \u2514\u2500 INMUTABLES")
print(f"          \u2514\u2500 Frozenset -- {_Frozenset}\n")

# Tipos de mapeos
print(f"  \u2514\u2500 MAPEOS")
_Diccionario = {'Llave': 'valor', '...': '...'}
print(f"      \u2514\u2500 Diccionarios --- {_Diccionario}\n")
print(f"                                                '{_Unicode}'")

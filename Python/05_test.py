# test_05.py
''' OPERADORES y FORMATO"
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Operadores y formato de tipos numéricos
""" En programación, los operadores se utilizan para obtener resultados desde otros datos o elementos.
En Python estos elementos sobre los que se aplica la operación pertenecen a un tipo de dato.
Cada tipo de dato tiene definidas las operaciones posibles entre sus elementos u objetos.
Las operaciones se realizan operando sobre uno, dos o más objetos y tipos de datos.
Los operadores son símbolos reservados por el propio lenguaje. """

# Importando funcionalidad al script 
from fractions import Fraction as frac
import colorama
colorama.init(autoreset=True)
Externo = colorama.Fore.RED
Interno = colorama.Fore.GREEN
Titulo = colorama.Fore.BLUE
Subtitulo = colorama.Fore.CYAN

# Agregando funcionalidad al script
def tipo (t):
    tipo = str(type(t)).split("'")[1]
    return tipo

def bites(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

'''
def binary(number):
    if number < 0:
        return bin((eval("0b"+str(int(bin(number)[3:].zfill(4).replace("0","2").replace("1","0").replace("2","1"))))+eval("0b1")))[2:].zfill(4)
    return bin(number)[2:].zfill(4)      
'''

###########################
# OPERACIONES CON NÚMEROS #
###########################

# Operaciones con enteros
print(f"-----------------------------------------------------")
print(Titulo + f"            OPERACIONES CON NÚMEROS ENTEROS          ")
Entero_1 = 2
Entero_2 = 10
Suma_entera = Entero_1 + Entero_2
Resta_entera = Entero_1 - Entero_2
Multiplicación_entera = Entero_1 * Entero_2     # Operación interna
Division_entera = Entero_1 / 2                  # Operación externa
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los enteros a={Entero_1}, b={Entero_2} se define:")
print(f"-----------------------------------------------------")
print(f"Suma:                    (a+b)= {Suma_entera}            ->    ", end=""); print(Interno + f"{tipo(Suma_entera)}")
print(f"Resta:                   (a-b)= {Resta_entera}            ->    ", end=""); print(Interno + f"{tipo(Resta_entera)}")
print(f"Multiplicación:          (a*b)= {Multiplicación_entera}            ->    ", end=""); print(Interno + f"{tipo(Multiplicación_entera)}")
print(f"Division:                (b/a)= {Division_entera:.2f}          ->    ", end=""); print(Externo + f"{tipo(Division_entera)}")

# operaciones con enteros a nivel de bit
Entero_1 = 4
Entero_2 = 2
OR_binaria = Entero_1 | Entero_2
XOR_binaria = Entero_1 ^ Entero_2
AND_binaria = Entero_1 & Entero_2
Desplaza_izq = Entero_1 << Entero_2
Desplaza_der = Entero_1 >> Entero_2
NOT_binaria = ~Entero_1
Complemento = bites(NOT_binaria, 8)
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los enteros a={Entero_1}, b={Entero_2} se define:")
print(f"-----------------------------------------------------")
print(f"OR:                      (a|b)= {OR_binaria}             ->    ", end=""); print(Interno + f"{tipo(OR_binaria)}")
print(f"XOR:                     (a^b)= {XOR_binaria}             ->    ", end=""); print(Interno + f"{tipo(XOR_binaria)}")
print(f"AND:                     (a&b)= {AND_binaria}             ->    ", end=""); print(Interno + f"{tipo(AND_binaria)}")
print(f"Izquierda:              (a<<b)= {Desplaza_izq}            ->    ", end=""); print(Interno + f"{tipo(Desplaza_izq)}")
print(f"Derecha:                (a>>b)= {Desplaza_der}             ->    ", end=""); print(Interno + f"{tipo(Desplaza_der)}")

# Operaciones con fraccionarios
print(f"-----------------------------------------------------")
print(Titulo + f"        OPERACIONES CON NÚMEROS FRACCIONARIOS        ")
Fraccionario_1 = frac(3, 2)
Fraccionario_2 = frac("1/2")
Suma_fraccionaria = Fraccionario_1 + Fraccionario_2
Multiplicación_fraccionaria = Fraccionario_1 * Fraccionario_2
Division_fraccionaria = Fraccionario_1 / Fraccionario_2           # Operación interna
Potencia_fraccionaria = Fraccionario_1 ** Fraccionario_2          # Operación externa
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los fraccionarios a/b={Fraccionario_1}, c/d={Fraccionario_2} se define:")
print(f"-----------------------------------------------------")
print(f"Suma:              (a/b + c/d)= {Suma_fraccionaria}             ->    ", end=""); print(Interno + f"{tipo(Suma_fraccionaria)}")
print(f"Multiplicación:    (a/b * c/d)= {Multiplicación_fraccionaria}           ->    ", end=""); print(Interno + f"{tipo(Multiplicación_fraccionaria)}")
print(f"Division:          (a/b / c/d)= {Division_fraccionaria}             ->    ", end=""); print(Interno + f"{tipo(Division_fraccionaria)}")
print(f"Potencia:         (a/b ** c/d)= {Potencia_fraccionaria:.2f}          ->    ", end=""); print(Externo + f"{tipo(Potencia_fraccionaria)}")

# Operaciones con reales
print(f"-----------------------------------------------------")
print(Titulo + f"           OPERACIONES CON NÚMEROS REALES            ")
Real_1 = -3.0
Real_2 = 2.0
Suma_real = Real_1 + Real_2
Multiplicación_real = Real_1 * Real_2       
Division_real = Real_1 / Real_2             
Modulo = Real_1 % Real_2                      # Operación interna
Potencia_real = pow(Real_1, Real_2)           # Operación externa
Radical_real = Real_1**(1/Real_2)               # Operación externa
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los Reales a={Real_1}, b={Real_2} se define:")
print(f"-----------------------------------------------------")
print(f"Suma:                    (a+b)= {Suma_real:.2f}         ->    ", end=""); print(Interno + f"{tipo(Suma_real)}")
print(f"Multiplicación:          (a*b)= {Multiplicación_real:.2f}         ->    ", end=""); print(Interno + f"{tipo(Multiplicación_real)}")
print(f"Division:                (a/b)= {Division_real:.2f}         ->    ", end=""); print(Interno + f"{tipo(Division_real)}")
print(f"Modulo:                  (a%b)= {Modulo:.2f}          ->    ", end=""); print(Interno + f"{tipo(Modulo)}")
print(f"Potencia:               (a**b)= {Potencia_real:.2f}          ->    ", end=""); print(Interno + f"{tipo(Potencia_real)}")
print(f"Radicación:         (a**(1/b))= {Radical_real:.1f}      ->    ", end=""); print(Externo + f"{tipo(Radical_real)}")
 
# Operaciones con complejos
print(f"-----------------------------------------------------")
print(Titulo + f"          OPERACIONES CON NÚMEROS COMPLEJOS          ")
Complejo_1 = 3 + 0j
Complejo_2 = 1j
Suma_compleja = Complejo_1 + Complejo_2
Multiplicación_compleja = Complejo_1 * Complejo_2
Division_compleja = Complejo_1 / Complejo_2
Potencia_compleja = Complejo_1 ** Complejo_2
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los Reales a={Complejo_1}, b={Complejo_2} se define:")
print(f"-----------------------------------------------------")
print(f"Suma:                    (a+b)= {Suma_compleja:.0f}          ->    ", end=""); print(Interno + f"{tipo(Suma_compleja)}")
print(f"Multiplicación:          (a*b)= {Multiplicación_compleja:.0f}          ->    ", end=""); print(Interno + f"{tipo(Multiplicación_compleja)}")
print(f"Division:                (a/b)= {Division_real:.2f}         ->    ", end=""); print(Interno + f"{tipo(Division_real)}")
print(f"Potencia:               (a**b)= {Potencia_compleja:.2f}    ->    ", end=""); print(Interno + f"{tipo(Potencia_compleja)}")

# Operaciones lógicas con boleanos
print(f"-----------------------------------------------------")
print(Titulo + f"      OPERACIONES LÓGICAS CON NÚMEROS BOLEANOS       ")
Lógico_1 = bool(5)
Lógico_2 = bool(0)
Negación = not Lógico_1
Suma_lógica = Lógico_1 or Lógico_2
Multiplicación_lógica = Lógico_1 and Lógico_2
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los Reales a={Lógico_1}, b={Lógico_2} se define:")
print(f"-----------------------------------------------------")
print(f"Negación:              (not a)= {Negación}         ->    ", end=""); print(Interno + f"{tipo(Negación)}")
print(f"Suma:                 (a OR b)= {Suma_lógica}          ->    ", end=""); print(Interno + f"{tipo(Suma_lógica)}")
print(f"Multiplicación:      (a AND b)= {Multiplicación_lógica}         ->    ", end=""); print(Interno + f"{tipo(Multiplicación_lógica)}")

# Operaciones de comparación numérica que resultan en boleanos
print(f"-----------------------------------------------------")
print(Titulo + f"       OPERACIONES DE COMPARACIÓN CON NÚMEROS        ")
Num_1 = 5
Num_2 = 5.0
Num_3 = 5 + 0j
Num_4 = 0.1
Num_5 = 0.2
Num_6 = 0.3
Igual = Num_1 == Num_2
Distinto = Num_1 != Num_3
Menor = (0.1 + 0.2) <= (0.3)
Mayor = (0.1 + 0.2) > (0.3)
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los números a={Num_1}, b={Num_2} c={Num_3} se define:")
print(f"-----------------------------------------------------")
print(f"Igual:                  (a==b)= {Igual}          ->    ", end=""); print(Externo + f"{tipo(Igual)}")
print(f"Distinto:               (a!=b)= {Distinto}         ->    ", end=""); print(Externo + f"{tipo(Distinto)}")
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean los números a={Num_4}, b={Num_5} c={Num_6} se define:")
print(f"-----------------------------------------------------")
print(f"Menor:              (a+b <= c)= {Menor}         ->    ", end=""); print(Externo + f"{tipo(Menor)}")
print(f"Mayor:               (a+b > c)= {Mayor}          ->    ", end=""); print(Externo + f"{tipo(Mayor)}")
print(f"-----------------------------------------------------")

##############################
# OPERACIONES CON SECUENCIAS #
##############################

# Operaciones con cadenas
print(f"-----------------------------------------------------")
print(Titulo + f"               OPERACIONES CON CADENAS               ")
Cadena_1 = "Hola "
Cadena_2 = "Mundo"
Concatenación = Cadena_1 + Cadena_2
Pertenencia = Cadena_1 in Concatenación
No_pertenencia = "hola" not in Concatenación
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean las cadenas a='{Cadena_1}', b='{Cadena_2}' se define:")
print(f"-----------------------------------------------------")
print(f"Concatenación:         (a+b)= '{Concatenación}'    ->    ", end=""); print(Interno + f"{tipo(Concatenación)}")
print(f"Pertenencia:        (a in b)= {Pertenencia}            ->    ", end=""); print(Externo + f"{tipo(Pertenencia)}")
print(f"No pertenencia: (a not in b)= {No_pertenencia}            ->    ", end=""); print(Externo + f"{tipo(No_pertenencia)}")

# Operaciones con listas
print(f"-----------------------------------------------------")
print(Titulo + f"               OPERACIONES CON LISTAS                ")
Lista_1 = list(range(1, 3))
Lista_2 = ["tres"]
Concatenación_listas = Lista_1 + Lista_2
Pertenencia_listas = 3 in Concatenación_listas
No_pertenencia_listas = 3 not in Concatenación_listas
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean las listas a={Lista_1}, b={Lista_2} se define:")
print(f"-----------------------------------------------------")
print(f"Concatenación:         (a+b)= {Concatenación_listas}  ->    ", end=""); print(Interno + f"{tipo(Concatenación_listas)}")
print(f"Pertenencia:        (3 in b)= {Pertenencia_listas}           ->    ", end=""); print(Externo + f"{tipo(Pertenencia_listas)}")
print(f"No pertenencia: (3 not in b)= {No_pertenencia_listas}            ->    ", end=""); print(Externo + f"{tipo(No_pertenencia_listas)}")

# Operaciones con tuplas
print(f"-----------------------------------------------------")
print(Titulo + f"               OPERACIONES CON TUPLAS                ")
Tupla_1 = (1, "dos")
Tupla_2 = (3,)
Concatenación_tuplas = Tupla_1 + Tupla_2
Pertenencia_tuplas = 2 in Concatenación_tuplas
No_pertenencia_tuplas = 2 not in Concatenación_tuplas
print(f"-----------------------------------------------------")
print(Subtitulo + f"Sean las tuplas a={Tupla_1}, b={Tupla_2} se define:")
print(f"-----------------------------------------------------")
print(f"Concatenación:         (a+b)= {Concatenación_tuplas}   ->    ", end=""); print(Interno + f"{tipo(Concatenación_tuplas)}")
print(f"Pertenencia:        (2 in b)= {Pertenencia_tuplas}           ->    ", end=""); print(Externo + f"{tipo(Pertenencia_tuplas)}")
print(f"No pertenencia: (2 not in b)= {No_pertenencia_tuplas}            ->    ", end=""); print(Externo + f"{tipo(No_pertenencia_tuplas)}")
print(f"-----------------------------------------------------")

# Operaciones entre tipos no permitidas (fuertemente tipado)
# "hola" + 5
# [1, 2] + (3, 4)
# "hola" + 5

# test_04.py
''' OPERADORES y FORMATO"
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Funciones incorporadas en el modulo estándar builtins
""" En programación, una función es una sección reutilizable y aislada de un programa.
Python Dispone de 67 funciones internas que siempre se están disponibles.
Estas están incluidas en un modulo que no necesita importarse.
Naturalmente siempre se pueden sobreescribir estas o definir nuevas funciones. """

def tipo (t):
    tipo = str(type(t)).split("'")[1]
    return tipo

###########################
# OPERACIONES CON NÚMEROS #
###########################

# Operaciones con enteros
Entero = 2
Suma_entera = Entero + 10
Resta_entera = Entero - 10
Multiplicación_entera = Entero * 10     # Operación interna
Division_entera = Entero / 2            # Operación externa

# Operaciones con fraccionarios
from fractions import Fraction
Fraccionario = Fraction('1/2')
Suma_fraccionaria = Fraccionario + Fraction(3, 2)
Multiplicación_fraccionaria = Fraccionario * Fraction(3, 2)
Division_fraccionaria = Fraccionario * Fraction(3, 2)           # Operación interna
Potencia_fraccionaria = Fraccionario ** Fraccionario            # Operación externa

# Operaciones con Reales
Flotante = 3.0
Flotante = 6 / Entero
Suma_real = Flotante + Entero
Multiplicación_real = Flotante * Entero       
Division_real = Flotante / Entero             
Modulo = Flotante % Entero                      # Operación interna
Potencia_real = pow(Flotante, Entero)           # Operación externa
Radical_real = (-Entero)**(1/2)                    # Operación externa

# Operaciones con Complejos
Complejo = 3 + 0j
Complejo = pow(-Entero, (1/2))
Suma_compleja = Complejo + (3 + 5j)
Multiplicación_compleja = Complejo * (3 + 5j)

###########################
# OPERACIONES CON LÓGICOS #
###########################

# Boleanos
Lógico = bool(1)
Lógico = True
Negación = not True
Suma_lógica = Lógico or True
Multiplicación_lógica = Lógico and True

# Comparación
Igual = (5 == 5.0)
Distinto = (5) != (5 + 0J)
Menor = (0.1 + 0.2) <= (0.3)
Mayor = (0.1 + 0.2) >= (0.3)

# Salida estándar
print(f"-----------------------------------------")
print(f"Suma Entera:                    {Suma_entera}        ->    {tipo(Suma_entera)}")
print(f"Resta Entera:                   {Resta_entera}        ->    {tipo(Resta_entera)}")
print(f"Multiplicación Entera:          {Multiplicación_entera}        ->    {tipo(Multiplicación_entera)}")
print(f"Division Entera:                {Division_entera:.2f}      ->    {tipo(Division_entera)}")
print(f"-----------------------------------------")
print(f"Suma Fraccionaria:              {Suma_fraccionaria}         ->    {tipo(Suma_fraccionaria)}")
print(f"Multiplicación Fraccionaria:    {Multiplicación_fraccionaria}       ->    {tipo(Multiplicación_fraccionaria)}")
print(f"Division Fraccionaria:          {Division_fraccionaria}       ->    {tipo(Division_fraccionaria)}")
print(f"Potencia Fraccionaria:          {Potencia_fraccionaria:.2f}      ->    {tipo(Potencia_fraccionaria)}")
print(f"-----------------------------------------")
print(f"Suma Real:                      {Suma_real:.2f}      ->    {tipo(Suma_real)}")
print(f"Multiplicación Real:            {Multiplicación_real:.2f}      ->    {tipo(Multiplicación_real)}")
print(f"Division Real:                  {Division_real:.2f}      ->    {tipo(Division_real)}")
print(f"Modulo:                         {Modulo:.2f}      ->    {tipo(Modulo)}")
print(f"Potencia Real:                  {Potencia_real:.2f}      ->    {tipo(Potencia_real)}")
print(f"Radiación Real:                 {Radical_real:.1f}  ->    {tipo(Radical_real)}")
print(f"-----------------------------------------")
print(f"Negación lógica:                {Negación}     ->    {tipo(Negación)}")
print(f"Suma lógica:                    {Suma_lógica}      ->    {tipo(Suma_lógica)}")
print(f"Multiplicación lógica:          {Multiplicación_lógica}      ->    {tipo(Multiplicación_lógica)}")
print(f"Igual:                          {Igual}      ->    {tipo(Igual)}")
print(f"Distinto:                       {Distinto}     ->    {tipo(Distinto)}")
print(f"Menor:                          {Menor}     ->    {tipo(Menor)}")
print(f"Mayor:                          {Mayor}      ->    {tipo(Mayor)}")
print(f"-----------------------------------------")

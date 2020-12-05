# test_08.py
''' ESTRUCTURAS DE CONTROL
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Estructuras de control
""" En programación, las estructuras de control, permiten tomar decisiones.
las estructuras de control modifican el flujo de ejecución de un programa.
Python dispone de ciclos y condicionales para controlar el flujo de ejecución.
→ Los ciclos son porciones de código que se repite hasta alanzar una condición.
→ Los condicionale son porciones de código que se ejecutan según sea una condición.  """

# Declaración de variables
""" En Python la funcion dir() hace parte de las funciones integradas por defecto.
Sin argumentos, esta funcion devuelve la lista de nombres en el ámbito local actual.
Con un objeto como argumento, intenta listar los identificadores definidos en el objeto. """
directorio = eval("dir(__builtins__)")
callables, noCallables, funciones, noFunciones = [], [], [], []
excepciones, otrasClases, noClases = [], [], []
errores, advertencias, otrasExcepciones, noExcepciones = [], [], [], []
imprimir = []
contador1, contador2 = 0, 0

# Estructuras de control (Ciclos y condicionales)
# ciclo for
""" El bucle for recorre un objeto iterable, como una lista, una tupla o un generador.
En Python el ciclo for se ejecuta exactamente una vez por cada elemento del objeto iterable,
Esto evita que un ciclo se repita no intencionalmente e indefinidamente "Error de bucle infinito."
Cada elemento del iterable se usa mientras se ejecuta el bloque de código interno. """
for i in directorio:
    if callable(eval(i)) == True:
        callables.append(i)
    else:
        noCallables.append(i)

for i in callables:
    try:
        if eval(f"issubclass({i}, BaseException)"):
            excepciones.append(i)
        else:
            otrasClases.append(i)
    except:
        noClases.append(i)

for i in excepciones:
    if "Error" in i:
        errores.append(i)
    elif "Warning" in i:
        advertencias.append(i)
    else:
        otrasExcepciones.append(i)

for i in noClases:
    tipo_cadena = str(type(eval(i))).split("'")[1]
    if ("Printer" in tipo_cadena) or ("Helper" in tipo_cadena):
        imprimir.append(i)
    elif "builtin_function_or_method" == tipo_cadena:
        funciones.append(i)
    else:
        noFunciones.append(i)

# Asignaciones y operaciones con variables
especiales = imprimir + noFunciones
funciones_incluidas = otrasClases + funciones

# Salida estándar
def imprimir_analisis():
    print("-------------------------------------------------")
    print(" DECLARACIONES EN MODULO BUILTIN DE PYTHON       ")
    print("-------------------------------------------------")
    print(f"Total de definiciones incluidas ============= {len(directorio):3d}")
    print(f"  \u251c\u2500 Definiciones no invocables --------- {len(noCallables):3d}")
    print(f"  \u2514\u2500 Definiciones de excepciones -------- {len(excepciones):3d}")
    print(f"      \u251c\u2500 Tipos de error           : {len(errores):2d} :")
    print(f"      \u251c\u2500 Tipos de advertencias    : {len(advertencias):2d} :")
    print(f"      \u2514\u2500 Tipos otras excepciones  : {len(otrasExcepciones):2d} :")
    print(f"  \u2514\u2500 Definiciones especiales ------------ {len(especiales):3d}")
    print(f"      \u251c\u2500 Para imprimir objetos    : {len(imprimir):2d} :")
    print(f"      \u2514\u2500 Para detener ejecución   : {len(noFunciones):2d} :")
    print(f"  \u2514\u2500 Definiciones de funciones ---------- {len(funciones_incluidas):3d}")
    print(f"      \u251c\u2500 Casting de tipos         : {len(otrasClases):2d} :")
    print(f"      \u2514\u2500 Otras funciones          : {len(funciones):2d} :")
    print("-------------------------------------------------")
    print("FUNCIONES BUILTIN")
    print("-------------------------------------------------")
    print(funciones_incluidas)
    print("-------------------------------------------------")

# Ciclo while
""" Este bucle evalúa una condición al inicio de cada repetición.
Si es verdadera, se ejecuta el bloque de código interno e inicia una nueva repetición,
Continúa evaluando y ejecutando mientras la condición sea verdadera.
Este ciclo requiere que la condición se pueda evaluar al inicio del ciclo.
y en el cuerpo debe falsear la condición para terminar el bucle,
de lo contrario la ejecución permanecerá infinitamente. """
opc = ""
while opc != "s":
    print("-------------------------------------------------")
    print(" Fin de análisis de identificadores incluidos...")
    print(" Directorio del Módulo incluido por defecto")
    print("-------------------------------------------------")
    opc = input("Desea imprimir el analisis [s/n]: [ ]\b\b")
    if opc == "s":
        imprimir_analisis()
        break

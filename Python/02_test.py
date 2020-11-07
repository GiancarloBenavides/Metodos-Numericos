# test_01.py 
''' para el curso de métodos numéricos
 por Ing. Giancarlo Ortiz '''
# Entrada estándar
x1 = input("Elige un número entero [1-9]:    ") 

# Funciones incorporadas "Built-in"
x1 = int(x1)
y1 = pow(x1, 3)
y2 = pow(x1, 0.5)

# Salida estándar
print("---------------------------------------")
print(f"Elegiste el número:      {x1:7.2f}")
print(f"El cubo de tu número es: {y1:7.2f}") 
print(f"La raíz de tu número es: {y2:7.2f}")
print("---------------------------------------")
# Generalidades De Python
Generalidades y script de python para el curso de Métodos Numéricos 2020-B

## Contenido:
* **01_test.py** - _Operaciones Con Cadenas_
* **02_test.py** - _Entrada Y Salida Estándar_
* **03_test.py** - _Tipos De Datos_
* **04_test.py** - _Asignación_
* **05_test.py** - _Operadores_
* **06_test.py** - _Funciones Incluidas - "Built-In"_
* **07_test.py** - _Biblioteca Estándar_
* **08_test.py** - _Estructuras De Control_
* **09_test.py** - _Importar Módulos No Incluidos_
* **10_test.py** - _Funciones_
* **11_test.py** - _Gráficas_
* **12_test.py** - _Archivos_

## Operaciones Con Cadenas
---
#### 01_test.py
En programación, las operaciones mas básicas incluyen operaciones con cadenas.
> Python usa la codificación Unicode en lugar de ASCII, lo que hace posibles mas de 100.000 Caracteres.
```python
Type("x") → <class 'str'> # cadena Unicode. 
```
## Entrada Y Salida Estándar
---
#### 02_test.py
En programación, los flujos estándar son canales de comunicación de entrada y salida.
* Estos canales conectan el programa de computadora y su entorno;
lo que hace posible introducir y recibir datos desde el programa. 
> Python incluye por defecto funciones que permiten Entrada/Salida.

## Variables y tipos De Datos
--- 
#### 03_test.py
En programación, los tipos de datos definen los valores que puede tomar una variable.
* Todo valor que pueda ser asignado a una variable tiene asociado un tipo de dato.
> En Python existen **14** tipos de datos básicos con sus operaciones asociadas.
> En Python todos los tipos de datos son objetos que heredan de una meta-clase.

## Construcción y Asignación
---
#### 04_test.py
En programación, un constructor es una subrutina cuya misión es iniciar un objeto.
* El proceso incluye la operación de asignación de un valor inicial a la variable.
> Python reserva una palabra para los constructores de cada uno de los tipos de datos. 

## Operadores
---
#### 05_test.py
En programación, los operadores se utilizan para obtener resultados desde otros datos o elementos.
* Estos elementos sobre los que se aplica la operación pertenecen a un tipo de dato definido en el lenguaje.
* Cada tipo de dato tiene definidas las operaciones posibles entre sus elementos u objetos.
> En Python las operaciones se realizan operando sobre uno, dos o más objetos y tipos de datos.
> En Python Los operadores son símbolos reservados por el propio lenguaje. 

## Funciones Incluidas - "Built-In"
---
#### 06_test.py
En programación, una función es una sección reusable y aislada de un programa.
* Naturalmente siempre se pueden sobrescribir estas o definir nuevas funciones. 
> Python Dispone de **67** funciones internas que siempre se están disponibles.
> Estas están incluidas en un modulo que no necesita importarse.

## Biblioteca Estándar
---
#### 07_test.py
En programación, las bibliotecas representan colecciones de código reusable.
* La mayor parte del poder de un lenguaje de programación está en sus bibliotecas.
* Un programa debe importar un módulo de biblioteca para poder usarlo.
> En Python use **help()** para conocer el contenido de un módulo de biblioteca.

## Estructuras De Control
---
#### 08_test.py
En programación, las estructuras de control, permiten tomar decisiones.
* las estructuras de control modifican el flujo de ejecución de un programa.
> Python dispone de ciclos y condicionales para controlar el flujo de ejecución.
>   → Los ciclos son porciones de código que se repite hasta alanzar una condición.
>   → Los condicionale son porciones de código que se ejecutan según sea una condición. 

## Importar Módulos No Incluidos
---
#### 09_test.py
Los lenguajes de programación incluyen funcionalidad adicional a la biblioteca estándar.
Los módulos que no están incluidos en esta biblioteca deben instalarse o importarse.
> En Python están disponibles en colecciones para instalar con cualquier administrador de paquetes.
> Los administradores de paquetes son herramientas como pip de **PyPi** o **conda** de Anaconda

```shell
# USO DE LOS GESTORES DE PAQUETES EN LA TERMINAL:
# → Anaconda administra las dependencias y permite instalar software no Python.
conda install numpy
# → Pypi es un repositorio que hace disponible mas de 270K paquetes. 
pip install numpy
```

## Funciones
---
#### 10_test.py
En programación las funciones son rutinas que deben declararse antes de invocarse.
* Para declararse o definirse las funciones se usan palabras clave del lenguaje.
* En la declaración se especifica los parámetros de entrada y los valores que retorna la función.
> En Python se definen con la palabra clave def, seguida del nombre de la función.
> El valor devuelto en las funciones con def será el dado con la instrucción return. 
> Sus parámetros se escriben entre paréntesis y pueden incluir valores por defecto.
> Otra forma de escribir funciones en Python, aunque menos utilizada, es con la palabra clave lambda.

## Gráficas
---
#### 11_test.py
En programación la generación de interfaces requiere módulos o librerías adicionales.
* Estas funcionalidades están estrechamente ligadas a la plataforma de ejecución.
* Existe una gran variedad de librerías para hacer gráficos en todas las plataformas.
> En Python, NumPy es el estándar de facto en ciencia para la operación numérica y Matplotlib, 
> lo es para la generación de gráficos a partir de datos contenidos en listas o arrays. 

## Manejo de Archivos
---
#### 12_test.py
Las plataformas exponen funcionalidad a los lenguajes para el manejo del sistema de archivos.
> Python proporciona funciones y métodos básicos para manipular archivos.
> Estos están disponibles en la biblioteca estándar de forma predeterminada.

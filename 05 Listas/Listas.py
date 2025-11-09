# Ejercicio 1

notas = [7, 5, 9, 8, 6, 10, 4, 8, 9, 7]

print("Notas de los estudiantes:")
for i in range(len(notas)):
    print(notas[i], end=" ")
print()

suma = 0
for i in range(len(notas)):
    suma += notas[i]
promedio = suma / len(notas)

mayor = notas[0]
menor = notas[0]
for i in range(1, len(notas)):
    if notas[i] > mayor:
        mayor = notas[i]
    if notas[i] < menor:
        menor = notas[i]

print("Promedio:", promedio)
print("Nota mas alta:", mayor)
print("Nota mas baja:", menor)

# Ejercicio 2

productos = []
for i in range(5):
    producto = input("Ingrese el producto " + str(i + 1) + ": ")
    productos.append(producto)

print("Lista ordenada:")
ordenados = sorted(productos)
for i in range(len(ordenados)):
    print(ordenados[i])

eliminar = input("Que producto desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)
else:
    print("El producto no esta en la lista.")

print("Lista actualizada:")
for i in range(len(productos)):
    print(productos[i])

# Ejercicio 3

import random

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

pares = []
impares = []

for i in range(len(numeros)):
    n = numeros[i]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Lista completa:", numeros)
print("Pares:", pares)
print("Impares:", impares)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# Ejercicio 4

valores = [1, 2, 2, 3, 4, 4, 5, 5, 5]
sin_repetidos = []

for i in range(len(valores)):
    n = valores[i]
    repetido = False
    for j in range(len(sin_repetidos)):
        if sin_repetidos[j] == n:
            repetido = True
            break
    if repetido == False:
        sin_repetidos.append(n)

print("Lista original:", valores)
print("Lista sin repetidos:", sin_repetidos)

# Ejercicio 5

estudiantes = ["Ana", "Juan", "Sofia", "Pedro", "Lucia", "Martin", "Carla", "Tomas"]

opcion = input("Desea agregar o eliminar un estudiante? (a/e): ")

if opcion == "a":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == "e":
    nombre = input("Ingrese el nombre a eliminar: ")
    pos = -1
    for i in range(len(estudiantes)):
        if estudiantes[i] == nombre:
            pos = i
            break
    if pos != -1:
        estudiantes.pop(pos)
    else:
        print("El estudiante no esta en la lista.")
else:
    print("Opcion no valida.")

print("Lista final:")
for i in range(len(estudiantes)):
    print(estudiantes[i])

# Ejercicio 6

numeros = [10, 20, 30, 40, 50, 60, 70]
ultimo = numeros[len(numeros) - 1]
rotada = [ultimo]

for i in range(len(numeros) - 1):
    rotada.append(numeros[i])

print("Lista original:", numeros)
print("Lista rotada:", rotada)

# Ejercicio 7

temperaturas = [
    [10, 22],
    [11, 24],
    [9, 21],
    [12, 25],
    [8, 20],
    [13, 27],
    [10, 23]
]

suma_min = 0
suma_max = 0
for i in range(len(temperaturas)):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]

prom_min = suma_min // len(temperaturas)
prom_max = suma_max // len(temperaturas)

mayor_amp = temperaturas[0][1] - temperaturas[0][0]
dia_mayor = 1

for i in range(1, len(temperaturas)):
    amp = temperaturas[i][1] - temperaturas[i][0]
    if amp > mayor_amp:
        mayor_amp = amp
        dia_mayor = i + 1

print("Promedio minimas:", prom_min)
print("Promedio maximas:", prom_max)
print("Dia con mayor amplitud:", dia_mayor)

# Ejercicio 8

notas = [
    [7, 8, 9],
    [6, 5, 7],
    [8, 9, 10],
    [5, 6, 5],
    [9, 8, 7]
]

for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    prom = suma / len(notas[i])
    print("Estudiante", i + 1, "promedio:", prom)

materias = len(notas[0])
for j in range(materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    prom = suma / len(notas)
    print("Materia", j + 1, "promedio:", prom)

# Ejercicio 9

tablero = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

def mostrar_tablero():
    for i in range(3):
        print(tablero[i][0], tablero[i][1], tablero[i][2])

jugador = "X"

for turno in range(9):
    mostrar_tablero()
    print("Turno del jugador", jugador)
    f = int(input("Fila (0-2): "))
    c = int(input("Columna (0-2): "))

    if f < 0 or f > 2 or c < 0 or c > 2:
        print("Posicion invalida")
        continue

    if tablero[f][c] == "-":
        tablero[f][c] = jugador
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Casilla ocupada, elija otra")

print("Tablero final:")
mostrar_tablero()

# Ejercicio 10

ventas = [
    [5, 6, 7, 4, 5, 8, 6],
    [3, 4, 2, 5, 6, 4, 3],
    [8, 7, 9, 6, 8, 7, 9],
    [4, 5, 3, 4, 5, 6, 5]
]

for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    print("Producto", i + 1, "total:", total)

# Total por dia
totales_dia = []
for j in range(len(ventas[0])):
    suma = 0
    for i in range(len(ventas)):
        suma += ventas[i][j]
    totales_dia.append(suma)

mayor_dia = totales_dia[0]
dia_max = 1
for j in range(1, len(totales_dia)):
    if totales_dia[j] > mayor_dia:
        mayor_dia = totales_dia[j]
        dia_max = j + 1

print("Dia con mas ventas:", dia_max)

# Producto mas vendido
totales_prod = []
for i in range(len(ventas)):
    suma = 0
    for j in range(len(ventas[i])):
        suma += ventas[i][j]
    totales_prod.append(suma)

mayor_prod = totales_prod[0]
prod_max = 1
for i in range(1, len(totales_prod)):
    if totales_prod[i] > mayor_prod:
        mayor_prod = totales_prod[i]
        prod_max = i + 1

print("Producto mas vendido:", prod_max)





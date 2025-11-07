# Ejercicio 1

for n in range(0, 101):
    print(n)


# Ejercicio 2

num = int(input("Ingrese un numero entero: "))
cont = 0
aux = abs(num)

if num == 0:
    cont = 1
else:
    while aux > 0:
        aux //= 10
        cont += 1

print("El numero tiene", cont, "digitos")

# Ejercicio 3

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a > b:
    a, b = b, a

suma = 0
for i in range(a + 1, b):
    suma += i

print("La suma entre", a, "y", b, "es:", suma)

# Ejercicio 4

suma = 0

while True:
    num = int(input("Ingrese un numero (0 para salir): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)

# Ejercicio 5

import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    n = int(input("Adivine el numero (0 a 9): "))
    intentos += 1
    if n == secreto:
        print(f"Correcto! Lo lograste en {intentos} intentos")
        break

# Ejercicio 6

for i in range(100, -1, -2):
    print(i)

# Ejercicio 7

n = int(input("Ingrese un numero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma del 0 al {n} es: {suma}")

# Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0
cant = 100

for i in range(cant):
    num = int(input("Ingrese el numero " + str(i + 1) + ": "))

    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9

suma = 0
cant = 100  

for i in range(cant):
    num = int(input("Ingrese el numero " + str(i + 1) + ": "))
    suma = suma + num

media = suma / cant
print("La media es:", media)

# Ejercicio 10

num = input("Ingrese un numero: ")

invertido = ""
largo = len(num)

for i in range(largo - 1, -1, -1):
    invertido = invertido + num[i]

print("Numero invertido:", invertido)



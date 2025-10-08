# Ejercicio 1

ed = input("Por favor ingrese su edad:")
edad = int(ed)

if edad > 18 :
    print ("Es mayor de edad")
else:
    print("Es menor de edad")


# Ejercicio 2

nt = input("Ingrese su nota:")
nota= int(nt)

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3

numero = int(input("Por favor ingrese un numero:"))
numeroPar = numero % 2

if numeroPar == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")


# Ejercicio 4

edad = int(input("Por favor, ingrese su edad:"))

if edad < 12:
    print("Niño/a.")
elif 12 <= edad < 18:
    print("Adolescente.")
elif 18 <= edad < 30:
    print("Adulto/a joven.")
elif edad >= 30:
    print("Adulto/a.")


# Ejercicio 5

cont = input("Por favor, ingrese una contaseña:")
if 8 <= len(cont) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"moda: {moda}")
print(f"mediana: {mediana}")
print(f"media: {media}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")


# Ejerciio 7

palabra = input("Ingrese una frase o palabra: ").lower()

ult = palabra[-1]

if ult in "aeiou":
    print(palabra + "!")
else:
    print(palabra)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("\n--Opciones--")
print("1: Si quiere su nombre en mayúsculas")
print("2: Si quiere su nombre en minúsculas")
print("3: Si quiere su nombre con la primera letra mayúscula")
opcion = input("Elija una opcion: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Elija una opcion valida.")

# Ejercicio 9 

magnitud = float(input("Ingrese la magnitud del terremoto: "))


if magnitud < 0:
    print("El valor no puede ser negativo.")
elif magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")


# Ejercicio 10

hemisferio = input("¿En qué hemisferio estás? (N/S): ").lower()
mes = int(input("Mes: "))
dia = int(input("Dia: "))

if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
    periodo = "inviernoN_veranoS"  
elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
    periodo = "primaveraN_otoñoS"    
elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
    periodo = "veranoN_inviernoS"    
else:
    periodo = "otoñoN_primaveraS"     

if hemisferio == "n":
    if periodo == "inviernoN_veranoS":   estacion = "Invierno"
    elif periodo == "primaveraN_otoñoS": estacion = "Primavera"
    elif periodo == "veranoN_inviernoS": estacion = "Verano"
    else:                                estacion = "Otoño"
elif hemisferio == "s":
    if periodo == "inviernoN_veranoS":   estacion = "Verano"
    elif periodo == "primaveraN_otoñoS": estacion = "Otoño"
    elif periodo == "veranoN_inviernoS": estacion = "Invierno"
    else:                                estacion = "Primavera"
else:
    estacion = None

if estacion is None:
    print("Hemisferio invalido. Usa N o S.")
else:
    print(f"Estacion: {estacion}")
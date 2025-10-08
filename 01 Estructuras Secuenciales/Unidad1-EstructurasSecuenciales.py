import math

#EJERCICIO-1
print("Hola mundo!")

#EJERCICIO-2
nombre = input("Por favor ingrese su nombre:")
print(f"Hola {nombre}!")

#EJERCICIO-3 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#EJERCICIO-4 
radio = float(input("Por favor ingrese un radio: "))

area = math.pi * radio **2
perimetro = 2 * math.pi * radio

print(f"El area del circulo de radio {radio} es {area} y su perimetro es {perimetro}")

#EJERCICIO-5 
segundos = float(input("Por favor ingrese una cantidad de segundos:"))

horas = float(segundos / 3600)

print(f"{segundos} segundos equivalen a {horas} horas")

#EJERCICIO-6 
numero = int(input("Por favor ingrese un numero:"))

print(f"""
  {numero} x 0 = {numero * 0}
  {numero} x 1 = {numero * 1}
  {numero} x 2 = {numero * 2}
  {numero} x 3 = {numero * 3}
  {numero} x 4 = {numero * 4}
  {numero} x 5 = {numero * 5}
  {numero} x 6 = {numero * 6}
  {numero} x 7 = {numero * 7}
  {numero} x 8 = {numero * 8}
  {numero} x 9 = {numero * 9}
      """)

#EJERCICIO-7 
numero1 = float(input("Por favor ingrese un numero:"))
numero2 = float(input("Por favor ingrese otro numero:"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2 
division = numero1 / numero2 

print(f"""
  Resultado de la suma: {suma}
  Resultado de la división: {division}
  Resultado de la multiplicación: {multiplicacion}
  Resultado de la resta: {resta}
      """)

#EJERCICIO-8 
peso = float(input("Por favor ingrese su peso en kilos:"))
altura = float(input("Por favor ingrese su altura en metros:"))

IMC = round(peso / altura**2, 2)

print(f"Su indice de masa corporal es: {IMC}")

#EJERCICIO-9 
celsius = float(input("Por favor ingrese una temperatura en grados Celsius:"))

fahrenheit = (9/5) * celsius + 32

print(f"{celsius} grados Celsius corresponden a {fahrenheit} grados Fahrenheit")

#EJERCICIO-10 
numero1 = float(input("Por favor ingrese el primer numero:"))
numero2 = float(input("Por favor ingrese el segundo numero:"))
numero3 = float(input("Por favor ingrese el tercer numero:"))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio es {promedio}")
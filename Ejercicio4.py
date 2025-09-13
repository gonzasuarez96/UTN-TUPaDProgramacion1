import math

radio = float(input("Por favor ingrese un radio: "))

area = math.pi * radio **2
perimetro = 2 * math.pi * radio

print(f"El area del circulo de radio {radio} es {area} y su perimetro es {perimetro}")
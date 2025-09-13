peso = float(input("Por favor ingrese su peso en kilos:"))
altura = float(input("Por favor ingrese su altura en metros:"))

IMC = round(peso / altura**2, 2)

print(f"Su indice de masa corporal es: {IMC}")
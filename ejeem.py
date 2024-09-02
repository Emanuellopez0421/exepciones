try:
    x=10/0
except ZeroDivisionError:
    print("No se puede dividir por cero")


try:
    y=int(input("Introduce un numero: "))
    x=10/0
except ZeroDivisionError:
    print("No se puede dividir por cero")

try:
    x=int(input("Introduce un numero: "))
except ZeroDivisionError:
    print("Debes de introducir un numero valido")
else:
    print(f"El numero es (x) ")



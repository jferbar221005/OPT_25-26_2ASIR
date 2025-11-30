"""
Crea un script que contenga 4 funciones separadas:

sumar(a, b) → devuelve la suma.
restar(a, b) → devuelve la resta.
multiplicar(a, b) → devuelve la multiplicación.
dividir(a, b) → devuelve la división (controlando la división por cero).

El programa principal debe:

Pedir dos números al usuario.
Llamar a cada función y mostrar los resultados.
Incluir un docstring explicativo en cada función.
Cumplir las normas de estilo PEP 8.
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

option=""

while option !="5":
    option=input("Elige la operacion: 1-Sumar 2-Restar 3-Multiplicar 4-Dividir 5-Salir:  ")

    if option == "1":
        a=int(input("Introduce el numero 1: "))
        b=int(input("Introduce el numero 2: "))
        print(sumar(a, b))

    elif option == "2":
        a=int(input("Introduce el numero 1: "))
        b=int(input("Introduce el numero 2: "))
        print(restar(a, b))

    elif option == "3":
        a=int(input("Introduce el numero 1: "))
        b=int(input("Introduce el numero 2: "))
        print(multiplicar(a, b))

    elif option == "4":
        a=int(input("Introduce el numero 1: "))
        b=int(input("Introduce el numero 2: "))
        print(dividir(a, b))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operacion = input("Elige operación (suma, resta, multiplicacion, division): ").lower()

match operacion:
    case "suma":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    case "resta":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    case "multiplicacion":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    case "division":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Error: División por cero no permitida.")
    case _:
        print("Operación no reconocida")

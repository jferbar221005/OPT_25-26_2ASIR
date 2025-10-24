"""
Programa que muestra la tabla de multiplicar de un número introducido por el usuario.

El programa pide un número y muestra los resultados desde 1 hasta 10
usando un bucle for.
Este ejercicio aplica buenas prácticas de estilo (PEP 8),
así como el uso de docstrings y comentarios claros.
"""

# Solicita al usuario un número entero
numero_base = int(input("Introduce un número entero: "))

# Recorre los números del 1 al 10 para generar la tabla
for factor in range(1, 11):
    # Calcula el producto de la iteración actual
    resultado = numero_base * factor
    # Muestra el resultado formateado
    print(f"{numero_base} x {factor} = {resultado}")

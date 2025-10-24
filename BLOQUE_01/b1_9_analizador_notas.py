"""
Programa que solicitaba tres notas al usuario y calculaba el promedio,
pero tenía un error lógico: sumaba las notas sin convertirlas a número,
por lo que el promedio era incorrecto.
Se corrigió convirtiendo explícitamente las entradas a float antes de la suma.
"""

# Pedir tres notas y convertirlas a float para evitar concatenación de strings
nota_1 = float(input("Introduce la primera nota: "))
nota_2 = float(input("Introduce la segunda nota: "))
nota_3 = float(input("Introduce la tercera nota: "))

# Calcular el promedio sumando las notas correctamente (ya en float)
promedio = (nota_1 + nota_2 + nota_3) / 3

print(f"El promedio de las notas es: {promedio}")

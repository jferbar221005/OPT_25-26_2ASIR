"""
Programa que recorre una lista de nombres y muestra solo aquellos
que no comiencen por la letra 'A' (mayúscula o minúscula).
Utiliza un bucle for y la instrucción 'continue' para saltar las coincidencias.
"""

# Lista de nombres de ejemplo
nombres = ["Ana", "Pedro", "Alba", "Lucía", "Andrés", "Miguel"]

# Recorremos la lista con un bucle for
for nombre in nombres:
    # Si el nombre empieza con A o a, se salta la iteración
    if nombre.startswith("A") or nombre.startswith("a"):
        continue
    # Si no empieza por A/a, se muestra en pantalla
    print(nombre)

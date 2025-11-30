"""
Genere una lista de 20 números enteros (pueden ser introducidos manualmente o generados con range).

Obtenga mediante comprensiones de listas:

Una lista con los cuadrados de todos los números.
Una lista con solo los números pares.
Una lista con los números mayores que 10.
Cree un diccionario que relacione cada número con su doble.

Muestre en pantalla todos los resultados.

Incluya un docstring explicando qué hace el programa.

"""

#Generar lista de 20 números (del 1 al 20)
numeros_generados = list(range(1, 21))
print(f"Originales: {numeros_generados}")

#Lista de Numeros cuadrados
cuadrados_numeros = []
for n in numeros_generados:
    cuadrados_numeros.append(n ** 2)
print(f"Cuadrados:  {cuadrados_numeros}")

#Lista de Numneros pares
numeros_pares = []
for n in numeros_generados:
    if n % 2 == 0:
        numeros_pares.append(n)
print(f"Pares:      {numeros_pares}")

#Lista de numeros mayores que 10
numeros_mayores = []
for n in numeros_generados:
    if n > 10:
        numeros_mayores.append(n)
print(f"Mayores >10: {numeros_mayores}")

#Diccionario de dobles
diccionario_dobles = {}
for n in numeros_generados:
    diccionario_dobles[n] = n * 2
print(f"Dobles:     {diccionario_dobles}")
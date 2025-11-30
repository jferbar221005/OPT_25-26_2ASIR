"""
Tenemos un diccionario con estudiantes y sus notas en tres materias:
estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}
Crea un iterador sobre las claves del diccionario.

Recorre el iterador usando next() dentro de un while True.

Para cada estudiante:

Calcula el promedio de sus notas.

Determina el estado:

"Aprobado" si promedio ≥ 6.5
"En recuperación" si promedio ≥ 5 y < 6.5
"Reprobado" si promedio < 5
Imprime un reporte claro y ordenado:

Ana - Notas: [8, 7, 9], Promedio: 8.0, Estado: Aprobado
Luis - Notas: [7, 6, 8], Promedio: 7.0, Estado: Aprobado
Marta - Notas: [9, 10, 9], Promedio: 9.33, Estado: Aprobado
Carlos - Notas: [6, 7, 5], Promedio: 6.0, Estado: En recuperación
Laura - Notas: [10, 9, 10], Promedio: 9.67, Estado: Aprobado
"""

estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

#Creamos el iterador sobre las claves del diccionario
iterador_estudiantes = iter(estudiantes)

print("--- REPORTE DE NOTAS ---\n")

#Bucle infinito controlado manualmente
while True:
    try:
#Intentamos obtener el siguiente nombre
        nombre = next(iterador_estudiantes)

#Obtenemos las notas usando la clave (nombre)
        notas = estudiantes[nombre]

#Calculamos el promedio
        promedio = sum(notas) / len(notas)

#Lógica del estado
        if promedio >= 6.5:
            estado = "Aprobado"
        elif 5 <= promedio < 6.5:
            estado = "En recuperación"
        else:
            estado = "Reprobado"

#Imprimimos (:.2f redondea a 2 decimales si es necesario)
        print(f"{nombre} - Notas: {notas}, Promedio: {promedio:.2f}, Estado: {estado}")

    except StopIteration:
#Cuando next no encuentra más elementos, lanza este error.
#Aquí capturamos el error para romper el bucle limpiamente.
        break
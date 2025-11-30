"""
Se tienen tres listas:
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
Recorre las listas simultáneamente usando enumerate() y zip().

El índice debe empezar en 1.
Para cada estudiante, calcula:

Promedio de sus notas.

Calificación final según el promedio:

"Aprobado" si promedio ≥ 6.5
"En recuperación" si promedio ≥ 5 y < 6.5
"Reprobado" si promedio < 5
Muestra un reporte en pantalla con el índice, nombre del estudiante, notas, promedio y calificación final.

Ejemplo de salida esperada
1 Ana - Matemáticas: 8, Física: 9, Química: 7, Promedio: 8.0, Estado: Aprobado
2 Luis - Matemáticas: 7, Física: 6, Química: 8, Promedio: 7.0, Estado: Aprobado
3 Marta - Matemáticas: 9, Física: 10, Química: 9, Promedio: 9.33, Estado: Aprobado
4 Carlos - Matemáticas: 6, Física: 7, Química: 5, Promedio: 6.0, Estado: En recuperación
Puntos clave para resolver la actividad
Usar zip(notas_matematicas, notas_fisica, notas_quimica) para combinar las notas.
Usar enumerate(..., start=1) para tener el índice visible en el reporte.
Calcular promedio usando (matematicas + fisica + quimica)/3.
Determinar el estado usando if...elif...else.
Mostrar toda la información de manera legible, con índice al inicio.
"""

#Definición de las listas
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

print("--- REPORTE DE NOTAS ---\n")

#Bucle principal usando enumerate y zip
for i, (nombre, mat, fis, quim) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):

#Calcular el promedio
    promedio = (mat + fis + quim) / 3

#Lógica de estado (if - elif - else)
    if promedio >= 6.5:
        estado = "Aprobado"
    elif 5 <= promedio < 6.5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

#Imprimir el resultado formateado
    print(f"{i} {nombre} - Matemáticas: {mat}, Física: {fis}, Química: {quim}, "
          f"Promedio: {promedio:.2f}, Estado: {estado}")
"""
Se tienen cuatro listas:
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
Crear un diccionario vacío llamado resultado_final.

Usar zip() para recorrer todas las listas al mismo tiempo y calcular:

Promedio de cada estudiante.

Estado final:

"Aprobado" si promedio ≥ 6.5
"En recuperación" si promedio ≥ 5 y < 6.5
"Reprobado" si promedio < 5
Guardar en el diccionario resultado_final de esta forma:

# Clave: nombre del estudiante
# Valor: diccionario con notas, promedio y estado
Por ejemplo:

{
  "Ana": {"Matemáticas": 8, "Física": 9, "Química": 7, "Promedio": 8.0, "Estado": "Aprobado"},
  "Luis": {...},
  ...
}
Imprimir un reporte ordenado usando for y zip():
Ana - Matemáticas: 8, Física: 9, Química: 7, Promedio: 8.0, Estado: Aprobado
Luis - Matemáticas: 7, Física: 6, Química: 8, Promedio: 7.0, Estado: Aprobado
Marta - Matemáticas: 9, Física: 10, Química: 9, Promedio: 9.33, Estado: Aprobado
Carlos - Matemáticas: 6, Física: 7, Química: 5, Promedio: 6.0, Estado: En recuperación
Puntos clave para resolver la actividad
Usar zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica) para recorrer todas las listas al mismo tiempo.
Calcular el promedio sumando las notas y dividiendo entre la cantidad de materias.
Determinar el estado usando if...elif...else.
Guardar toda la información en un diccionario anidado.
Mostrar el reporte final usando otro for para iterar sobre resultado_final.items().

"""

#Definimos las listas con los datos
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

#Creamos el diccionario vacío donde guardaremos los datos
resultado_final = {}

#Procesamos los datos usando zip()
for nombre, mat, fis, quim in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

#Calcular el promedio
    promedio = (mat + fis + quim) / 3

#Determinar el estado según las reglas
    if promedio >= 6.5:
        estado = "Aprobado"
    elif 5 <= promedio < 6.5:
        estado = "En recuperación"
    else:
        estado = "Suspenso"

#Guardamos en el diccionario anidado
    resultado_final[nombre] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": quim,
        "Promedio": round(promedio, 2), #Redondeamos a 2 decimales
        "Estado": estado
    }

#Imprimir el reporte final iterando sobre el diccionario creado
print("--- BOLETIN DE CALIFICACIONES ---\n")

for nombre, datos in resultado_final.items():
#Accedemos a los datos internos usando las claves del sub-diccionario

    print(f"{nombre} - Matemáticas: {datos['Matemáticas']}, "
          f"Física: {datos['Física']}, "
          f"Química: {datos['Química']}, "
          f"Promedio: {datos['Promedio']}, "
          f"Estado: {datos['Estado']}")
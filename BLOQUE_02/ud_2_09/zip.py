"""
Crea tres listas:

nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

Usa zip() para imprimir:

Ana - Matemáticas: 8, Física: 9
Luis - Matemáticas: 7, Física: 6
Marta - Matemáticas: 9, Física: 10
"""

nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]
#Listas con datos

#Para mostrar en pantalla ordenadamente las notas de los estudiantes usamos un bucle "for"
for nom, mat, fis in zip(nombres, notas_matematicas, notas_fisica):
#Mostramos los estudiantes con sus notas correspondientes
    print(f"{nom} - Matematicas: {mat}, Física: {fis}")
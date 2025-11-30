"""
Crea una tupla llamada persona con los siguientes datos: nombre, edad, ciudad.

Desempaqueta la tupla en tres variables (nombre, edad, ciudad).

Muestra en pantalla un mensaje con la información.

Añade un docstring al inicio del programa explicando qué hace.
"""

persona = ("Jose", 20, "San Juan")
#Tupla con datos de la persona

nombre, edad, ciudad = persona
#Variables con posiciones

print(f"Hola, soy {nombre} tengo {edad} años y vivo en {ciudad}")
#Mostramos en pantalla los datos
"""
Lista de nombres:

nombres = ["Ana", "Luis", "Marta", "Carlos"]

Recorre la lista usando enumerate() y muestra el índice y el nombre.

Convierte el resultado en lista de tuplas y muéstralo.
"""

nombres = ["Ana", "Luis", "Marta", "Carlos"]
#Lista con los nombres

#Definimos un bucle con los parametros indice y nom
for indice, nom in enumerate(nombres):
    print(indice, nom)

lista_converted = list(enumerate(nombres))
print(lista_converted)
#Mostramos por pantalla la lista numerada
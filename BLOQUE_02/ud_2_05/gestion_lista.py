"""
Defina una lista vacía compras.

Pida al usuario 5 productos y los añada a la lista con append().

Muestre la lista completa.

Pida al usuario un producto a eliminar y lo quite con remove().

Muestre la lista ordenada alfabéticamente con sort().

Incluya un docstring explicando qué hace el programa.
"""

compras = []

print("Lista de la compra: \n")
lista_compra = input("Introduce lo que necesites comprar: ")
#Pedimos por teclado la lista de productos con la variable "lista_compra"

compras.extend(lista_compra.split())
print(compras)
#Separamos el texto introducido por teclado y lo mostramoos por pantalla

producto_eliminado = input("Elimina algun producto: ")
compras.remove(producto_eliminado)
#Pedimos eliminar un producto de los añadidos

compras.sort()

print(compras)
#Mostramos la lista final
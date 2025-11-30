"""
Defina una variable global contador = 0.

Implemente tres funciones:

incrementar() → suma 1 al contador.
decrementar() → resta 1 al contador.
mostrar_contador() → imprime el valor actual.
Use la palabra clave global para modificar el contador dentro de las funciones.

Desde el programa principal, llama a las funciones en este orden:

incrementar() dos veces.
decrementar() una vez.
mostrar_contador().

Añade un docstring en cada función explicando lo que hace.
"""

contador = 0

def incrementar():
    """Añade al contador 1"""
    global contador
    contador += 1

def decrementar():
    """Resta al contador 1"""
    global contador
    contador -= 1

def mostrar_contador():
    """Muestra el contador con el valor actual"""
    print(contador)


incrementar()
incrementar()
decrementar()
mostrar_contador()
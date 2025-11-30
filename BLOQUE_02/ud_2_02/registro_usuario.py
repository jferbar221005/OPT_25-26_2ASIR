"""
Crea una función registrar_usuario(nombre, edad, ciudad="Madrid").

La función debe mostrar en pantalla: "Usuario: [nombre], Edad: [edad], Ciudad: [ciudad]".

Debe poder llamarse con:

Todos los argumentos posicionales.

Algún argumento omitido, usando el valor por defecto.

Argumentos nombrados en distinto orden.

Incluye un docstring en la función.

Desde el programa principal, llama a la función al menos 3 veces con diferentes combinaciones de argumentos.
"""

def registrar_usuario(nombre, edad, ciudad='Madrid'):
    """Muestra la info de el nombre, edad y ciudad del usuario"""
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

registrar_usuario("Roddy", 23, "Huelva")
print("-" * 50) #Esto me lo ha dicho Roddy pa que quede mas bonito
registrar_usuario(nombre="Adrian", edad="19")
print("-" * 50)
registrar_usuario("Jose", 20)
"""
Crea un diccionario vacío llamado agenda.

Pide al usuario que introduzca 3 contactos (nombre y teléfono).

El nombre será la clave.
El teléfono será el valor.
Muestra la agenda completa usando un bucle.

Permite al usuario buscar un contacto por nombre:

Si existe, muestra el teléfono.
Si no existe, muestra "Contacto no encontrado".
Añade un docstring explicando qué hace el programa.
"""

agenda = {}

print("--- Vamos a crear tu agenda (3 contactos) ---\n")

# Usamos un bucle 'for' porque sabemos exactamente cuántas veces queremos repetir (3)
for i in range(3):
    print(f"Contacto número {i + 1}:")
    nombre = input("   Nombre: ")
    telefono = input("   Teléfono: ")

# Guardamos en el diccionario: Clave = nombre, Valor = telefono
    agenda[nombre] = telefono
    print("¡Guardado!\n")

# Mostramos la agenda completa
print("--- Agenda guardada ---")
for nombre, telefono in agenda.items():
    print(f"- {nombre}: {telefono}")

# Buscar un contacto
print("\n--- Búsqueda ---")
buscar = input("¿A quién quieres buscar?: ")

# Intenta buscar el nombre, y si no existe, devuelve el mensaje:
resultado = agenda.get(buscar, "Ese contacto no existe.")

print(f"Numero de Tlfno: {resultado}")
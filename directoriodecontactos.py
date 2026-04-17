"""
Directorio de Contactos - Programa para gestionar un directorio de contactos
Usa diccionarios anidados para almacenar información de contactos
"""

# Diccionario principal para almacenar contactos
directorio = {}


def crear_contacto():
    """
    Solicita nombre, email, teléfono y ciudad.
    Crea la entrada en el diccionario principal con esos datos
    """
    print("\n" + "="*60)
    print("CREAR NUEVO CONTACTO")
    print("="*60)
    
    nombre = input("Nombre del contacto: ").strip()
    
    # Verificar si el contacto ya existe
    if nombre in directorio:
        print(f"\n✗ El contacto '{nombre}' ya existe en el directorio.")
        return
    
    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()
    ciudad = input("Ciudad: ").strip()
    
    # Crear el diccionario anidado para el contacto
    directorio[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad
    }
    
    print(f"\n✓ El contacto '{nombre}' ha sido creado correctamente.")


def ver_contactos():
    """
    Itera con .items() e imprime cada contacto con todos sus campos de forma legible
    """
    if not directorio:
        print("\n✗ El directorio está vacío. No hay contactos que mostrar.")
        return
    
    print("\n" + "="*60)
    print("LISTA DE CONTACTOS")
    print("="*60)
    
    for nombre, datos in directorio.items():
        print(f"\n📇 Contacto: {nombre}")
        for campo, valor in datos.items():
            campo_formateado = campo.capitalize()
            print(f"   {campo_formateado}: {valor}")
        print("-" * 60)


def buscar_contacto():
    """
    Pide un nombre y muestra los datos del contacto.
    Usa .get() para evitar errores si no existe
    """
    print("\n" + "="*60)
    print("BUSCAR CONTACTO")
    print("="*60)
    
    nombre = input("Nombre del contacto a buscar: ").strip()
    
    # Usar .get() para acceder de forma segura
    contacto = directorio.get(nombre)
    
    if contacto:
        print(f"\n✓ Contacto encontrado: {nombre}")
        print("-" * 60)
        for campo, valor in contacto.items():
            campo_formateado = campo.capitalize()
            print(f"   {campo_formateado}: {valor}")
        print("-" * 60)
    else:
        print(f"\n✗ El contacto '{nombre}' no existe en el directorio.")


def actualizar_telefono():
    """
    Pide el nombre del contacto y el nuevo teléfono.
    Accede al diccionario anidado y actualiza el campo "teléfono"
    """
    print("\n" + "="*60)
    print("ACTUALIZAR TELÉFONO")
    print("="*60)
    
    nombre = input("Nombre del contacto: ").strip()
    
    # Usar .get() para verificar si existe
    if nombre in directorio:
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        directorio[nombre]["teléfono"] = nuevo_telefono
        print(f"\n✓ El teléfono de '{nombre}' ha sido actualizado a: {nuevo_telefono}")
    else:
        print(f"\n✗ El contacto '{nombre}' no existe en el directorio.")


def eliminar_contacto():
    """
    Pide el nombre y usa .pop() para eliminar la entrada completa del directorio
    """
    print("\n" + "="*60)
    print("ELIMINAR CONTACTO")
    print("="*60)
    
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    # Usar .pop() para eliminar de forma segura
    contacto_eliminado = directorio.pop(nombre, None)
    
    if contacto_eliminado:
        print(f"\n✓ El contacto '{nombre}' ha sido eliminado correctamente del directorio.")
    else:
        print(f"\n✗ El contacto '{nombre}' no existe en el directorio.")


def menu_principal():
    """
    Menú principal del programa de directorio de contactos
    """
    while True:
        print("\n" + "="*60)
        print("DIRECTORIO DE CONTACTOS")
        print("="*60)
        print("1. Crear nuevo contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar contacto")
        print("4. Actualizar teléfono de contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        print("="*60)
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            crear_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            actualizar_telefono()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n✗ Opción no válida. Por favor, selecciona 1, 2, 3, 4, 5 o 6.")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()

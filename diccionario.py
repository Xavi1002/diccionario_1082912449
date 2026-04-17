"""
Gestor de Compras - Programa que gestiona una lista de artículos de compra
"""

# Lista de artículos de compra - cada artículo es un diccionario
articulos = [
    {"nombre": "Leche", "precio": 1.50, "cantidad": 2},
    {"nombre": "Pan", "precio": 2.00, "cantidad": 1},
    {"nombre": "Huevos", "precio": 3.50, "cantidad": 1},
    {"nombre": "Queso", "precio": 5.00, "cantidad": 2},
    {"nombre": "Manzanas", "precio": 0.75, "cantidad": 6}
]


def mostrar_articulos():
    """
    Itera sobre la lista e imprime cada artículo con su precio y cantidad
    usando un bucle for y .items()
    """
    print("\n" + "="*60)
    print("LISTA DE ARTÍCULOS DE COMPRA")
    print("="*60)
    
    for articulo in articulos:
        print("\nArtículo:")
        for clave, valor in articulo.items():
            if clave == "precio":
                print(f"  {clave.capitalize()}: ${valor:.2f}")
            elif clave == "cantidad":
                print(f"  {clave.capitalize()}: {valor} unidades")
            else:
                print(f"  {clave.capitalize()}: {valor}")


def calcular_total():
    """
    Recorre la lista y acumula precio × cantidad para cada artículo
    Muestra el total al final
    """
    total = 0
    
    print("\n" + "="*60)
    print("DESGLOSE DE GASTOS")
    print("="*60)
    
    for articulo in articulos:
        subtotal = articulo["precio"] * articulo["cantidad"]
        total += subtotal
        print(f"{articulo['nombre']}: ${articulo['precio']:.2f} × {articulo['cantidad']} = ${subtotal:.2f}")
    
    print("-" * 60)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("="*60)
    
    return total


def eliminar_articulo():
    """
    Pide el nombre del producto a eliminar.
    Busca el diccionario correspondiente en la lista y usa remove() para borrarlo
    """
    nombre_eliminar = input("\n¿Cuál es el nombre del producto a eliminar? ").strip()
    
    # Buscar el artículo en la lista
    articulo_encontrado = None
    for articulo in articulos:
        if articulo["nombre"].lower() == nombre_eliminar.lower():
            articulo_encontrado = articulo
            break
    
    # Si se encontró, eliminarlo
    if articulo_encontrado:
        articulos.remove(articulo_encontrado)
        print(f"\n✓ El producto '{nombre_eliminar}' ha sido eliminado correctamente.")
    else:
        print(f"\n✗ El producto '{nombre_eliminar}' no se encontró en la lista.")


def menu_principal():
    """
    Menú principal del programa
    """
    while True:
        print("\n" + "="*60)
        print("GESTOR DE COMPRAS")
        print("="*60)
        print("1. Ver lista de artículos")
        print("2. Calcular total de compra")
        print("3. Eliminar un artículo")
        print("4. Salir")
        print("="*60)
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            mostrar_articulos()
        elif opcion == "2":
            calcular_total()
        elif opcion == "3":
            eliminar_articulo()
        elif opcion == "4":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n✗ Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()

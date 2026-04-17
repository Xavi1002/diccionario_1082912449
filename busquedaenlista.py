"""
Búsqueda en Lista - Programa que implementa funciones de búsqueda y manipulación de listas
Incluye: buscar índice, calcular promedio, filtrar números, ordenar lista
"""

# Lista de números para trabajar
numeros = [45, 23, 67, 12, 89, 34, 56, 78, 11, 90, 55]


def buscar_indice(numero):
    """
    Devuelve el índice del número en la lista, o -1 si no existe
    Usa .index() o un bucle con comprobación
    """
    try:
        # Intentar usar .index()
        indice = numeros.index(numero)
        return indice
    except ValueError:
        # Si no existe, devolver -1
        return -1


def calcular_promedio():
    """
    Calcula y devuelve el promedio de todos los elementos.
    Usa sum() y len() para simplificar el cálculo
    """
    if len(numeros) == 0:
        return 0
    
    promedio = sum(numeros) / len(numeros)
    return promedio


def filtrar_por_umbral(umbral):
    """
    Devuelve una nueva lista con todos los números mayores que el umbral indicado.
    Usa comprensión de listas
    """
    # Opción 1: Usar comprensión de listas (más Pythonica)
    lista_filtrada = [num for num in numeros if num > umbral]
    return lista_filtrada


def ordenar_lista():
    """
    Ordena los números de menor a mayor y devuelve la lista ordenada.
    Usa sorted() para no modificar la lista original
    """
    # Usar sorted() para devolver una nueva lista ordenada
    lista_ordenada = sorted(numeros)
    return lista_ordenada


def mostrar_menu():
    """
    Menú principal del programa de búsqueda en lista
    """
    while True:
        print("\n" + "="*60)
        print("BÚSQUEDA Y MANIPULACIÓN DE LISTAS")
        print("="*60)
        print(f"Lista actual: {numeros}")
        print("="*60)
        print("1. Buscar índice de un número")
        print("2. Calcular promedio de la lista")
        print("3. Filtrar números mayores que un umbral")
        print("4. Ordenar lista de menor a mayor")
        print("5. Agregar número a la lista")
        print("6. Ver lista actual")
        print("7. Salir")
        print("="*60)
        
        opcion = input("Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            buscar_numero()
        elif opcion == "2":
            calcular_y_mostrar_promedio()
        elif opcion == "3":
            filtrar_y_mostrar()
        elif opcion == "4":
            mostrar_lista_ordenada()
        elif opcion == "5":
            agregar_numero()
        elif opcion == "6":
            mostrar_lista_actual()
        elif opcion == "7":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n✗ Opción no válida. Por favor, selecciona 1, 2, 3, 4, 5, 6 o 7.")


def buscar_numero():
    """
    Interfaz para buscar un número en la lista
    """
    print("\n" + "="*60)
    print("BUSCAR ÍNDICE DE UN NÚMERO")
    print("="*60)
    
    try:
        numero = int(input("Ingresa el número a buscar: ").strip())
        indice = buscar_indice(numero)
        
        if indice != -1:
            print(f"\n✓ El número {numero} se encuentra en el índice: {indice}")
        else:
            print(f"\n✗ El número {numero} no existe en la lista.")
    except ValueError:
        print("\n✗ Por favor, ingresa un número válido.")


def calcular_y_mostrar_promedio():
    """
    Calcula y muestra el promedio de la lista
    """
    print("\n" + "="*60)
    print("CALCULAR PROMEDIO")
    print("="*60)
    
    promedio = calcular_promedio()
    print(f"\nLista: {numeros}")
    print(f"Suma total: {sum(numeros)}")
    print(f"Cantidad de elementos: {len(numeros)}")
    print(f"Promedio: {promedio:.2f}")


def filtrar_y_mostrar():
    """
    Interfaz para filtrar números mayores que un umbral
    """
    print("\n" + "="*60)
    print("FILTRAR POR UMBRAL")
    print("="*60)
    
    try:
        umbral = int(input("Ingresa el umbral (números mayores a este): ").strip())
        lista_filtrada = filtrar_por_umbral(umbral)
        
        print(f"\nLista original: {numeros}")
        print(f"Números mayores que {umbral}: {lista_filtrada}")
        print(f"Cantidad de números filtrados: {len(lista_filtrada)}")
    except ValueError:
        print("\n✗ Por favor, ingresa un número válido.")


def mostrar_lista_ordenada():
    """
    Muestra la lista ordenada de menor a mayor
    """
    print("\n" + "="*60)
    print("ORDENAR LISTA")
    print("="*60)
    
    lista_ordenada = ordenar_lista()
    
    print(f"\nLista original: {numeros}")
    print(f"Lista ordenada: {lista_ordenada}")


def agregar_numero():
    """
    Permite agregar un nuevo número a la lista
    """
    print("\n" + "="*60)
    print("AGREGAR NÚMERO")
    print("="*60)
    
    try:
        numero = int(input("Ingresa el número a agregar: ").strip())
        numeros.append(numero)
        print(f"\n✓ El número {numero} ha sido agregado correctamente.")
        print(f"Lista actualizada: {numeros}")
    except ValueError:
        print("\n✗ Por favor, ingresa un número válido.")


def mostrar_lista_actual():
    """
    Muestra la lista actual con información adicional
    """
    print("\n" + "="*60)
    print("LISTA ACTUAL")
    print("="*60)
    
    print(f"\nElementos: {numeros}")
    print(f"Cantidad: {len(numeros)}")
    print(f"Mínimo: {min(numeros)}")
    print(f"Máximo: {max(numeros)}")
    print(f"Suma: {sum(numeros)}")
    print(f"Promedio: {calcular_promedio():.2f}")


# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()

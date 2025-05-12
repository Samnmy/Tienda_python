# Inventario de productos
inventario = []

# Funciones de validación de entrada
def input_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número entero.")

def input_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número decimal.")

def input_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("❌ El texto no puede estar vacío.")

# Función para mostrar productos
def mostrar_productos():
    if not inventario:
        print("📦 El inventario está vacío.")
    else:
        print("\n📋 Inventario:")
        for producto in inventario:
            print(f"🔹 ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")

# Función para agregar producto
def agregar_producto():
    while True:
        nuevo_id = input_entero("🔢 ID del producto: ")
        if any(p['id'] == nuevo_id for p in inventario):
            print("❌ Ese ID ya existe. Intenta con otro.")
        else:
            break
    nombre = input_texto("📝 Nombre del producto: ")
    precio = input_flotante("💵 Precio del producto: ")
    cantidad = input_entero("📦 Cantidad del producto: ")

    inventario.append({
        'id': nuevo_id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print("✅ Producto agregado exitosamente.")

# Función para eliminar producto
def eliminar_producto():
    if not inventario:
        print("❌ No hay productos que eliminar.")
        return
    id_eliminar = input_entero("🗑️ Ingresa el ID del producto a eliminar: ")
    for i, producto in enumerate(inventario):
        if producto['id'] == id_eliminar:
            inventario.pop(i)
            print("✅ Producto eliminado.")
            return
    print("❌ No se encontró un producto con ese ID.")

# Función para buscar producto
def buscar_producto():
    nombre_buscar = input_texto("🔍 Ingresa el nombre del producto a buscar: ").lower()
    encontrados = [p for p in inventario if nombre_buscar in p['nombre'].lower()]
    if encontrados:
        print("📦 Productos encontrados:")
        for p in encontrados:
            print(f"🔹 ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")
    else:
        print("❌ No se encontraron productos con ese nombre.")

# Función para actualizar producto
def actualizar_producto():
    id_actualizar = input_entero("✏️ Ingresa el ID del producto a actualizar: ")
    for producto in inventario:
        if producto['id'] == id_actualizar:
            nuevo_precio = input_flotante("💲 Nuevo precio: ")
            nueva_cantidad = input_entero("📦 Nueva cantidad: ")
            producto.update({"precio": nuevo_precio, "cantidad": nueva_cantidad})
            print("✅ Producto actualizado.")
            return
    print("❌ Producto no encontrado.")

# Mostrar productos con bajo stock
def productos_bajo_stock():
    limite = input_entero("⚠️ Mostrar productos con stock menor a: ")
    bajos = [p for p in inventario if p['cantidad'] < limite]
    if bajos:
        print("📉 Productos con bajo stock:")
        for p in bajos:
            print(f"🔹 ID: {p['id']} | Nombre: {p['nombre']} | Cantidad: {p['cantidad']}")
    else:
        print("✅ Todos los productos tienen suficiente stock.")

# Menú principal
def menu():
    while True:
        print("\n🔧 MENÚ PRINCIPAL")
        print("1️⃣ Mostrar todos los productos")
        print("2️⃣ Agregar nuevo producto")
        print("3️⃣ Eliminar producto")
        print("4️⃣ Buscar producto por nombre")
        print("5️⃣ Actualizar producto")
        print("6️⃣ Mostrar productos con bajo stock")
        print("7️⃣ Salir")
        
        opcion = input("📍 Elige una opción (1-7): ").strip()

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            productos_bajo_stock()
        elif opcion == "7":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Elige un número del 1 al 7.")

# Ejecutar el menú
menu()

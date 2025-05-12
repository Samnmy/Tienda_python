# Sistema de Gestión de Inventario de Productos

Este proyecto proporciona un sistema para gestionar un inventario de productos. Permite agregar, eliminar, actualizar, buscar productos, así como mostrar productos con bajo stock. Es útil para pequeñas empresas, tiendas o cualquier negocio que necesite controlar su inventario de productos.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades principales:

1. **Mostrar todos los productos**: Muestra la lista completa de productos en el inventario con su ID, nombre, precio y cantidad disponible.

2. **Agregar un nuevo producto**: Permite agregar un nuevo producto al inventario, validando que el ID del producto sea único.

3. **Eliminar un producto**: Permite eliminar un producto del inventario a través de su ID.

4. **Buscar producto por nombre**: Permite buscar productos por nombre, mostrando los que coinciden con el término de búsqueda.

5. **Actualizar un producto**: Permite actualizar el precio y la cantidad de un producto existente.

6. **Mostrar productos con bajo stock**: Permite mostrar los productos cuya cantidad está por debajo de un límite definido por el usuario.

7. **Menú interactivo**: Ofrece un menú de opciones en la consola para interactuar con el sistema de inventario.

## Estructura de Datos

El inventario se representa como una lista de diccionarios, donde cada diccionario contiene los detalles de un producto. Los atributos de cada producto son:

- **id**: ID único del producto.
- **nombre**: Nombre del producto.
- **precio**: Precio del producto.
- **cantidad**: Cantidad disponible en inventario.

## Funciones Principales

- **input_entero(mensaje)**: Solicita un número entero al usuario. Si el valor ingresado no es válido, muestra un mensaje de error y solicita la entrada nuevamente.
- **input_flotante(mensaje)**: Solicita un número decimal al usuario. Si el valor ingresado no es válido, muestra un mensaje de error y solicita la entrada nuevamente.
- **input_texto(mensaje)**: Solicita una cadena de texto al usuario. Si el valor ingresado está vacío, muestra un mensaje de error y solicita la entrada nuevamente.
- **mostrar_productos()**: Muestra todos los productos en el inventario con su ID, nombre, precio y cantidad.
- **agregar_producto()**: Permite agregar un nuevo producto al inventario con validación de ID único.
- **eliminar_producto()**: Permite eliminar un producto del inventario a través de su ID.
- **buscar_producto()**: Permite buscar productos por nombre y mostrar los productos encontrados.
- **actualizar_producto()**: Permite actualizar el precio y la cantidad de un producto existente.
- **productos_bajo_stock()**: Muestra los productos cuyo stock está por debajo de un límite especificado por el usuario.
- **menu()**: Muestra el menú principal interactivo y permite al usuario elegir qué operación realizar.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `inventario_productos.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo donde podrás seleccionar qué operación realizar sobre el inventario.

### Ejemplo de flujo

1. **Mostrar productos**:
   - El sistema muestra todos los productos en el inventario con su ID, nombre, precio y cantidad.

2. **Agregar un producto**:
   - El sistema solicita al usuario los detalles del producto (ID, nombre, precio y cantidad) y agrega el producto al inventario.

3. **Eliminar un producto**:
   - El sistema solicita el ID de un producto para eliminarlo del inventario.

4. **Buscar producto**:
   - El sistema solicita un nombre de producto y muestra los productos que coincidan con el término de búsqueda.

5. **Actualizar producto**:
   - El sistema solicita el ID de un producto y permite actualizar su precio y cantidad.

6. **Mostrar productos con bajo stock**:
   - El sistema muestra los productos cuyo stock es menor que el valor especificado por el usuario.

## Contribuciones

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.

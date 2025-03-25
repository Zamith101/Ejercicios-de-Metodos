class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = precio  # Atributo privado
    
    # Método para cambiar el precio del producto
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El nuevo precio debe ser mayor que cero.")
        self.__precio = nuevo_precio
    
    # Método para consultar el precio actual
    def obtener_precio(self):
        return self.__precio
    
    # Método para obtener el nombre del producto
    def obtener_nombre(self):
        return self.__nombre
    
    # Método para aplicar un descuento al precio
    def aplicar_descuento(self, porcentaje_descuento):
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        descuento = (self.__precio * porcentaje_descuento) / 100
        self.__precio -= descuento
    
# Ejemplo
try:
    # Crear un producto con nombre y precio
    producto = Producto("Camiseta", 25)
    
    # Consultar el nombre y el precio
    print(f"Producto: {producto.obtener_nombre()}")
    print(f"Precio inicial: ${producto.obtener_precio():.2f}")
    
    # Cambiar el precio del producto
    producto.cambiar_precio(30)
    print(f"Nuevo precio: ${producto.obtener_precio():.2f}")
    
    # Aplicar un descuento del 20%
    producto.aplicar_descuento(20)
    print(f"Precio después del descuento: ${producto.obtener_precio():.2f}")
    
    # Intentar cambiar el precio a un valor no válido (negativo)
    producto.cambiar_precio(-5)
except ValueError as e:
    print(e)

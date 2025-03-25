class Rectangulo:
    def __init__(self, largo, ancho):
        # Asegurarse de que tanto el largo como el ancho sean mayores que cero
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = largo  # Atributo privado
        self.__ancho = ancho  # Atributo privado
    
    # Método para cambiar las dimensiones del rectángulo
    def cambiar_dimensiones(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = largo
        self.__ancho = ancho
    
    # Método para calcular el área del rectángulo
    def calcular_area(self):
        return self.__largo * self.__ancho
    
    # Método para calcular el perímetro del rectángulo
    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)
    
    # Método para consultar las dimensiones actuales
    def obtener_dimensiones(self):
        return f"Largo: {self.__largo}, Ancho: {self.__ancho}"

# Ejemplo
try:
    # Crear un rectángulo con largo 5 y ancho 3
    rectangulo = Rectangulo(5, 3)
    
    # Consultar las dimensiones actuales
    print(f"Dimensiones iniciales: {rectangulo.obtener_dimensiones()}")
    
    # Calcular y mostrar el área
    print(f"Área del rectángulo: {rectangulo.calcular_area()} unidades cuadradas")
    
    # Calcular y mostrar el perímetro
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()} unidades")
    
    # Cambiar las dimensiones del rectángulo
    rectangulo.cambiar_dimensiones(8, 4)
    print(f"Dimensiones después de cambiar: {rectangulo.obtener_dimensiones()}")
    
    # Intentar cambiar las dimensiones a valores no válidos (negativos)
    rectangulo.cambiar_dimensiones(-2, 3)
except ValueError as e:
    print(e)

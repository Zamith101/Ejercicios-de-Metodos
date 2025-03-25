class Empleado:
    # Atributo de clase para llevar el contador de empleados
    cantidad_total_empleados = 0
    
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Atributo privado para el nombre del empleado
        self.__salario = salario  # Atributo privado para el salario del empleado
        
        # Incrementamos el contador de empleados al crear un nuevo empleado
        Empleado.cantidad_total_empleados += 1
    
    # Método para consultar el nombre del empleado
    def obtener_nombre(self):
        return self.__nombre
    
    # Método para consultar el salario del empleado
    def obtener_salario(self):
        return self.__salario
    
    # Método de clase para obtener la cantidad total de empleados
    @classmethod
    def cantidad_empleados(cls):
        return cls.cantidad_total_empleados


# Ejemplo
try:
    # Crear empleados
    empleado1 = Empleado("Juan Pérez", 3000)
    empleado2 = Empleado("María Gómez", 3500)
    empleado3 = Empleado("Carlos López", 4000)
    
    # Consultar la cantidad total de empleados
    print(f"Total de empleados: {Empleado.cantidad_empleados()}")
    
    # Consultar detalles de un empleado
    print(f"Empleado: {empleado1.obtener_nombre()}, Salario: ${empleado1.obtener_salario()}")
    print(f"Empleado: {empleado2.obtener_nombre()}, Salario: ${empleado2.obtener_salario()}")
    print(f"Empleado: {empleado3.obtener_nombre()}, Salario: ${empleado3.obtener_salario()}")
    
except ValueError as e:
    print(e)

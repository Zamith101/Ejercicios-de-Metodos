import random

class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
        self.__notas = []       # Atributo privado para almacenar las notas
    
    # Método para agregar una nueva nota aleatoria
    def agregar_nota_aleatoria(self):
        nota = random.randint(0, 100)  # Genera una nota aleatoria entre 0 y 100
        self.__notas.append(nota)
    
    # Método para calcular el promedio de las notas
    def calcular_promedio(self):
        if len(self.__notas) == 0:
            return 0  # Si no hay notas, el promedio es 0
        return sum(self.__notas) / len(self.__notas)
    
    # Métodos para consultar el nombre y la edad del estudiante
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_edad(self):
        return self.__edad

# Ejemplo
try:
    estudiante = Estudiante("Juan Pérez", 20)
    
    # Agregar 5 notas aleatorias
    for _ in range(5):
        estudiante.agregar_nota_aleatoria()
    
    print(f"Nombre: {estudiante.obtener_nombre()}")
    print(f"Edad: {estudiante.obtener_edad()}")
    print(f"Notas: {estudiante._Estudiante__notas}")  # Mostrar las notas generadas
    print(f"Promedio de notas: {estudiante.calcular_promedio():.2f}")
    
except ValueError as e:
    print(e)

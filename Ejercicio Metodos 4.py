class Libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        self.__total_paginas = total_paginas  # Atributo privado
        self.__pagina_actual = 1  # El lector comienza en la página 1

    # Método para avanzar un número de páginas
    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas > self.__total_paginas:
            raise ValueError(f"No puedes avanzar más allá de la página {self.__total_paginas}.")
        self.__pagina_actual += paginas

    # Método para retroceder un número de páginas
    def retroceder_paginas(self, paginas):
        if self.__pagina_actual - paginas < 1:
            raise ValueError("No puedes retroceder más allá de la página 1.")
        self.__pagina_actual -= paginas

    # Método para consultar la página actual
    def obtener_pagina_actual(self):
        return self.__pagina_actual

    # Método para obtener la información completa del libro
    def obtener_informacion(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nTotal de Páginas: {self.__total_paginas}\nPágina Actual: {self.__pagina_actual}"

# Ejemplo
try:
    libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 500)
    
    # Avanzar 100 páginas
    libro.avanzar_paginas(100)
    print(f"Página actual después de avanzar 100 páginas: {libro.obtener_pagina_actual()}")
    
    # Retroceder 50 páginas
    libro.retroceder_paginas(50)
    print(f"Página actual después de retroceder 50 páginas: {libro.obtener_pagina_actual()}")
    
    # Intentar retroceder más allá de la página 1 (esto lanzará un error)
    libro.retroceder_paginas(200)
except ValueError as e:
    print(e)

# Obtener la información completa del libro
print("\nInformación del libro:")
print(libro.obtener_informacion())

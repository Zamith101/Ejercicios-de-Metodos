class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = numero  # Número de tarjeta de crédito
    
    @staticmethod
    def validar_tarjeta(numero):
        """
        Valida un número de tarjeta usando el algoritmo de Luhn.
        """
        # Convertir el número de tarjeta a una lista de dígitos
        digitos = [int(d) for d in str(numero)]
        longitud = len(digitos)
        suma = 0
        
        # Recorremos los dígitos de la tarjeta de derecha a izquierda
        for i in range(longitud - 1, -1, -1):
            digito = digitos[i]
            
            # Si el índice es par (contando desde 0, pero desde el final), duplicamos el dígito
            if (longitud - i) % 2 == 0:
                digito *= 2
                # Si el resultado es mayor o igual a 10, restamos 9
                if digito >= 10:
                    digito -= 9
            suma += digito
        
        # Si la suma es múltiplo de 10, el número de tarjeta es válido
        return suma % 10 == 0


# Ejemplo de uso:

try:
    # Número de tarjeta (Ejemplo con número válido de 16 dígitos)
    numero_tarjeta = "4532015112830366"
    
    # Validar la tarjeta
    if TarjetaCredito.validar_tarjeta(numero_tarjeta):
        print("El número de tarjeta es válido.")
    else:
        print("El número de tarjeta no es válido.")
    
    # Otro ejemplo de número de tarjeta inválido
    numero_tarjeta_invalido = "1234567812345670"
    if TarjetaCredito.validar_tarjeta(numero_tarjeta_invalido):
        print("El número de tarjeta es válido.")
    else:
        print("El número de tarjeta no es válido.")
    
except ValueError as e:
    print(e)

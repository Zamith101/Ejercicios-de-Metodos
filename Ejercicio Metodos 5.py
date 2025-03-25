class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado para el titular
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__saldo = saldo_inicial  # Atributo privado para el saldo
    
    # Método para depositar dinero en la cuenta
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.__saldo += monto
    
    # Método para retirar dinero de la cuenta
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= monto
    
    # Método para consultar el saldo de la cuenta
    def obtener_saldo(self):
        return self.__saldo
    
    # Método para consultar el titular de la cuenta
    def obtener_titular(self):
        return self.__titular


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, porcentaje_interes):
        super().__init__(titular, saldo_inicial)
        if porcentaje_interes < 0:
            raise ValueError("El porcentaje de interés no puede ser negativo.")
        self.__porcentaje_interes = porcentaje_interes  # Atributo privado para el porcentaje de interés
    
    # Método para aplicar el interés anual al saldo de la cuenta
    def aplicar_interes(self):
        interes = (self.obtener_saldo() * self.__porcentaje_interes) / 100
        self.depositar(interes)
    
    # Método para consultar el porcentaje de interés
    def obtener_porcentaje_interes(self):
        return self.__porcentaje_interes


# Ejemplo
try:
    # Crear una cuenta de ahorro con un saldo inicial de 1000 y un interés anual del 5%
    cuenta_ahorro = CuentaAhorro("Juan Pérez", 1000, 5)
    
    # Consultar el titular y saldo inicial
    print(f"Titular: {cuenta_ahorro.obtener_titular()}")
    print(f"Saldo inicial: ${cuenta_ahorro.obtener_saldo():.2f}")
    
    # Aplicar el interés anual
    cuenta_ahorro.aplicar_interes()
    print(f"Saldo después de aplicar el interés: ${cuenta_ahorro.obtener_saldo():.2f}")
    
    # Consultar el porcentaje de interés actual
    print(f"Porcentaje de interés: {cuenta_ahorro.obtener_porcentaje_interes()}%")
    
    # Realizar un depósito
    cuenta_ahorro.depositar(500)
    print(f"Saldo después del depósito: ${cuenta_ahorro.obtener_saldo():.2f}")
    
    # Realizar un retiro
    cuenta_ahorro.retirar(200)
    print(f"Saldo después del retiro: ${cuenta_ahorro.obtener_saldo():.2f}")
    
except ValueError as e:
    print(e)

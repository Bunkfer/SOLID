"""
    Ocultar detalles internos de un objeto
    Controlar acceso a los atributos del objeto
"""

class CuentaBancaria:
    def __init__(self, numero_cuenta,saldo):
        self._numero_cuenta = numero_cuenta #protegido
        self.__saldo = saldo #privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        self.__saldo += monto
    
    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo Insuficiente")

cuenta = CuentaBancaria("12345", 1000)
print(cuenta._numero_cuenta)
#cuenta.__saldo  FALLA POR QUE ESTA OCULTO
print(cuenta.get_saldo())

cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.get_saldo())
"""
    L - Liskov Substitution Principle (Principio de Sustitución de Liskov):

Los objetos de una clase derivada deben poder reemplazar objetos de su clase base sin alterar el comportamiento del programa.
Esto garantiza que las subclases mantengan la compatibilidad de comportamiento con la clase base.

---> Las clases hijas no deben lanzar errores en las clases padres esta es una razon para crear una nueva clase padre <----

"""
class MetodoPagoBase:
    def procesar_pago():
        pass


class MetodoPagoAutomatico(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass


class MetodoPagoManual(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass


# Metodos de pago automaticos
class PagoTarjeta(MetodoPagoAutomatico):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando tarjeta { self.numero_tarjeta}"
        )


class PagoPayPal(MetodoPagoAutomatico):
    def __init__(self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando PayPal cuenta { self.cuenta_paypal}"
        )


class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando Bitcoin { self.direccion_bitcoin}"
        )


# Metodos de pago manual
class PagoCheque(MetodoPagoManual):
    def __init__(self, numero_cheque):
        self.numero_cheque = numero_cheque

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago manual de {cantidad} usando cheque {self.numero_cheque}"
        )


def realizar_pago_automatico(metodo_pago: MetodoPagoAutomatico, cantidad):
    metodo_pago.procesar_pago(cantidad)


def realizar_pago_manual(metodo_pago: MetodoPagoManual, cantidad):
    metodo_pago.procesar_pago(cantidad)


# Instanciar las clases
pago_tarjeta = PagoTarjeta("123 456 789 123")
pago_paypal = PagoPayPal("mi_cuenta@pago.com")
pago_bitcoin = PagoBitcoin("892173912udfhie938")
pago_cheque = PagoCheque("123456768")

realizar_pago_automatico(pago_tarjeta, 1000)
realizar_pago_automatico(pago_paypal, 400)
realizar_pago_automatico(pago_bitcoin, 6000)

realizar_pago_manual(pago_cheque, 3000)


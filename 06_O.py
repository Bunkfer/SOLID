"""
    O - Open/Closed Principle (Principio Abierto/Cerrado):

Las entidades de software (clases, módulos, funciones) deben estar abiertas para su ampliacion pero cerradas para modificación.
Puedes añadir nuevas funcionalidades extendiendo el código existente, pero no modificando su estructura original.
"""

from abc import ABC, abstractmethod

# clase maestra
class ManejadorPedidos(ABC):
    @abstractmethod
    def procesar_pedido(self, detalles):
        pass

class PedidoParaLlevar(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para llevar: {detalles}")

class PedidoLocal(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para comer en el local: {detalles}")

class PedidoEntregaADomicilio(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para entrega a domicilio: { detalles}")

class PedidoEspecial(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para evento especial: {detalles}")

class Restaurante:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.manejadores_pedido = []

    def registrar_pedido(self, pedido):
        self.manejadores_pedido.append(pedido)

    def generar_pedido(self, tipo_pedido, detalles):
        tipo_pedido.procesar_pedido(detalles)

    def mostrar_pedidos(self):
        if not self.manejadores_pedido:
            print("\nNo hay pedidos registrados.")
        else:
            print("\nPedidos registrados:")
            for pedido in self.manejadores_pedido:
                print(pedido)

restaurante = Restaurante("Mi restaurante de pastas ")

pedido1 = "Plato de pasta grande"
pedido2 = "Plato especial de mariscos"

restaurante.registrar_pedido(pedido1)
restaurante.registrar_pedido(pedido2)

restaurante.generar_pedido(PedidoParaLlevar(), pedido1)
restaurante.generar_pedido(PedidoEspecial(), pedido2)

restaurante.mostrar_pedidos()




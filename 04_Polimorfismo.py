"""
Capacidad de diferentes objetos para responder
a la misma invocacion
En este caso la def area se comporta diferente en diferentes clases
"""

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio**2

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return self.lado**2
    
def calcular_area(figura):
    return figura.area()

circulo1 = Circulo(5)
cuadrado1 = Cuadrado(10)
print(f"El area del circulo {calcular_area(circulo1)}")
print(f"El area del cuadrado {calcular_area(cuadrado1)}")
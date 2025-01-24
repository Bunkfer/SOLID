"""
    Separacion del comportamiento de un objeto
    El objeto que en este caso es un vehiculo se puede:
        prender, apagar, acelerar, frenar, abrir puertas, cambiar rueda, etc
"""

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0
    
    def encencer(self):
        self.encendido =  True
        print("El vehiculo esta Encendido")
    
    def apagar(self):
        self.encendido =  False
        print("El vehiculo esta Apagado")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El vehiculo ha acelerado {self.velocidad} km/h")
        else:
            print("No se puede acelerar, encienda el vehiculo")
    
    def frenar(self, decremento):
        if self.encendido:
            if (self.velocidad-decremento)>=0:
                print(f"El veliculo desacelero a {self.velocidad} km/h")
            else:
                self.velocidad = 0
                print("El vehiculo se detuvo")
        else:
            print("No se puede frenar, encienda el vehiculo")
    
    def mostrar_vehiculo(self):
        print(f"Este es un {self.marca} de {self.modelo}")   

vehiculo1 = vehiculo("Toyota", "Corolla")
vehiculo1.mostrar_vehiculo()
vehiculo1.encencer()
vehiculo1.acelerar(10)
vehiculo1.frenar(10)
vehiculo1.apagar()



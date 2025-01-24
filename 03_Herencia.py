class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir(self):
        return f"Este vehiculo es un {self.modelo}"
    
class automovil(vehiculo):
    def __init__(self,marca,modelo,puertas):
        vehiculo.__init__(self,marca,modelo)
        """
        Se puede heredar de esta forma
        ------>>> super().__init__(self,marca,modelo)
        pero cuando hay dos o tres generaciones de herencia no sirve
        """
        self.puertas = puertas
    def escribir(self):
        return f"Este es un automovil {self.marca} {self.modelo} con {self.puertas} puertas"
    
class camion(vehiculo):
    def __init__(self,marca,modelo,puertas,carga):
        vehiculo.__init__(self,marca,modelo)
        self.puertas = puertas
        self.carga = carga
    def escribir(self):
        return f"Este es un camion {self.marca} {self.modelo} con {self.puertas} puertas y puede cargar {self.carga}"   
    
auto1 = automovil("toyota","corola",4)
camion1 = camion("Toyota", "camion", 2, "200 kg")

print(auto1.escribir())
print(camion1.escribir())
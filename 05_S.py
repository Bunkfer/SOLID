"""
    S - Single Responsibility Principle (Principio de Responsabilidad Única):

Una clase debe tener una única responsabilidad o razón para cambiar.
Cada clase debe encargarse de una parte específica de la funcionalidad del sistema. 
Esto mejora la claridad y facilita el mantenimiento.
"""

class Engine:
    def getRPM(self):
        return 3000  # valor por defecto del motor


class Vehicle:
    def __init__(self, name, speed, engine):
        self._name = name
        self._speed = speed
        self._engine = engine

    def getName(self):
        return self._name

    def getEngimeRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed


class VehiclePrinter:
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RPM: {}".format(
                self._vehicle.getName(),
                self._vehicle.getMaxSpeed(),
                self._vehicle.getEngimeRPM(),
            )
        )


class VehiclePersistance:
    def __init__(self, vehicle, db):
        self._vehicle = vehicle
        self._persistance = db
        print("Hey, storing data! in", self._persistance)


if __name__ == "__main__":
    engine = Engine()
    vehicle = Vehicle(name="Honda", engine=engine, speed=300)
    persistance = VehiclePersistance(vehicle=vehicle, db="SQL")
    printer = VehiclePrinter(vehicle=vehicle)
    printer.printInfo()
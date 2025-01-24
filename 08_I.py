"""
    I - Interface Segregation Principle (ISP) - Principio de Segregación de Interfaces
Una clase no debería estar obligada a implementar interfaces que no utiliza. 
Es mejor dividir las interfaces grandes en interfaces más pequeñas y específicas.
"""

from abc import ABC, abstractmethod
from typing import Protocol

"""
class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    def turn_off(self) -> None:
        pass


class ITemperatureRegulatable(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int) -> None:
        pass
"""

class ISwitchable(Protocol):
    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...
    

class ITemperatureRegulatable(Protocol):
    def set_temperature(self, temperature: int) -> None: ...


class SmartLight(ISwitchable):
    def turn_off(self) -> None:
        print("Turning light OFF")

    def turn_on(self) -> None:
        print("Turning light ON")


class SmartTemperature(ISwitchable, ITemperatureRegulatable):
    def turn_off(self) -> None:
        print("Turning Temp. OFF")

    def turn_on(self) -> None:
        print("Turning Temp. ON")

    def set_temperature(self, temperature: int) -> None:
        print(f"Setting temperature {temperature}")


smartLight = SmartLight()
smartLight.turn_off()
smartLight.turn_on()


smartTherm = SmartTemperature()
smartTherm.turn_off()
smartTherm.turn_on()
smartTherm.set_temperature(10)


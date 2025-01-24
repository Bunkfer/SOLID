"""
    D - Dependency Inversion Principle (DIP) - Principio de Inversión de Dependencias
Las clases de alto nivel no deben depender de clases de bajo nivel; ambas deben depender de abstracciones.
"""

from abc import ABC, abstractmethod
from typing import Protocol


# Abstraccion  para el servicio de notificacion ( interface )
"""
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass
"""
class Notificador(Protocol):
    def enviar(self, mensaje: str) -> None: ...

# Implementacion del servicio de notificacion para correo electronico
# Clase de BAJO NIVEL --> (incluye detalles)
class EmailNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando email: {mensaje}")


# Implementacion del servicio de notificacion para SMS
# Clase de BAJO NIVEL --> (incluye detalles)
class SmsNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando sms: {mensaje}")


# Clase o modulo de ALTO NIVEL que maneja la logica de negocios
class App:
    def __init__(self, notificador: Notificador):  # inversion DE DEPENDENCIAS
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print(f"Notificacion enviada correctamente")


# MODO DE USO
email_notificador = EmailNotificador()
app_con_email = App(email_notificador)  # INYECCION DE DEPENDENCIAS
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electronico")

sms_notificador = SmsNotificador()
app_con_sms = App(sms_notificador)  # INYECCION DE DEPENDENCIAS
app_con_sms.enviar_notificacion("Este es un mensaje de prueba de sms")
email_notificador = EmailNotificador()
app_con_email = App(email_notificador)
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electronico")


from MediConnect import MediConnect
from Factura import Factura
from HistorialMedico import HistorialMedico
from Pago import Pago
from ServicioMedico import ServicioMedico

class Usuarios():
  def __init__(self,Nombre,Contraseña,IdCita):
    self.Nombre = Nombre
    self.Contraseña = Contraseña
    self.mediconnect = MediConnect(IdCita)
  def __getattr__(self, attr):
    return getattr(self.mediconnect, attr)
  def IniciarSesion(self,IdUsuario):
    return f"Sesion iniciada del Usuario {IdUsuario}"
  def CerrarSesion(self,IdUsuario):
    return f"Sesion finalizada del Usuario {IdUsuario}"


class Paciente(Usuarios):
  def __init__(self,Nombre,Contraseña,IdCita, #Usuario
               Solicitud,Enfermedad,          #Paciente
               IdPaciente,DiagnosticoPrev,Tratamiento, #HistorialMedico
               IdPago,Monto):                 #Pago
    Usuarios.__init__(self,Nombre,Contraseña,IdCita)
    self.Solicitud = Solicitud
    self.Enfermedad = Enfermedad
    self.NoHist = HistorialMedico(IdPaciente,DiagnosticoPrev,Tratamiento)
    self.NoPago = Pago(IdPago,Monto)
  def __getattr__(self, attr):
        try:
            return getattr(self.mediconnect, attr)
        except AttributeError:
            pass  # Si no se encuentra en mediconnect, intenta con HistorialMedico
        try:
            return getattr(self.NoHist, attr)
        except AttributeError:
            pass  # Si no se encuentra en historial, intenta en Pago
        try:
            return getattr(self.NoPago, attr)
        except AttributeError:
            pass
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")
  def VerHistorial(self):
    return f"En el historial agregamos la enfermedad {self.Enfermedad}"
  def Pagar(self):
    return f"El pago del paciente {self.IdPaciente} se esta ejecutando\nNo. Solicitud: {self.Solicitud}"

class Medico(Usuarios):
  def __init__(self,Nombre,Contraseña,IdCita, #Usuario
               Especialidad,Horario,          #Medico
               IdServicio,Disponibilidad):    #ServicioMedico
    Usuarios.__init__(self,Nombre,Contraseña,IdCita)
    self.Especialidad = Especialidad
    self.Horario = Horario
    self.NoServ = ServicioMedico(IdServicio,Disponibilidad,IdCita)
  def __getattr__(self, attr):
        try:
            return getattr(self.mediconnect, attr)
        except AttributeError:
            pass  # Si no se encuentra en mediconnect, intenta con ServicioMedico
        try:
            return getattr(self.NoServ, attr)
        except AttributeError:
            pass  
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")
  def ActualizarHistorial(self):
    return f"El Horario del especialista {self.Especialidad} es: {self.Horario} "

class Administrativo(Usuarios):
  def __init__(self,Nombre,Contraseña,IdCita, #Usuarios
               HoraEntrada,HoraSalida,CntPagos,CntFactura, #Administrativo
               IdFactura,IdPaciente,IdPago,Monto): #Factura
    Usuarios.__init__(self,Nombre,Contraseña,IdCita)
    self.HoraEntrada = HoraEntrada
    self.HoraSalida = HoraSalida
    self.CntPagos = CntPagos
    self.CntFactura = CntFactura
    self.NoFactura = Factura(IdFactura,IdPaciente,IdPago,Monto)
  def __getattr__(self, attr):
        try:
            return getattr(self.mediconnect, attr)
        except AttributeError:
            pass  # Si no se encuentra en mediconnect, intenta con ServicioMedico
        try:
            return getattr(self.NoFactura, attr)
        except AttributeError:
            pass  
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")
  def IrAtrabajar(self):
    return f"El trabajador {self.Nombre} esta dirijiendose a trabajar"
  def RegistrarEntrada(self):
    return f"El trabajador {self.Nombre} entro a trabajar a {self.HoraEntrada}"
  def ProcesarPago (self):
    return f"El pago {self.IdPago} esta en proceso"
  def Facturar (self):
    return f"Se han generado {self.CntFactura}"
  def ConfirmarPago(self):
    return f"Se han confirmado {self.CntPagos}"
  def VerificarSeguro(self):
    return f"El seguro esta activo"
  def RegistrarSalida(self):
    return f"El trabajador {self.Nombre} salio del trabajo a {self.HoraSalida}"
  def RegresarCasa(self):
    return f"El trabajador {self.Nombre} regreso a casa"
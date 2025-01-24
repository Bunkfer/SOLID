class MediConnect():
  def __init__(self,IdCita):
    self.IdCita = IdCita
  def ModificarCita(self):
    return f"Se Modifica cita {self.IdCita}"
  def CancelarCita(self):
    return f"Se Cancela cita {self.IdCita}"
  def ProgramarCita(self):
    return f"Se Programa cita {self.IdCita}"
  def ConsultarCita(self):
    return f"Se Consulta cita {self.IdCita}"
  def ConfirmarCita(self):
    return f"La cita {self.IdCita} se puede realizar"
  def AdminCita(self):
    return f"Se Administra cita {self.IdCita}"
  def GestionandoCita(self):
    return f"Se Gestiona cita {self.IdCita}"
class ServicioMedico():
  def __init__(self,IdServicio,Disponibilidad,IdCita):
    self.IdServicio = IdServicio
    self.Disponibilidad = Disponibilidad
    self.IdCita = IdCita
  def Consultar(self):
    return f"La cita {self.IdCita} en el servicio {self.IdServicio} esta {self.Disponibilidad}"
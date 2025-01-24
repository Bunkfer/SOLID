class HistorialMedico():
  def __init__(self,IdPaciente,DiagnosticoPrev,Tratamiento):
    self.IdPaciente = IdPaciente
    self.DiagnosticoPrev = DiagnosticoPrev
    self.Tratamiento = Tratamiento
  def Añadir(self):
    return f"Se añade un historial del paciente {self.IdPaciente}"
  def Obtener(self):
    return f"El paciente: {self.IdPaciente}\nDiagnostico: {self.DiagnosticoPrev}\nTratamiento: {self.Tratamiento}"
  def Modificar(self):
    return f"Se ha modificado un parametro del paciente {self.IdPaciente}"
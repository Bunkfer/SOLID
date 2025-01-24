class Factura():
  def __init__(self,IdFactura,IdPaciente,IdPago,Monto):
    self.IdFactura = IdFactura
    self.IdPaciente = IdPaciente
    self.Monto = Monto
    self.IdPago = IdPago
  def Generar(self):
    return f"La factura {self.IdFactura} se esta generando\nMonto: {self.Monto}\nPaciente: {self.IdPaciente}"
  def Actualizar(self):
    return f"La factura {self.IdFactura} ligada al pago {self.IdPago}\nEsta actualizada"
class Pago():
  def __init__(self,IdPago,Monto):
    self.IdPago =IdPago
    self.Monto = Monto
  def Procesar(self):
    return f"El pago {self.IdPago} por el monto {self.Monto}\nEsta en Proceso"
import sys
from PyQt5.QtWidgets import (QMessageBox,QApplication,QFormLayout, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout)
from Usuarios import *

class MediConnectApp(QMainWindow):
    def __init__(self):
        super(MediConnectApp, self).__init__()
        self.setWindowTitle('MediConnect System')
        self.setGeometry(1000, 400, 1000, 500)
        
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        
        self.tabAdministrativo = QWidget()
        self.tabMedico = QWidget()
        self.tabPaciente = QWidget()
        
        self.tabWidget.addTab(self.tabPaciente, "Paciente")
        self.tabWidget.addTab(self.tabMedico, "Medico")
        self.tabWidget.addTab(self.tabAdministrativo, "Administrativo")

        # Inicialización de UI para cada pestaña
        self.create_administrativo_tab()
        self.create_medico_tab()
        self.create_paciente_tab()

        self.headerLabel = QLabel(f"Bienvenido al Restaurante 'El Buen Sabor' - Calle Principal #123")
        self.headerLabel.setStyleSheet("""
                                            QLabel {
                                                color: black;
                                                background-color: gray;
                                                font-size: 26px; 
                                                font-weight: bold;
                                                padding: 30px 0px;
                                            }
                                        """)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.headerLabel)

        self.headerLabel = QLabel(f"Hospital General No. 3  (Recuerda guardar primero la información)")
        self.headerLabel.setStyleSheet("""
                                            QLabel {
                                                color: blue;
                                                background-color: white;
                                                font-size: 26px; 
                                                font-weight: bold;
                                                padding: 20px 0px;
                                            }
                                        """)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.headerLabel)
        self.layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

    def create_administrativo_tab(self):
        from Usuarios import Administrativo
        
        layoutAdmin = QFormLayout()
        
                                                        #Usuario
        self.nombreAdmin = QLineEdit()
        self.contrasenaAdmin = QLineEdit()

        #Sesion
        sesionLayout = QHBoxLayout()
        self.IniciarSesion = QPushButton("Iniciar Sesión")
        self.CerrarSesion = QPushButton("Cerrar Sesión")
        sesionLayout.addWidget(self.IniciarSesion)
        sesionLayout.addWidget(self.CerrarSesion)

        #Cita
        CitaLayout = QHBoxLayout()
        self.AdminCita = QPushButton("Admin Cita")
        self.ConfirmarCita = QPushButton("Confirmar Cita")
        self.GestionandoCita = QPushButton("Gestionar Cita")
        CitaLayout.addWidget(self.AdminCita)
        CitaLayout.addWidget(self.ConfirmarCita)
        sesionLayout.addWidget(self.GestionandoCita)
        
                                                        #Administrativo
        self.HoraEntrada = QLineEdit()
        self.HoraSalida = QLineEdit()
        self.CntPagos = QLineEdit()
        self.CntFactura = QLineEdit()

        # Botones Layout 1
        Admin1Layout = QHBoxLayout()
        self.IrATrabajar = QPushButton("Ir A Trabajar")
        self.RegistrarEntrada = QPushButton("Registrar Entrada")
        self.ProcesarPago = QPushButton("Procesar Pago")
        self.Facturar = QPushButton("Facturar")
        Admin1Layout.addWidget(self.IrATrabajar)
        Admin1Layout.addWidget(self.RegistrarEntrada)
        Admin1Layout.addWidget(self.ProcesarPago)
        Admin1Layout.addWidget(self.Facturar)

        # Botones Layout 2
        Admin2Layout = QHBoxLayout()
        self.ConfirmarPago = QPushButton("Confirmar Pago")
        self.VerificarSeguro = QPushButton("Verificar Seguro")
        self.RegistrarSalida = QPushButton("Registrar Salida")
        self.RegresarCasa = QPushButton("Regresar Casa")
        Admin2Layout.addWidget(self.ConfirmarPago)
        Admin2Layout.addWidget(self.VerificarSeguro)
        Admin2Layout.addWidget(self.RegistrarSalida)
        Admin2Layout.addWidget(self.RegresarCasa)
        
                                                            #Factura
        self.IdFactura = QLineEdit()
        self.IdPaciente = QLineEdit()
        self.IdPago = QLineEdit()
        self.Monto = QLineEdit()

        #Boton Pago
        PagoLayout = QHBoxLayout()
        self.Generar = QPushButton("Generar")
        self.Actualizar = QPushButton("Actualizar")
        PagoLayout.addWidget(self.Generar)
        PagoLayout.addWidget(self.Actualizar)

        #Boton General
        self.Guardar = QPushButton("Guardar")
        
        self.IDuser_Ad = QLabel("0000")
        # Añadir los campos al layout
        layoutAdmin.addRow("Id Usuario: ", self.IDuser_Ad)
        layoutAdmin.addRow("Nombre:", self.nombreAdmin)
        layoutAdmin.addRow("Contraseña:", self.contrasenaAdmin)
        layoutAdmin.addRow("", sesionLayout)
        layoutAdmin.addRow("", CitaLayout)

        layoutAdmin.addRow("Hora Entrada:", self.HoraEntrada)
        layoutAdmin.addRow("Hora Salida:", self.HoraSalida)
        layoutAdmin.addRow("Cantidad de Pagos:", self.CntPagos)
        layoutAdmin.addRow("Cantidad de Facturas:", self.CntFactura)
        layoutAdmin.addRow("", Admin1Layout)
        layoutAdmin.addRow("", Admin2Layout)
       
        layoutAdmin.addRow("ID Factura:", self.IdFactura)
        layoutAdmin.addRow("ID Paciente:", self.IdPaciente)
        layoutAdmin.addRow("ID Pago:", self.IdPago)
        layoutAdmin.addRow("Monto:", self.Monto)
        layoutAdmin.addRow("", PagoLayout)
        layoutAdmin.addRow("", self.Guardar)
        
        self.tabAdministrativo.setLayout(layoutAdmin)
        self.Guardar.clicked.connect(self.crear_administrativo)     
        
        self.IniciarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Ad.IniciarSesion(f"Mediconnect.User.{self.IDuser_Ad.text()}")))
        self.CerrarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Ad.CerrarSesion(f"Mediconnect.User.{self.IDuser_Ad.text()}")))
        self.AdminCita.clicked.connect(lambda: self.MostrarMensaje(self.Ad.AdminCita()))
        self.ConfirmarCita.clicked.connect(lambda: self.MostrarMensaje(self.Ad.ConfirmarCita()))
        self.GestionandoCita.clicked.connect(lambda: self.MostrarMensaje(self.Ad.GestionandoCita()))

        self.IrATrabajar.clicked.connect(lambda: self.MostrarMensaje(self.Ad.IrAtrabajar()))
        self.RegistrarEntrada.clicked.connect(lambda: self.MostrarMensaje(self.Ad.RegistrarEntrada()))
        self.ProcesarPago.clicked.connect(lambda: self.MostrarMensaje(self.Ad.ProcesarPago()))
        self.Facturar.clicked.connect(lambda: self.MostrarMensaje(self.Ad.Facturar()))

        self.ConfirmarPago.clicked.connect(lambda: self.MostrarMensaje(self.Ad.ConfirmarPago()))
        self.VerificarSeguro.clicked.connect(lambda: self.MostrarMensaje(self.Ad.VerificarSeguro()))
        self.RegistrarSalida.clicked.connect(lambda: self.MostrarMensaje(self.Ad.RegistrarSalida()))
        self.RegresarCasa.clicked.connect(lambda: self.MostrarMensaje(self.Ad.RegresarCasa()))

        self.Generar.clicked.connect(lambda: self.MostrarMensaje(self.Ad.Generar()))
        self.Actualizar.clicked.connect(lambda: self.MostrarMensaje(self.Ad.Actualizar()))

    def crear_administrativo(self):
        import random
        from Usuarios import Administrativo
        IdUsuario = random.randint(0000, 9999)  # Asegúrate de que estos valores sean accesibles
        self.IDuser_Ad.setText(f"{IdUsuario}")
        IdCita = random.randint(0000, 9999)
        self.Ad = Administrativo(self.nombreAdmin.text(), self.contrasenaAdmin.text(), IdCita,
                                 self.HoraEntrada.text(), self.HoraSalida.text(), self.CntPagos.text(), self.CntFactura.text(), 
                                 self.IdFactura.text(), self.IdPaciente.text(), self.IdPago.text(), self.Monto.text())

    def create_medico_tab(self):
        from Usuarios import Medico
        
        layoutMedico = QFormLayout()
                                                        #Usuario
        self.nombreAdmin = QLineEdit()
        self.contrasenaAdmin = QLineEdit()

        #Sesion
        sesionLayout = QHBoxLayout()
        self.IniciarSesion = QPushButton("Iniciar Sesión")
        self.CerrarSesion = QPushButton("Cerrar Sesión")
        sesionLayout.addWidget(self.IniciarSesion)
        sesionLayout.addWidget(self.CerrarSesion)

        #Cita
        self.ConsultarCita = QPushButton("Consultar Cita")

        
                                                        #Medico
        self.Especialidad = QLineEdit()
        self.Horario = QLineEdit()
        
        self.ActualizarHistorial = QPushButton("Actualizar Historial")

                                                        #Servicio Medico
        self.IdServicio = QLineEdit()
        self.Disponibilidad = QLineEdit()
        self.IdCita = QLineEdit()

        #Boton
        self.Consultar = QPushButton("Consultar")

        #Boton General
        self.Guardar = QPushButton("Guardar")
        
        
        # Añadir los campos al layout
        self.IDuser_Me = QLabel("0000")
        layoutMedico.addRow("Id Usuario: ", self.IDuser_Me)
        layoutMedico.addRow("Nombre:", self.nombreAdmin)
        layoutMedico.addRow("Contraseña:", self.contrasenaAdmin)
        layoutMedico.addRow("", sesionLayout)
        layoutMedico.addRow("", self.ConsultarCita)

        layoutMedico.addRow("Especilidad:", self.Especialidad)
        layoutMedico.addRow("Horario:", self.Horario)
        layoutMedico.addRow("", self.ActualizarHistorial)

        layoutMedico.addRow("IdServicio:", self.IdServicio)
        layoutMedico.addRow("Disponibilidad:", self.Disponibilidad)
        layoutMedico.addRow("", self.Consultar)

        layoutMedico.addRow("", self.Guardar)


        self.tabMedico.setLayout(layoutMedico)
        self.Guardar.clicked.connect(self.crear_medico)  

        self.IniciarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Md.IniciarSesion(f"Mediconnect.User.{self.IDuser_Me.text()}")))
        self.CerrarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Md.CerrarSesion(f"Mediconnect.User.{self.IDuser_Me.text()}")))
        self.ConsultarCita.clicked.connect(lambda: self.MostrarMensaje(self.Md.ConsultarCita()))

        self.ActualizarHistorial.clicked.connect(lambda: self.MostrarMensaje(self.Md.ActualizarHistorial()))
        self.Consultar.clicked.connect(lambda: self.MostrarMensaje(self.Md.Consultar()))

    def crear_medico(self):
        import random
        from Usuarios import Medico
        IdUsuario = random.randint(0000, 9999)  # Asegúrate de que estos valores sean accesibles
        self.IDuser_Me.setText(f"{IdUsuario}")
        IdCita = random.randint(0000, 9999)
        self.Md = Medico(self.nombreAdmin.text(), self.contrasenaAdmin.text(), IdCita,
                                 self.Especialidad.text(),self.Horario.text(), 
                                 self.IdServicio.text(), self.Disponibilidad.text())

    def create_paciente_tab(self):
        from Usuarios import Paciente

        layoutPaciente = QFormLayout()

                                            #Usuario
        self.nombreAdmin = QLineEdit()
        self.contrasenaAdmin = QLineEdit()

        #Sesion
        sesionLayout = QHBoxLayout()
        self.IniciarSesion = QPushButton("Iniciar Sesión")
        self.CerrarSesion = QPushButton("Cerrar Sesión")
        sesionLayout.addWidget(self.IniciarSesion)
        sesionLayout.addWidget(self.CerrarSesion)

        #Cita
        cita1Layout = QHBoxLayout()
        self.ProgramarCita = QPushButton("Programar Cita")
        self.ModificarCita = QPushButton("Modificar Cita")
        self.CancelarCita = QPushButton("Cancelar Cita")
        cita1Layout.addWidget(self.ProgramarCita)
        cita1Layout.addWidget(self.ModificarCita)
        cita1Layout.addWidget(self.CancelarCita)

                                            #Paciente
        self.Solicitud = QLineEdit()
        self.Enfermedad = QLineEdit()
        
        md1Layout = QHBoxLayout()
        self.VerHistorial = QPushButton("Ve rHistorial")
        self.Pagar = QPushButton("Pagar")
        md1Layout.addWidget(self.VerHistorial)
        md1Layout.addWidget(self.Pagar)

                                            #Historial Medico
        self.IdPaciente = QLineEdit()
        self.DiagnosticoPrev = QLineEdit()
        self.Tratamiento = QLineEdit()

        HM1Layout = QHBoxLayout()
        self.Añadir = QPushButton("Añadir")
        self.Obtener = QPushButton("Obtener")
        self.Modificar = QPushButton("Modificar")
        HM1Layout.addWidget(self.Añadir)
        HM1Layout.addWidget(self.Obtener)
        HM1Layout.addWidget(self.Modificar)

                                            #Pago
        self.IdPago = QLineEdit()
        self.Monto = QLineEdit()

        self.Procesar = QPushButton("Procesar")

        #Boton General
        self.Guardar = QPushButton("Guardar")

         # Añadir los campos al layout
        self.IDuser_Pa = QLabel("0000")
        layoutPaciente.addRow("Id Usuario: ", self.IDuser_Pa)
        layoutPaciente.addRow("Nombre:", self.nombreAdmin)
        layoutPaciente.addRow("Contraseña:", self.contrasenaAdmin)
        layoutPaciente.addRow("", sesionLayout)
        layoutPaciente.addRow("", cita1Layout)

        layoutPaciente.addRow("Solicitud:", self.Solicitud)
        layoutPaciente.addRow("Enfermedad:", self.Enfermedad)
        layoutPaciente.addRow("", md1Layout)

        layoutPaciente.addRow("IdPaciente:", self.IdPaciente)
        layoutPaciente.addRow("Diagnostico Previo:", self.DiagnosticoPrev)
        layoutPaciente.addRow("Tratamiento:", self.Tratamiento)
        layoutPaciente.addRow("", HM1Layout)

        layoutPaciente.addRow("IdPago:", self.IdPago)
        layoutPaciente.addRow("Monto:", self.Monto)
        layoutPaciente.addRow("", self.Procesar)

        layoutPaciente.addRow("", self.Guardar)

        self.tabPaciente.setLayout(layoutPaciente)
        self.Guardar.clicked.connect(self.crear_paciente)  

        self.IniciarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Pa.IniciarSesion(f"Mediconnect.User.{self.IDuser_Pa.text()}")))
        self.CerrarSesion.clicked.connect(lambda: self.MostrarMensaje(self.Pa.CerrarSesion(f"Mediconnect.User.{self.IDuser_Pa.text()}")))
        self.ProgramarCita.clicked.connect(lambda: self.MostrarMensaje(self.Pa.ProgramarCita()))
        self.ModificarCita.clicked.connect(lambda: self.MostrarMensaje(self.Pa.ModificarCita()))
        self.CancelarCita.clicked.connect(lambda: self.MostrarMensaje(self.Pa.CancelarCita()))

        self.VerHistorial.clicked.connect(lambda: self.MostrarMensaje(self.Pa.VerHistorial()))
        self.Pagar.clicked.connect(lambda: self.MostrarMensaje(self.Pa.Pagar()))

        self.Añadir.clicked.connect(lambda: self.MostrarMensaje(self.Pa.Añadir()))
        self.Obtener.clicked.connect(lambda: self.MostrarMensaje(self.Pa.Obtener()))
        self.Modificar.clicked.connect(lambda: self.MostrarMensaje(self.Pa.Modificar()))

        self.Procesar.clicked.connect(lambda: self.MostrarMensaje(self.Pa.Procesar()))

    def crear_paciente(self):
        import random
        from Usuarios import Paciente
        IdUsuario = random.randint(0000, 9999)  # Asegúrate de que estos valores sean accesibles
        self.IDuser_Pa.setText(f"{IdUsuario}")
        IdCita = random.randint(0000, 9999)
        self.Pa = Paciente(self.nombreAdmin.text(), self.contrasenaAdmin.text(), IdCita,
                                 self.Solicitud.text(),self.Enfermedad.text(), 
                                 self.IdPaciente.text(), self.DiagnosticoPrev.text(), self.Tratamiento.text(),
                                 self.IdPago.text(), self.Monto.text())  

    def MostrarMensaje(self,Mensaje):        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Mensaje de Inicio de Sesión")
        msgBox.setText(Mensaje)
        msgBox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MediConnectApp()
    ex.show()
    sys.exit(app.exec_())

import MySQLdb

from PyQt5 import QtWidgets

import sys


class Ventana(QtWidgets.QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        self.setWindowTitle("Biblioteca")

        self.setMaximumSize(450, 350)
        self.setMinimumSize(450, 350)
        self.resize(450, 350)

        self.conn = MySQLdb.connect(host="localhost", port=3306, user="root", password="root", db="library")


    # Puedes agregar un mensaje de error o lanzar una excepción aquí si lo prefieres.

        self.cursor = self.conn.cursor()

        self.label1 = QtWidgets.QLabel("Username", self)
        self.label2 = QtWidgets.QLabel("Password", self)
        self.label3 = QtWidgets.QLabel("Bienvenido al Sistema de Biblioteca", self)
        self.label4 = QtWidgets.QLabel("Nuevo usuario ------>", self)
        self.label5 = QtWidgets.QLabel("Bienvenido al Sistema de Biblioteca", self)
        self.label6 = QtWidgets.QLabel("Bienvenido al Sistema de Biblioteca ", self)
        self.label7 = QtWidgets.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label8 = QtWidgets.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)

        self.idUsuario = 0
        self.nombreDelUsuario = ""

        ## boton ventana princial Aceptar
        self.button1 = QtWidgets.QPushButton("Aceptar", self)

        ##boton ventana principal Registrar
        self.button2 = QtWidgets.QPushButton("Registrar", self)

        ##boton ventana agregar nuevo usuario Registrar
        self.button3 = QtWidgets.QPushButton("Registrar", self)

        ##boton ventana agregar nuevo usuario Cancelar
        self.button4 = QtWidgets.QPushButton("Cancelar", self)

        ##boton al loguearse como usuario correcto Aceptar
        self.button5 = QtWidgets.QPushButton("Aceptar", self)
        self.button5.move(86, 50)

        ##boton al entrar a la base de datos Ver Lista de Usuarios
        self.button6 = QtWidgets.QPushButton("Lista de Usuarios", self)

        ##Boton al registrar un usuario correcto Aceptar
        self.button7 = QtWidgets.QPushButton("Aceptar", self)

        ##Botones Base de Datos

        self.tabla1 = QtWidgets.QTableWidget(self)
        self.tabla1.hide()
        self.myList1 = ["Usuario_id", "Nombre", "Direccion", "Municipio", "Estado", "Email", "Password"]
        self.tabla1.setColumnCount(7)
        self.tabla1.setGeometry(35, 90, 945, 240)
        self.tabla1.setHorizontalHeaderLabels(self.myList1)
        self.tabla1.verticalHeader().hide()
        self.tabla1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.tabla1.setColumnWidth(0, 70)
        self.tabla1.setColumnWidth(1, 180)
        self.tabla1.setColumnWidth(2, 160)
        self.tabla1.setColumnWidth(3, 120)
        self.tabla1.setColumnWidth(4, 110)
        self.tabla1.setColumnWidth(5, 180)
        self.tabla1.setColumnWidth(6, 120)

        self.tabla2 = QtWidgets.QTableWidget(self)
        self.tabla2.hide()
        self.myList2 = ["Libro_id", "Nombre", "Autor", "Edicion", "Ano", "Editorial", "Disponibles"]
        self.tabla2.setColumnCount(7)
        self.tabla2.setGeometry(35, 380, 945, 240)
        self.tabla2.setHorizontalHeaderLabels(self.myList2)
        self.tabla2.verticalHeader().hide()
        self.tabla2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.tabla2.setColumnWidth(0, 50)
        self.tabla2.setColumnWidth(1, 260)
        self.tabla2.setColumnWidth(2, 260)
        self.tabla2.setColumnWidth(3, 50)
        self.tabla2.setColumnWidth(4, 50)
        self.tabla2.setColumnWidth(5, 180)
        self.tabla2.setColumnWidth(6, 75)

        self.tabla3 = QtWidgets.QTableWidget(self)
        self.tabla3.hide()
        self.myList3 = ["Libro_id", "Nombre", "Autor", "Edicion", "Ano", "Editorial"]
        self.tabla3.setColumnCount(6)
        self.tabla3.setGeometry(35, 90, 945, 240)
        self.tabla3.setHorizontalHeaderLabels(self.myList3)
        self.tabla3.verticalHeader().hide()
        self.tabla3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.tabla3.setColumnWidth(0, 60)
        self.tabla3.setColumnWidth(1, 250)
        self.tabla3.setColumnWidth(2, 250)
        self.tabla3.setColumnWidth(3, 70)
        self.tabla3.setColumnWidth(4, 70)
        self.tabla3.setColumnWidth(5, 240)

        self.button21 = QtWidgets.QPushButton("Listar mis libros", self)

        self.button8 = QtWidgets.QPushButton("Renovar libro", self)
        self.button9 = QtWidgets.QPushButton("Cerrar Sesion", self)
        self.button10 = QtWidgets.QPushButton("Buscar libro", self)
        self.button11 = QtWidgets.QPushButton("Aceptar", self)
        self.button12 = QtWidgets.QPushButton("Aceptar", self)

        ##Botones Unicamente Modo Admin
        self.button13 = QtWidgets.QPushButton("Autorizar prestamo", self)
        self.button14 = QtWidgets.QPushButton("Devolver prestamo", self)
        self.button15 = QtWidgets.QPushButton("Agregar libro", self)
        self.button16 = QtWidgets.QPushButton("Modificar libro", self)
        self.button17 = QtWidgets.QPushButton("Listar libros", self)
        self.button18 = QtWidgets.QPushButton("Guardar Cambios", self)
        self.button18.setGeometry(1100, 460, 90, 25)
        self.button19 = QtWidgets.QPushButton("Guardar Cambios", self)
        self.button19.setGeometry(1100, 510, 90, 25)

        self.lineEdit9 = QtWidgets.QLineEdit(self)
        self.lineEdit10 = QtWidgets.QLineEdit(self)
        self.lineEdit11 = QtWidgets.QLineEdit(self)
        self.lineEdit12 = QtWidgets.QLineEdit(self)

        self.label9 = QtWidgets.QLabel("Mis prestamos de libros", self)
        self.label10 = QtWidgets.QLabel("Libros disponibles en la Biblioteca", self)
        self.label11 = QtWidgets.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label12 = QtWidgets.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label13 = QtWidgets.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)

        self.button8.hide()
        self.button9.hide()
        self.button10.hide()
        self.button11.hide()
        self.button12.hide()
        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()
        self.button18.hide()
        self.button19.hide()
        self.lineEdit9.hide()
        self.lineEdit10.hide()
        self.lineEdit11.hide()
        self.lineEdit12.hide()
        self.label9.hide()
        self.label10.hide()
        self.label11.hide()
        self.label12.hide()
        self.label13.hide()

        # Ventana Extra Movimienttos

        self.label14 = QtWidgets.QLabel("Movimiento Exitoso", self)
        self.label15 = QtWidgets.QLabel("Error el usuario ya tiene el libro", self)
        self.label16 = QtWidgets.QLabel("Error el usuario no tiene el libro", self)
        self.label17 = QtWidgets.QLabel("Error no hay libros disponibles", self)
        self.button20 = QtWidgets.QPushButton("Aceptar", self)
        self.label14.setGeometry(82, 15, 150, 20)
        self.label15.setGeometry(55, 15, 150, 20)
        self.label16.setGeometry(55, 15, 150, 10)
        self.label17.setGeometry(55, 15, 150, 10)
        self.button20.setGeometry(85, 45, 80, 30)

        self.lineEdit1 = QtWidgets.QLineEdit(self)

        ##Line Edit utilizada unicamente para password en ventana inicial
        self.lineEdit2 = QtWidgets.QLineEdit(self)

        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit4 = QtWidgets.QLineEdit(self)
        self.lineEdit5 = QtWidgets.QLineEdit(self)
        self.lineEdit6 = QtWidgets.QLineEdit(self)
        self.lineEdit7 = QtWidgets.QLineEdit(self)

        ##Line Edit utilizada unicamente para password en ventana Registro de nuevo usuario
        self.lineEdit8 = QtWidgets.QLineEdit(self)

        self.label1.move(90, 90)
        self.label2.move(90, 120)
        self.label3.move(135, 20)
        self.label4.move(160, 225)
        self.button1.move(300, 89)
        self.button2.move(300, 220)
        self.button6.move(680, 80)
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.label8.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit7.hide()
        self.lineEdit8.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button6.hide()
        self.button7.hide()
        self.button21.hide()
        self.lineEdit1.setGeometry(150, 90, 135, 20)
        self.lineEdit2.setGeometry(150, 120, 135, 20)
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")
        self.lineEdit7.setText("")
        self.lineEdit8.setText("")
        self.pixmapa1 = QtWidgets.QPixmap("C:\\HelloW.jpg")

        # Ocultando Ventana Extra
        self.label14.hide()
        self.label15.hide()
        self.label16.hide()
        self.label17.hide()
        self.button20.hide()

        ##Colocando ambas LineEdit con propiedades de password unicamente
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit8.setEchoMode(QtWidgets.QLineEdit.Password)

        self.button1.clicked.connect(self.iniciarBase)
        self.button2.clicked.connect(self.insertarNuevoUsuario)
        self.button3.clicked.connect(self.registrandoNuevoUsuario)
        self.button4.clicked.connect(self.cargarVentanaInicial)
        self.button5.clicked.connect(self.interfazBaseDatos)
        self.button6.clicked.connect(self.listarUsuarios)
        self.button7.clicked.connect(self.cargarVentanaInicial)
        self.button9.clicked.connect(self.cargarVentanaInicial)
        self.button17.clicked.connect(self.listarLibros)
        self.button13.clicked.connect(self.autorizandoPrestamo)
        self.button14.clicked.connect(self.devolviendoPrestamo)
        self.button15.clicked.connect(self.agregandoLibro)
        self.button16.clicked.connect(self.modificandoLibro)
        self.button19.clicked.connect(self.agregarCambiosLibro)
        self.button18.clicked.connect(self.agregarNuevoLibro)
        self.button20.clicked.connect(self.aceptarMovimiento)
        self.button21.clicked.connect(self.verMisLibrosUsuarioNormal)
        self.button10.clicked.connect(self.buscarLibro)
        self.lineEdit9.returnPressed.connect(self.buscarLibro)
        self.button5.setAutoDefault(True)
        self.button20.setAutoDefault(True)

        # self.cursor.execute("SELECT * from libro")
        # renglon = self.cursor.fetchall()
        # print(renglon)

        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def insertarNuevoUsuario(self):

        self.label1.setText("Direccion")
        self.label2.setText("Municipio")
        self.label1.move(65, 120)
        self.label2.move(65, 160)
        self.label3.setText("Registro de Nuevo Usuario")
        self.label3.move(210, 30)
        self.label4.setText("Nombre de usuario")
        self.label4.move(65, 80)
        self.label5.setVisible(True)
        self.label5.setText("Estado")
        self.label5.move(65, 200)
        self.label6.setVisible(True)
        self.label6.setText("Email")
        self.label7.setVisible(True)
        self.label6.move(65, 240)
        self.label7.setText("Password")
        self.label7.move(65, 280)
        self.label8.hide()
        self.setMaximumSize(550, 430)
        self.setMinimumSize(550, 430)
        self.resize(550, 430)
        self.move(350, 150)
        self.lineEdit3.setVisible(True)
        self.lineEdit4.setVisible(True)
        self.lineEdit5.setVisible(True)
        self.lineEdit6.setVisible(True)
        self.lineEdit1.setGeometry(180, 80, 250, 20)
        self.lineEdit8.setGeometry(180, 280, 250, 20)
        self.lineEdit3.setGeometry(180, 120, 250, 20)
        self.lineEdit4.setGeometry(180, 160, 250, 20)
        self.lineEdit5.setGeometry(180, 200, 250, 20)
        self.lineEdit6.setGeometry(180, 240, 250, 20)
        self.button1.hide()
        self.button2.hide()
        self.button5.hide()
        self.lineEdit2.hide()
        self.button3.setVisible(True)
        self.button4.setVisible(True)
        self.button4.move(310, 340)
        self.button3.move(210, 340)
        self.lineEdit1.setText("")
        self.lineEdit8.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")
        if (self.label4.isEnabled() == True):
            self.label4.setVisible(True)
        if (self.lineEdit8.isEnabled() == True):
            self.lineEdit8.setVisible(True)

    def cargarVentanaInicial(self):

        self.tabla1.setRowCount(0)
        self.tabla2.setRowCount(0)
        self.tabla3.setRowCount(0)

        self.lineEdit9.setText("")
        self.setMaximumSize(450, 350)
        self.setMinimumSize(450, 350)
        self.resize(450, 350)
        self.center()
        self.label1.setText("Username")
        self.label2.setText("Password")
        self.label3.setText("Bienvenido al Sistema de Biblioteca")
        self.label4.setText("Nuevo usuario ------>")
        self.label5.setText("Bienvenido al Sistema de Biblioteca kdkdkdkd")
        self.label6.setText("Bienvenido al Sistema de Biblioteca jjdjdjd")
        self.label7.setText("Usernamenndjhdjdjdjdjdjddhdhdh hdhdhdhdhdhdjhd")
        self.button1.setText("Aceptar")
        self.button2.setText("Registrar")
        self.button3.setText("Registrar")
        self.button4.setText("Cancelar")
        self.label1.move(80, 100)
        self.label2.move(80, 130)
        self.label3.move(135, 20)
        self.label4.move(150, 215)
        self.button1.move(300, 99)
        self.lineEdit1.move(150, 100)
        self.lineEdit2.move(150, 130)
        self.button2.move(300, 210)
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit8.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button7.hide()
        self.tabla1.hide()
        self.tabla2.hide()
        self.tabla3.hide()
        self.button1.setVisible(True)
        self.button2.setVisible(True)
        self.lineEdit1.setGeometry(140, 100, 145, 20)
        self.lineEdit2.setGeometry(140, 130, 145, 20)
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")

        self.tabla1.clear()
        self.tabla2.clear()
        self.tabla3.clear()
        self.tabla1.setHorizontalHeaderLabels(self.myList1)
        self.tabla2.setHorizontalHeaderLabels(self.myList2)
        self.tabla3.setHorizontalHeaderLabels(self.myList3)

        ##Ocultar Interfaz De DB
        self.button6.hide()
        self.button8.hide()
        self.button9.hide()
        self.button10.hide()
        self.button11.hide()
        self.button12.hide()
        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()
        self.button18.hide()
        self.button19.hide()

        self.label14.hide()
        self.label15.hide()
        self.label16.hide()
        self.label17.hide()
        self.button20.hide()

        self.label9.hide()
        self.label10.hide()
        self.label11.hide()
        self.label12.hide()
        self.label13.hide()
        self.lineEdit9.hide()
        self.nombreDelUsuario = ""
        self.button21.hide()

        if (self.lineEdit1.isEnabled() == True):
            self.lineEdit1.setVisible(True)
        if (self.lineEdit2.isEnabled() == True):
            self.lineEdit2.setVisible(True)
        if (self.label1.isEnabled() == True):
            self.label1.setVisible(True)
        if (self.label2.isEnabled() == True):
            self.label2.setVisible(True)
        if (self.label3.isEnabled() == True):
            self.label3.setVisible(True)
        if (self.label4.isEnabled() == True):
            self.label4.setVisible(True)

    def iniciarBase(self):

        nombre = "'" + str(self.lineEdit1.text() + "'")
        contra = "'" + str(self.lineEdit2.text() + "'")
        self.cursor.execute("SELECT * from usuario where username =%s" % (nombre))
        datos = self.cursor.fetchone()

        if (datos != None):

            if (str(self.lineEdit1.text()) == 'Administrador' and str(self.lineEdit2.text()) == 'universidad'):
                self.idUsuario = int(datos[0])
                self.nombreDelUsuario += "Administrador"
                self.setMaximumSize(250, 100)
                self.setMinimumSize(250, 100)
                self.resize(250, 100)
                self.move(500, 250)
                self.label2.hide()
                self.label3.hide()
                self.label1.hide()
                self.label5.hide()
                self.label6.hide()
                self.label7.hide()
                self.button1.hide()
                self.button3.hide()
                self.button2.hide()
                self.button4.hide()
                self.lineEdit1.hide()
                self.lineEdit2.hide()
                self.lineEdit3.hide()
                self.lineEdit4.hide()
                self.lineEdit5.hide()
                self.lineEdit6.hide()
                self.lineEdit8.hide()
                self.label4.move(90, 15)
                self.label4.setText("Login Correcto")
                self.button5.setVisible(True)


            elif (datos[1] == str(self.lineEdit1.text()) and datos[6] == str(self.lineEdit2.text())):
                self.idUsuario = int(datos[0])
                self.nombreDelUsuario += str(datos[1])
                self.setMaximumSize(250, 100)
                self.setMinimumSize(250, 100)
                self.resize(250, 100)
                self.move(500, 250)
                self.label2.hide()
                self.label3.hide()
                self.label1.hide()
                self.label5.hide()
                self.label6.hide()
                self.label7.hide()
                self.button1.hide()
                self.button3.hide()
                self.button2.hide()
                self.button4.hide()
                self.lineEdit1.hide()
                self.lineEdit2.hide()
                self.lineEdit3.hide()
                self.lineEdit4.hide()
                self.lineEdit5.hide()
                self.lineEdit6.hide()
                self.lineEdit8.hide()
                self.label4.move(90, 15)
                self.label4.setText("Login Correcto")
                self.button5.setVisible(True)

            else:
                if (self.label8.isEnabled() == True):
                    self.label8.setVisible(True)
                self.label8.setGeometry(125, 60, 200, 200)
                self.label8.setPixmap(self.pixmapa1)

        else:
            if (self.label8.isEnabled() == True):
                self.label8.setVisible(True)
            self.label8.setGeometry(125, 60, 200, 200)
            self.label8.setPixmap(self.pixmapa1)

    def interfazBaseDatos(self):

        # Login Administrador
        if (self.nombreDelUsuario == 'Administrador'):
            self.setMaximumSize(1200, 680)
            self.setMinimumSize(1200, 680)
            self.resize(1200, 680)
            self.move(0, 0)
            self.label4.hide()
            self.label8.hide()
            self.button5.hide()
            self.button6.setVisible(True)
            self.button6.setGeometry(1010, 110, 105, 25)
            self.button13.setGeometry(1010, 160, 105, 25)
            self.button14.setGeometry(1010, 210, 105, 25)
            self.button17.setGeometry(1010, 410, 80, 25)
            self.button15.setGeometry(1010, 460, 80, 25)
            self.button16.setGeometry(1010, 510, 80, 25)

            self.label9.setVisible(True)
            self.label9.setText("Usuarios Registrados")
            self.label10.setVisible(True)
            self.label10.setText("Libros registrados en la Biblioteca")
            self.label9.setGeometry(38, 60, 200, 20)
            self.label10.setGeometry(38, 350, 200, 20)
            self.button9.setVisible(True)
            self.button9.setGeometry(400, 20, 80, 20)

            if (self.label3.isEnabled() == True):
                self.label3.setVisible(True)
            if (self.tabla1.isEnabled() == True):
                self.tabla1.setVisible(True)
            if (self.tabla2.isEnabled() == True):
                self.tabla2.setVisible(True)

            mensaje1 = "Bienvenido " + self.nombreDelUsuario
            self.label3.setText(mensaje1)
            self.label3.setGeometry(250, 20, 200, 20)

            if (self.button13.isEnabled() == True):
                self.button13.setVisible(True)
            if (self.button14.isEnabled() == True):
                self.button14.setVisible(True)
            if (self.button15.isEnabled() == True):
                self.button15.setVisible(True)
            if (self.button16.isEnabled() == True):
                self.button16.setVisible(True)
            if (self.button17.isEnabled() == True):
                self.button17.setVisible(True)

        ##Login Usuario
        else:
            self.setMaximumSize(1200, 680)
            self.setMinimumSize(1200, 680)
            self.resize(1200, 680)
            self.move(0, 0)
            self.label4.hide()
            self.label8.hide()

            self.button5.hide()
            self.button6.hide()
            # self.button8.setVisible(True)
            self.button9.setVisible(True)
            self.button10.setVisible(True)
            self.button21.setVisible(True)
            self.button8.setGeometry(1000, 165, 90, 25)
            self.button9.setGeometry(400, 20, 80, 20)
            self.button10.setGeometry(1000, 405, 80, 25)
            self.button21.setGeometry(1000, 115, 90, 25)

            self.lineEdit9.setGeometry(1000, 440, 160, 20)
            self.lineEdit9.setVisible(True)

            if (self.label3.isEnabled() == True):
                self.label3.setVisible(True)

            mensaje1 = "Bienvenido " + self.nombreDelUsuario
            self.label3.setText(mensaje1)
            self.label3.setGeometry(250, 20, 200, 20)
            self.label9.setVisible(True)
            self.label10.setVisible(True)
            self.label9.setGeometry(38, 60, 200, 20)
            self.label10.setGeometry(38, 350, 200, 20)
            self.label9.setText("Mis prestamos de libros")
            self.label10.setText("Libros disponibles en la Biblioteca")

            if (self.tabla2.isEnabled() == True):
                self.tabla2.setVisible(True)

            if (self.tabla3.isEnabled() == True):
                self.tabla3.setVisible(True)

    def registrandoNuevoUsuario(self):

        if (
                self.lineEdit1.text() != "" and self.lineEdit8.text() != "" and self.lineEdit3.text() != "" and self.lineEdit4.text() != "" and self.lineEdit5.text() != "" and self.lineEdit6.text() != ""):
            nombreUsuario = str(self.lineEdit1.text())
            contrasenaUsuario = str(self.lineEdit8.text())
            direccionUsuario = str(self.lineEdit3.text())
            estadoUsuario = str(self.lineEdit5.text())
            correoUsuario = str(self.lineEdit6.text())
            municipioUsuario = str(self.lineEdit4.text())
            self.cursor.execute(
                """INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES('%s','%s','%s','%s','%s','%s')""" % (
                nombreUsuario, direccionUsuario, municipioUsuario, estadoUsuario, correoUsuario, contrasenaUsuario))
            self.conn.commit()
            self.registroCorrecto()
            # self.cargarVentanaInicial()

    def listarUsuarios(self):

        self.cursor.close()
        self.conn.close()
        self.conn = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * from usuario")
        renglon = self.cursor.fetchall()
        self.tabla1.setRowCount(len(renglon))

        i = 0
        j = 0

        while (i < len(renglon)):
            j = 0
            while (j < 7):
                data = str(renglon[i][j])
                self.tabla1.setItem(i, j, QtWidgets.QTableWidgetItem(data))
                self.tabla1.item(i, j).setTextAlignment(1012)

                j = j + 1
            i = i + 1

    def listarLibros(self):

        self.cursor.close()
        self.conn.close()
        self.conn = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * from libro")
        renglon = self.cursor.fetchall()
        self.tabla2.setRowCount(len(renglon))
        i = 0
        j = 0

        while (i < len(renglon)):
            j = 0
            while (j < 7):
                data = str(renglon[i][j])
                self.tabla2.setItem(i, j, QtWidgets.QTableWidgetItem(data))
                self.tabla2.item(i, j).setTextAlignment(1012)
                j = j + 1
            i = i + 1

    def registroCorrecto(self):

        self.label1.hide()
        self.label2.hide()
        self.label4.hide()
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.lineEdit1.hide()
        self.lineEdit2.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit7.hide()
        self.lineEdit8.hide()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button6.hide()
        self.button7.setVisible(True)
        self.setMaximumSize(250, 100)
        self.setMinimumSize(250, 100)
        self.resize(250, 100)
        self.move(500, 250)
        self.label3.move(90, 15)
        self.label3.setText("Registro Correcto")
        self.button7.setVisible(True)
        self.button7.move(86, 50)

    def autorizandoPrestamo(self):

        i = 0
        j = 0
        k = 0
        loTiene = 0

        idUsuario = int(self.tabla1.item(self.tabla1.currentRow(), 0).text())
        idLibro = int(self.tabla2.item(self.tabla2.currentRow(), 0).text())

        self.cursor.execute("SELECT * from prestamo")
        DatosPrestamo = self.cursor.fetchall()

        self.cursor.execute("SELECT * from usuario")
        DatosUsuario = self.cursor.fetchall()

        for j in range(len(DatosUsuario)):
            if (DatosUsuario[j][0] == idUsuario):
                break

        self.cursor.execute("SELECT * from libro ")
        DatosLibro = self.cursor.fetchall()

        for i in range(len(DatosLibro)):
            if (idLibro == DatosLibro[i][0]):

                for k in range(len(DatosPrestamo)):
                    if (DatosUsuario[j][0] == DatosPrestamo[k][0]):
                        if (DatosLibro[i][0] == DatosPrestamo[k][1]):
                            self.errorLoTiene()
                            loTiene = 1
                            break

                if (DatosLibro[i][6] >= 1 and loTiene == 0):
                    self.cursor.execute("""INSERT INTO prestamo (usuario_id, libro_id) VALUES(%d,%d)""" % (
                    int(DatosUsuario[j][0]), int(DatosLibro[i][0])))
                    self.conn.commit()
                    self.cursor.execute("UPDATE libro set disponibles = %d WHERE libro_id = %d" % (
                    int(DatosLibro[i][6] - 1), int(DatosLibro[i][0])))
                    self.conn.commit()
                    self.movimientoExitoso()
                    break

                elif (loTiene == 0):
                    self.errorNoHayDisponibles()
                    break

    def devolviendoPrestamo(self):

        i = 0
        j = 0
        k = 0
        loTiene = 0

        idUsuario = int(self.tabla1.item(self.tabla1.currentRow(), 0).text())
        idLibro = int(self.tabla2.item(self.tabla2.currentRow(), 0).text())

        self.cursor.execute("SELECT * from prestamo")
        DatosPrestamo = self.cursor.fetchall()

        self.cursor.execute("SELECT * from usuario")
        DatosUsuario = self.cursor.fetchall()

        for j in range(len(DatosUsuario)):
            if (DatosUsuario[j][0] == idUsuario):
                break

        self.cursor.execute("SELECT * from libro ")
        DatosLibro = self.cursor.fetchall()

        for i in range(len(DatosLibro)):
            if (idLibro == DatosLibro[i][0]):

                for k in range(len(DatosPrestamo)):
                    if (DatosUsuario[j][0] == DatosPrestamo[k][0]):
                        if (DatosLibro[i][0] == DatosPrestamo[k][1]):
                            self.cursor.execute("DELETE FROM prestamo WHERE usuario_id=%d AND libro_id=%d" % (
                            int(DatosUsuario[j][0]), int(DatosLibro[i][0])))
                            loTiene = 1
                            self.conn.commit()
                            self.cursor.execute("UPDATE libro set disponibles = %d WHERE libro_id = %d" % (
                            int(DatosLibro[i][6] + 1), int(DatosLibro[i][0])))
                            self.conn.commit()
                            self.movimientoExitoso()
                            break

        if (loTiene == 0):
            self.errorNoLoTiene()

    def agregandoLibro(self):
        self.button18.setVisible(True)
        if (self.button18.isEnabled() == True):
            self.button18.setVisible(True)

        self.tabla2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tabla2.setRowCount(self.tabla2.rowCount() + 1)

    def modificandoLibro(self):
        self.button19.setVisible(True)
        if (self.button19.isEnabled() == True):
            self.button19.setVisible(True)
        self.tabla2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)

    def agregarNuevoLibro(self):
        self.tabla2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        dato2 = str(self.tabla2.item(self.tabla2.currentRow(), 1).text())
        dato3 = str(self.tabla2.item(self.tabla2.currentRow(), 2).text())
        dato4 = int(self.tabla2.item(self.tabla2.currentRow(), 3).text())
        dato5 = int(self.tabla2.item(self.tabla2.currentRow(), 4).text())
        dato6 = str(self.tabla2.item(self.tabla2.currentRow(), 5).text())
        dato7 = int(self.tabla2.item(self.tabla2.currentRow(), 6).text())

        self.cursor.execute(
            """INSERT INTO libro (nombre, autor, edicion, ano, editorial, disponibles) VALUES('%s','%s',%d,%d,'%s',%d)""" % (
            dato2, dato3, dato4, dato5, dato6, dato7))
        self.conn.commit()
        self.button18.hide()
        self.movimientoExitoso()

    def agregarCambiosLibro(self):
        self.tabla2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        dato1 = int(self.tabla2.item(self.tabla2.currentRow(), 0).text())
        dato2 = str(self.tabla2.item(self.tabla2.currentRow(), 1).text())
        dato3 = str(self.tabla2.item(self.tabla2.currentRow(), 2).text())
        dato4 = int(self.tabla2.item(self.tabla2.currentRow(), 3).text())
        dato5 = int(self.tabla2.item(self.tabla2.currentRow(), 4).text())
        dato6 = str(self.tabla2.item(self.tabla2.currentRow(), 5).text())
        dato7 = int(self.tabla2.item(self.tabla2.currentRow(), 6).text())
        self.cursor.execute(
            "UPDATE libro set nombre = '%s',autor='%s',edicion=%d,ano=%d,editorial='%s',disponibles=%d  WHERE libro_id = %d" % (
            dato2, dato3, dato4, dato5, dato6, dato7, dato1))
        self.conn.commit()
        self.button19.hide()
        self.movimientoExitoso()

    def movimientoExitoso(self):

        self.setMaximumSize(250, 100)
        self.setMinimumSize(250, 100)
        self.resize(250, 100)
        self.center()

        self.label14.setVisible(True)
        self.button20.setVisible(True)

        self.button6.hide()
        self.button9.hide()

        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()

        self.tabla1.hide()
        self.tabla2.hide()

        self.label10.hide()
        self.label9.hide()
        self.label3.hide()

    def errorLoTiene(self):

        self.setMaximumSize(250, 100)
        self.setMinimumSize(250, 100)
        self.resize(250, 100)
        self.center()

        self.label15.setVisible(True)
        self.button20.setVisible(True)

        self.button6.hide()
        self.button9.hide()

        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()

        self.tabla1.hide()
        self.tabla2.hide()

        self.label10.hide()
        self.label9.hide()
        self.label3.hide()

    def errorNoLoTiene(self):

        self.setMaximumSize(250, 100)
        self.setMinimumSize(250, 100)
        self.resize(250, 100)
        self.center()

        self.label16.setVisible(True)
        self.button20.setVisible(True)

        self.button6.hide()
        self.button9.hide()

        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()

        self.tabla1.hide()
        self.tabla2.hide()

        self.label10.hide()
        self.label9.hide()
        self.label3.hide()

    def errorNoHayDisponibles(self):

        self.setMaximumSize(250, 100)
        self.setMinimumSize(250, 100)
        self.resize(250, 100)
        self.center()

        self.label17.setVisible(True)
        self.button20.setVisible(True)

        self.button6.hide()
        self.button9.hide()

        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.button17.hide()

        self.tabla1.hide()
        self.tabla2.hide()

        self.label10.hide()
        self.label9.hide()
        self.label3.hide()

    def aceptarMovimiento(self):

        self.label14.hide()
        self.label15.hide()
        self.label16.hide()
        self.label17.hide()
        self.button20.hide()
        self.interfazBaseDatos()

    def verMisLibrosUsuarioNormal(self):

        self.cursor.close()
        self.conn.close()
        self.conn = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT usuario_id FROM usuario WHERE username='%s' " % (str(self.nombreDelUsuario)))
        idDelusuario = self.cursor.fetchall()

        self.cursor.execute("SELECT libro_id from prestamo WHERE usuario_id = %d" % (idDelusuario[0][0]))
        idsLibros = self.cursor.fetchall()

        self.cursor.execute("SELECT * from libro")
        renglon = self.cursor.fetchall()

        self.tabla3.setRowCount(len(idsLibros))
        i = 0
        j = 0
        k = 0
        renglonCount = 0

        for j in range(len(renglon)):
            for i in range(len(idsLibros)):
                if (renglon[j][0] == idsLibros[i][0]):
                    for k in range(6):
                        data = str(renglon[j][k])
                        self.tabla3.setItem(renglonCount, k, QtWidgets.QTableWidgetItem(data))
                        self.tabla3.item(renglonCount, k).setTextAlignment(1012)

                    renglonCount = renglonCount + 1

    def buscarLibro(self):

        texto = "%" + self.lineEdit9.text() + "%"
        self.cursor.execute(
            "SELECT * from libro WHERE UPPER(nombre) LIKE '%s' OR UPPER(autor) LIKE '%s' " % (texto, texto))
        renglon = self.cursor.fetchall()

        i = 0
        j = 0
        renglonCount = 0
        self.tabla2.setRowCount(0)

        for i in range(len(renglon)):

            filas = self.tabla2.rowCount() + 1
            self.tabla2.setRowCount(filas)

            for j in range(7):
                data = str(renglon[i][j])
                self.tabla2.setItem(renglonCount, j, QtWidgets.QTableWidgetItem(data))
                self.tabla2.item(renglonCount, j).setTextAlignment(1012)

            renglonCount = renglonCount + 1

    def setWindowTitle(self, param: object) -> object:
        pass


app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec_())
ventana.cursor.close()
ventana.conn.close()
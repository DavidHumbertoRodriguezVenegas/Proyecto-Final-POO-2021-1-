# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_afiliado.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_view_afiliado(object):
    def setupUi(self, view_afiliado):
        view_afiliado.setObjectName("view_afiliado")
        view_afiliado.resize(800, 600)
        view_afiliado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(view_afiliado)
        self.centralwidget.setObjectName("centralwidget")
        self.line_ide = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ide.setGeometry(QtCore.QRect(220, 180, 151, 20))
        self.line_ide.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_ide.setMaxLength(12)
        self.line_ide.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_ide.setReadOnly(True)
        self.line_ide.setObjectName("line_ide")
        self.line_apellido = QtWidgets.QLineEdit(self.centralwidget)
        self.line_apellido.setGeometry(QtCore.QRect(330, 260, 151, 20))
        self.line_apellido.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_apellido.setMaxLength(60)
        self.line_apellido.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_apellido.setReadOnly(True)
        self.line_apellido.setObjectName("line_apellido")
        self.line_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nombre.setGeometry(QtCore.QRect(140, 260, 151, 20))
        self.line_nombre.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_nombre.setMaxLength(60)
        self.line_nombre.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_nombre.setReadOnly(True)
        self.line_nombre.setObjectName("line_nombre")
        self.line_direccion = QtWidgets.QLineEdit(self.centralwidget)
        self.line_direccion.setGeometry(QtCore.QRect(520, 260, 151, 20))
        self.line_direccion.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_direccion.setMaxLength(60)
        self.line_direccion.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_direccion.setReadOnly(True)
        self.line_direccion.setObjectName("line_direccion")
        self.line_correo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_correo.setGeometry(QtCore.QRect(140, 330, 151, 20))
        self.line_correo.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_correo.setMaxLength(60)
        self.line_correo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_correo.setReadOnly(True)
        self.line_correo.setObjectName("line_correo")
        self.line_telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.line_telefono.setGeometry(QtCore.QRect(330, 330, 151, 20))
        self.line_telefono.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_telefono.setMaxLength(60)
        self.line_telefono.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_telefono.setReadOnly(True)
        self.line_telefono.setObjectName("line_telefono")
        self.line_ciudad = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ciudad.setGeometry(QtCore.QRect(520, 330, 151, 20))
        self.line_ciudad.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_ciudad.setMaxLength(60)
        self.line_ciudad.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_ciudad.setReadOnly(True)
        self.line_ciudad.setObjectName("line_ciudad")
        self.line_nacimiento = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nacimiento.setGeometry(QtCore.QRect(140, 400, 151, 20))
        self.line_nacimiento.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_nacimiento.setMaxLength(60)
        self.line_nacimiento.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_nacimiento.setReadOnly(True)
        self.line_nacimiento.setObjectName("line_nacimiento")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 111))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 81, 181);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre.setGeometry(QtCore.QRect(140, 240, 151, 16))
        self.label_nombre.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nombre.setObjectName("label_nombre")
        self.label_telefono = QtWidgets.QLabel(self.centralwidget)
        self.label_telefono.setGeometry(QtCore.QRect(330, 310, 151, 16))
        self.label_telefono.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_telefono.setAlignment(QtCore.Qt.AlignCenter)
        self.label_telefono.setObjectName("label_telefono")
        self.label_nacimiento = QtWidgets.QLabel(self.centralwidget)
        self.label_nacimiento.setGeometry(QtCore.QRect(140, 380, 151, 16))
        self.label_nacimiento.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_nacimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.label_ide = QtWidgets.QLabel(self.centralwidget)
        self.label_ide.setGeometry(QtCore.QRect(220, 160, 151, 16))
        self.label_ide.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_ide.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ide.setObjectName("label_ide")
        self.label_direccion = QtWidgets.QLabel(self.centralwidget)
        self.label_direccion.setGeometry(QtCore.QRect(520, 240, 151, 16))
        self.label_direccion.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_direccion.setObjectName("label_direccion")
        self.label_ciudad = QtWidgets.QLabel(self.centralwidget)
        self.label_ciudad.setGeometry(QtCore.QRect(520, 310, 151, 16))
        self.label_ciudad.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_ciudad.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ciudad.setObjectName("label_ciudad")
        self.label_correo = QtWidgets.QLabel(self.centralwidget)
        self.label_correo.setGeometry(QtCore.QRect(140, 310, 151, 16))
        self.label_correo.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_correo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_correo.setObjectName("label_correo")
        self.label_apellido = QtWidgets.QLabel(self.centralwidget)
        self.label_apellido.setGeometry(QtCore.QRect(330, 240, 151, 16))
        self.label_apellido.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_apellido.setAlignment(QtCore.Qt.AlignCenter)
        self.label_apellido.setObjectName("label_apellido")
        self.label_vacunacion = QtWidgets.QLabel(self.centralwidget)
        self.label_vacunacion.setGeometry(QtCore.QRect(220, 460, 151, 16))
        self.label_vacunacion.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_vacunacion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vacunacion.setObjectName("label_vacunacion")
        self.line_vacunado = QtWidgets.QLineEdit(self.centralwidget)
        self.line_vacunado.setGeometry(QtCore.QRect(220, 480, 151, 20))
        self.line_vacunado.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_vacunado.setMaxLength(60)
        self.line_vacunado.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_vacunado.setReadOnly(True)
        self.line_vacunado.setObjectName("line_vacunado")
        self.label_edad = QtWidgets.QLabel(self.centralwidget)
        self.label_edad.setGeometry(QtCore.QRect(330, 380, 151, 16))
        self.label_edad.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_edad.setAlignment(QtCore.Qt.AlignCenter)
        self.label_edad.setObjectName("label_edad")
        self.line_edad = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edad.setGeometry(QtCore.QRect(330, 400, 151, 20))
        self.line_edad.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_edad.setMaxLength(60)
        self.line_edad.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_edad.setReadOnly(True)
        self.line_edad.setObjectName("line_edad")
        self.line_plan = QtWidgets.QLineEdit(self.centralwidget)
        self.line_plan.setGeometry(QtCore.QRect(410, 180, 151, 20))
        self.line_plan.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_plan.setMaxLength(12)
        self.line_plan.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_plan.setReadOnly(True)
        self.line_plan.setObjectName("line_plan")
        self.label_plan = QtWidgets.QLabel(self.centralwidget)
        self.label_plan.setGeometry(QtCore.QRect(410, 160, 151, 16))
        self.label_plan.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_plan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plan.setObjectName("label_plan")
        self.line_afiliacion = QtWidgets.QLineEdit(self.centralwidget)
        self.line_afiliacion.setGeometry(QtCore.QRect(520, 400, 151, 20))
        self.line_afiliacion.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_afiliacion.setText("")
        self.line_afiliacion.setMaxLength(60)
        self.line_afiliacion.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_afiliacion.setReadOnly(True)
        self.line_afiliacion.setObjectName("line_afiliacion")
        self.label_afiliacion = QtWidgets.QLabel(self.centralwidget)
        self.label_afiliacion.setGeometry(QtCore.QRect(520, 380, 151, 16))
        self.label_afiliacion.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_afiliacion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_afiliacion.setObjectName("label_afiliacion")
        self.line_desafiliacion = QtWidgets.QLineEdit(self.centralwidget)
        self.line_desafiliacion.setGeometry(QtCore.QRect(410, 480, 151, 20))
        self.line_desafiliacion.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.line_desafiliacion.setText("")
        self.line_desafiliacion.setMaxLength(60)
        self.line_desafiliacion.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.line_desafiliacion.setReadOnly(True)
        self.line_desafiliacion.setObjectName("line_desafiliacion")
        self.label_desafil = QtWidgets.QLabel(self.centralwidget)
        self.label_desafil.setGeometry(QtCore.QRect(410, 460, 151, 16))
        self.label_desafil.setStyleSheet("color: rgb(116, 116, 116);")
        self.label_desafil.setAlignment(QtCore.Qt.AlignCenter)
        self.label_desafil.setObjectName("label_desafil")
        self.push_regresar = QtWidgets.QPushButton(self.centralwidget)
        self.push_regresar.setGeometry(QtCore.QRect(30, 40, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.push_regresar.setFont(font)
        self.push_regresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_regresar.setStyleSheet("color: rgb(63, 81, 181);\n"
"border-style: solid;\n"
"background-color:rgb(255, 255, 255) ;\n"
"border-color:rgb(63, 81, 181);\n"
"border-width: 2px;\n"
"border-radius: 10px;")
        self.push_regresar.setObjectName("push_regresar")
        view_afiliado.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(view_afiliado)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        view_afiliado.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(view_afiliado)
        self.statusbar.setObjectName("statusbar")
        view_afiliado.setStatusBar(self.statusbar)

        self.retranslateUi(view_afiliado)
        QtCore.QMetaObject.connectSlotsByName(view_afiliado)

    def retranslateUi(self, view_afiliado):
        _translate = QtCore.QCoreApplication.translate
        view_afiliado.setWindowTitle(_translate("view_afiliado", "Consultar Afiliado"))
        self.label.setText(_translate("view_afiliado", "CONSULTAR AFILIADO"))
        self.label_nombre.setText(_translate("view_afiliado", "Nombre"))
        self.label_telefono.setText(_translate("view_afiliado", "Telefono"))
        self.label_nacimiento.setText(_translate("view_afiliado", "Fecha de Nacimiento"))
        self.label_ide.setText(_translate("view_afiliado", "Numero de identificación"))
        self.label_direccion.setText(_translate("view_afiliado", "Dirección"))
        self.label_ciudad.setText(_translate("view_afiliado", "Ciudad de Residencia"))
        self.label_correo.setText(_translate("view_afiliado", "Correo"))
        self.label_apellido.setText(_translate("view_afiliado", "Apellido"))
        self.label_vacunacion.setText(_translate("view_afiliado", "Vacunado"))
        self.label_edad.setText(_translate("view_afiliado", "Edad"))
        self.label_plan.setText(_translate("view_afiliado", "Plan Asignado"))
        self.label_afiliacion.setText(_translate("view_afiliado", "Fecha De Afiliación"))
        self.label_desafil.setText(_translate("view_afiliado", "Fecha De Desafiliación"))
        self.push_regresar.setText(_translate("view_afiliado", "Regresar"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_lote.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crear_lote(object):
    def setupUi(self, crear_lote):
        crear_lote.setObjectName("crear_lote")
        crear_lote.resize(831, 554)
        crear_lote.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(crear_lote)
        self.centralwidget.setObjectName("centralwidget")
        self.label_no_lote = QtWidgets.QLabel(self.centralwidget)
        self.label_no_lote.setGeometry(QtCore.QRect(150, 290, 91, 21))
        self.label_no_lote.setObjectName("label_no_lote")
        self.lineEdit_no_lote = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_no_lote.setGeometry(QtCore.QRect(110, 310, 161, 21))
        self.lineEdit_no_lote.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_no_lote.setMaxLength(10)
        self.lineEdit_no_lote.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_lote.setObjectName("lineEdit_no_lote")
        self.lineEdit_cant_recibida = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cant_recibida.setGeometry(QtCore.QRect(410, 120, 171, 21))
        self.lineEdit_cant_recibida.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_cant_recibida.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cant_recibida.setObjectName("lineEdit_cant_recibida")
        self.calendarWidget_fechav = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_fechav.setGeometry(QtCore.QRect(450, 320, 312, 183))
        self.calendarWidget_fechav.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget_fechav.setObjectName("calendarWidget_fechav")
        self.lineEdit_Titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Titulo.setGeometry(QtCore.QRect(0, 0, 831, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_Titulo.setFont(font)
        self.lineEdit_Titulo.setStyleSheet("background-color: rgb(63, 81, 181);\n"
"\n"
"font: 75 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Titulo.setReadOnly(True)
        self.lineEdit_Titulo.setObjectName("lineEdit_Titulo")
        self.comboBox_fabricante = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_fabricante.setGeometry(QtCore.QRect(110, 410, 161, 22))
        self.comboBox_fabricante.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.comboBox_fabricante.setObjectName("comboBox_fabricante")
        self.label_cant_recibida = QtWidgets.QLabel(self.centralwidget)
        self.label_cant_recibida.setGeometry(QtCore.QRect(450, 90, 101, 20))
        self.label_cant_recibida.setObjectName("label_cant_recibida")
        self.lineEdit_fecha_ven = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fecha_ven.setGeometry(QtCore.QRect(110, 360, 161, 21))
        self.lineEdit_fecha_ven.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_fecha_ven.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_fecha_ven.setReadOnly(True)
        self.lineEdit_fecha_ven.setObjectName("lineEdit_fecha_ven")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 340, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_tipo_vac = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tipo_vac.setGeometry(QtCore.QRect(410, 190, 171, 20))
        self.lineEdit_tipo_vac.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_tipo_vac.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tipo_vac.setReadOnly(True)
        self.lineEdit_tipo_vac.setObjectName("lineEdit_tipo_vac")
        self.lineEdit_nodosis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nodosis.setGeometry(QtCore.QRect(600, 120, 181, 20))
        self.lineEdit_nodosis.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_nodosis.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nodosis.setReadOnly(True)
        self.lineEdit_nodosis.setObjectName("lineEdit_nodosis")
        self.lineEdit_temperatura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_temperatura.setGeometry(QtCore.QRect(410, 260, 171, 20))
        self.lineEdit_temperatura.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_temperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_temperatura.setReadOnly(True)
        self.lineEdit_temperatura.setObjectName("lineEdit_temperatura")
        self.lineEdit_efectividad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_efectividad.setGeometry(QtCore.QRect(600, 260, 181, 20))
        self.lineEdit_efectividad.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_efectividad.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_efectividad.setReadOnly(True)
        self.lineEdit_efectividad.setObjectName("lineEdit_efectividad")
        self.lineEdit_proteccion = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_proteccion.setGeometry(QtCore.QRect(600, 190, 181, 20))
        self.lineEdit_proteccion.setStyleSheet("border-width: 2px; \n"
"border-style: solid; \n"
"border-color: white white rgb(233, 30, 99) white;")
        self.lineEdit_proteccion.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_proteccion.setReadOnly(True)
        self.lineEdit_proteccion.setObjectName("lineEdit_proteccion")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 160, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 230, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 230, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 160, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 390, 61, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 30, 101, 21))
        self.pushButton.setStyleSheet("color: rgb(63, 81, 181);\n"
"border-style: solid;\n"
"background-color:rgb(255, 255, 255) ;\n"
"border-color:rgb(63, 81, 181);\n"
"border-width: 2px;\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_regre = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_regre.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.pushButton_regre.setStyleSheet("color: rgb(63, 81, 181);\n"
"border-style: solid;\n"
"background-color:rgb(255, 255, 255) ;\n"
"border-color:rgb(63, 81, 181);\n"
"border-width: 2px;\n"
"border-radius: 10px;")
        self.pushButton_regre.setObjectName("pushButton_regre")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 90, 251, 421))
        self.label_8.setStyleSheet("border-image: url(:/vacuna/vacuna.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lineEdit_cant_recibida.raise_()
        self.calendarWidget_fechav.raise_()
        self.lineEdit_Titulo.raise_()
        self.label_cant_recibida.raise_()
        self.lineEdit_tipo_vac.raise_()
        self.lineEdit_nodosis.raise_()
        self.lineEdit_temperatura.raise_()
        self.lineEdit_efectividad.raise_()
        self.lineEdit_proteccion.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_regre.raise_()
        self.label_8.raise_()
        self.lineEdit_no_lote.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.comboBox_fabricante.raise_()
        self.lineEdit_fecha_ven.raise_()
        self.label_no_lote.raise_()
        crear_lote.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(crear_lote)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        crear_lote.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(crear_lote)
        self.statusbar.setObjectName("statusbar")
        crear_lote.setStatusBar(self.statusbar)

        self.retranslateUi(crear_lote)
        QtCore.QMetaObject.connectSlotsByName(crear_lote)

    def retranslateUi(self, crear_lote):
        _translate = QtCore.QCoreApplication.translate
        crear_lote.setWindowTitle(_translate("crear_lote", "Crear un lote"))
        self.label_no_lote.setText(_translate("crear_lote", "Número de lote"))
        self.lineEdit_Titulo.setText(_translate("crear_lote", "CREAR LOTE"))
        self.label_cant_recibida.setText(_translate("crear_lote", "Cantidad recibida"))
        self.label.setText(_translate("crear_lote", "Fecha de Vencimiento"))
        self.label_2.setText(_translate("crear_lote", "Tipo de Vacuna"))
        self.label_3.setText(_translate("crear_lote", "Número de dosis"))
        self.label_4.setText(_translate("crear_lote", "Temperatura"))
        self.label_5.setText(_translate("crear_lote", "Efectividad"))
        self.label_6.setText(_translate("crear_lote", "Protección"))
        self.label_7.setText(_translate("crear_lote", "Fabricante"))
        self.pushButton.setText(_translate("crear_lote", "Guardar"))
        self.pushButton_regre.setText(_translate("crear_lote", "Regresar"))
import vacuna

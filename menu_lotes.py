# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuLotes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_lotes(object):
    def setupUi(self, menu_lotes):
        menu_lotes.setObjectName("menu_lotes")
        menu_lotes.resize(571, 580)
        menu_lotes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(menu_lotes)
        self.centralwidget.setObjectName("centralwidget")
        self.push_crear_lote = QtWidgets.QPushButton(self.centralwidget)
        self.push_crear_lote.setGeometry(QtCore.QRect(150, 170, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_crear_lote.setFont(font)
        self.push_crear_lote.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"border: 2px groove gray;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(63,81,181);\n"
"color: rgb(63,81,181);")
        self.push_crear_lote.setObjectName("push_crear_lote")
        self.push_consultar_lote = QtWidgets.QPushButton(self.centralwidget)
        self.push_consultar_lote.setGeometry(QtCore.QRect(150, 230, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_consultar_lote.setFont(font)
        self.push_consultar_lote.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"border: 2px groove gray;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(63,81,181);\n"
"color: rgb(63,81,181);")
        self.push_consultar_lote.setObjectName("push_consultar_lote")
        self.push_editar_lote = QtWidgets.QPushButton(self.centralwidget)
        self.push_editar_lote.setGeometry(QtCore.QRect(150, 350, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_editar_lote.setFont(font)
        self.push_editar_lote.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"border: 2px groove gray;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(63,81,181);\n"
"color: rgb(63,81,181);")
        self.push_editar_lote.setObjectName("push_editar_lote")
        self.push_regresar = QtWidgets.QPushButton(self.centralwidget)
        self.push_regresar.setGeometry(QtCore.QRect(150, 410, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_regresar.setFont(font)
        self.push_regresar.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"border: 2px groove gray;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(63,81,181);\n"
"color: rgb(63,81,181);")
        self.push_regresar.setObjectName("push_regresar")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(-40, 0, 661, 81))
        self.label_titulo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("\n"
"font: 26pt \"Tahoma\";\n"
"background-color: rgb(63,81,181);\n"
"color: rgb(255,255,255);")
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.push_consulta_general = QtWidgets.QPushButton(self.centralwidget)
        self.push_consulta_general.setGeometry(QtCore.QRect(150, 290, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_consulta_general.setFont(font)
        self.push_consulta_general.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;\n"
"border: 2px groove gray;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(63,81,181);\n"
"color: rgb(63,81,181);")
        self.push_consulta_general.setObjectName("push_consulta_general")
        menu_lotes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_lotes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.menubar.setObjectName("menubar")
        menu_lotes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_lotes)
        self.statusbar.setObjectName("statusbar")
        menu_lotes.setStatusBar(self.statusbar)

        self.retranslateUi(menu_lotes)
        QtCore.QMetaObject.connectSlotsByName(menu_lotes)

    def retranslateUi(self, menu_lotes):
        _translate = QtCore.QCoreApplication.translate
        menu_lotes.setWindowTitle(_translate("menu_lotes", "Menu modulo de afiliados"))
        self.push_crear_lote.setText(_translate("menu_lotes", "Crear lote"))
        self.push_consultar_lote.setText(_translate("menu_lotes", "Consulta individual lote"))
        self.push_editar_lote.setText(_translate("menu_lotes", "Editar lote"))
        self.push_regresar.setText(_translate("menu_lotes", "Regresar"))
        self.label_titulo.setText(_translate("menu_lotes", "MENU DE LOTES"))
        self.push_consulta_general.setText(_translate("menu_lotes", "Consulta general lote"))

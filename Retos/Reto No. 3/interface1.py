# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from HodgkinHuxley import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VoltajeEntradaSlicer = QtWidgets.QSlider(self.centralwidget)
        self.VoltajeEntradaSlicer.setGeometry(QtCore.QRect(110, 90, 160, 16))
        self.VoltajeEntradaSlicer.setOrientation(QtCore.Qt.Horizontal)
        self.VoltajeEntradaSlicer.setObjectName("VoltajeEntradaSlicer")
        self.Recuperacionslicer = QtWidgets.QSlider(self.centralwidget)
        self.Recuperacionslicer.setGeometry(QtCore.QRect(110, 130, 160, 16))
        self.Recuperacionslicer.setOrientation(QtCore.Qt.Horizontal)
        self.Recuperacionslicer.setObjectName("Recuperacionslicer")
        self.ButtomAdams = QtWidgets.QPushButton(self.centralwidget)
        self.ButtomAdams.setGeometry(QtCore.QRect(10, 360, 81, 31))
        self.ButtomAdams.setObjectName("ButtomAdams")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.ButtomAdams.clicked.connect(self.graficarAdams)
        self.label.setGeometry(QtCore.QRect(20, 70, 81, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 390, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CorrienteInicioSlicer = QtWidgets.QSlider(self.centralwidget)
        self.CorrienteInicioSlicer.setGeometry(QtCore.QRect(110, 170, 160, 16))
        self.CorrienteInicioSlicer.setOrientation(QtCore.Qt.Horizontal)
        self.CorrienteInicioSlicer.setObjectName("CorrienteInicioSlicer")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 81, 16))
        self.label_3.setObjectName("label_3")
        self.CorrienteFinalSilicer = QtWidgets.QSlider(self.centralwidget)
        self.CorrienteFinalSilicer.setGeometry(QtCore.QRect(110, 210, 160, 16))
        self.CorrienteFinalSilicer.setOrientation(QtCore.Qt.Horizontal)
        self.CorrienteFinalSilicer.setObjectName("CorrienteFinalSilicer")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 71, 16))
        self.label_4.setObjectName("label_4")
        self.CapacitanciaSlicer = QtWidgets.QSlider(self.centralwidget)
        self.CapacitanciaSlicer.setGeometry(QtCore.QRect(110, 250, 160, 16))
        self.CapacitanciaSlicer.setOrientation(QtCore.Qt.Horizontal)
        self.CapacitanciaSlicer.setObjectName("CapacitanciaSlicer")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 61, 16))
        self.label_5.setObjectName("label_5")
        self.TrecuperacionSlicer = QtWidgets.QSlider(self.centralwidget)
        self.TrecuperacionSlicer.setGeometry(QtCore.QRect(110, 290, 160, 16))
        self.TrecuperacionSlicer.setOrientation(QtCore.Qt.Horizontal)
        self.TrecuperacionSlicer.setObjectName("TrecuperacionSlicer")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 101, 16))
        self.label_6.setObjectName("label_6")
        self.VentradaLabel = QtWidgets.QLabel(self.centralwidget)
        self.VentradaLabel.setGeometry(QtCore.QRect(280, 90, 39, 11))
        self.VentradaLabel.setText("")
        self.VentradaLabel.setObjectName("VentradaLabel")
        self.RecuperacionLabel = QtWidgets.QLabel(self.centralwidget)
        self.RecuperacionLabel.setGeometry(QtCore.QRect(280, 130, 39, 11))
        self.RecuperacionLabel.setText("")
        self.RecuperacionLabel.setObjectName("RecuperacionLabel")
        self.CorrInicioLabel = QtWidgets.QLabel(self.centralwidget)
        self.CorrInicioLabel.setGeometry(QtCore.QRect(280, 170, 39, 11))
        self.CorrInicioLabel.setText("")
        self.CorrInicioLabel.setObjectName("CorrInicioLabel")
        self.CorrienteFinalLabel = QtWidgets.QLabel(self.centralwidget)
        self.CorrienteFinalLabel.setGeometry(QtCore.QRect(280, 210, 39, 11))
        self.CorrienteFinalLabel.setText("")
        self.CorrienteFinalLabel.setObjectName("CorrienteFinalLabel")
        self.Capacitancialabel = QtWidgets.QLabel(self.centralwidget)
        self.Capacitancialabel.setGeometry(QtCore.QRect(280, 250, 39, 11))
        self.Capacitancialabel.setText("")
        self.Capacitancialabel.setObjectName("Capacitancialabel")
        self.TrecuperacionLabel = QtWidgets.QLabel(self.centralwidget)
        self.TrecuperacionLabel.setGeometry(QtCore.QRect(280, 290, 39, 11))
        self.TrecuperacionLabel.setText("")
        self.TrecuperacionLabel.setObjectName("TrecuperacionLabel")
        self.ButtonOde = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonOde.setGeometry(QtCore.QRect(100, 360, 81, 31))
        self.ButtonOde.setObjectName("ButtonOde")
        self.ButtonSimulacion = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonOde.clicked.connect(self.graficarrk)
        self.ButtonSimulacion.setGeometry(QtCore.QRect(200, 360, 71, 31))
        self.ButtonSimulacion.setObjectName("ButtonSimulacion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.ButtonSimulacion.clicked.connect(self.graficarSimulacion)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.VoltajeEntradaSlicer.valueChanged.connect(self.actualizarValores)
        self.Recuperacionslicer.valueChanged.connect(self.actualizarValores)
        self.CorrienteInicioSlicer.valueChanged.connect(self.actualizarValores)
        self.CorrienteFinalSilicer.valueChanged.connect(self.actualizarValores)
        self.CapacitanciaSlicer.valueChanged.connect(self.actualizarValores)
        self.TrecuperacionSlicer.valueChanged.connect(self.actualizarValores)

        self.CorrienteInicioSlicer.setMaximum(5)
        self.CorrienteFinalSilicer.setMaximum(15)
        self.CapacitanciaSlicer.setMaximum(15)
        self.TrecuperacionSlicer.setMaximum(15)
        self.TrecuperacionSlicer.setMinimum(1)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtomAdams.setText(_translate("MainWindow", "Graficar Rk"))
        self.label.setText(_translate("MainWindow", "Voltaje de entrada"))
        self.label_2.setText(_translate("MainWindow", "Recuperación"))
        self.label_3.setText(_translate("MainWindow", "Crriente de inicio"))
        self.label_4.setText(_translate("MainWindow", "Corriente Final"))
        self.label_5.setText(_translate("MainWindow", "Capacitancia"))
        self.label_6.setText(_translate("MainWindow", "Tiempo de recuperacion"))
        self.ButtonOde.setText(_translate("MainWindow", "Graficar con Adams"))
        self.ButtonSimulacion.setText(_translate("MainWindow", "Sumulacion"))
        self.actualizarValores()
    

    def actualizarValores(self):
        x= str(self.VoltajeEntradaSlicer.value()) + " V"
        self.VentradaLabel.setText(x)
        c= str(self.Recuperacionslicer.value())
        self.RecuperacionLabel.setText(c)
        d= str(self.CorrienteInicioSlicer.value()) + " uA"
        self.CorrInicioLabel.setText(d)
        #self.CorrienteInicioSlicer.setMinimum(self.CorrienteInicioSlicer.value())
        x =str(self.CorrienteFinalSilicer.value()) + " uA"
        self.CorrienteFinalLabel.setText(x)
        x =str(self.CapacitanciaSlicer.value()) + " uF"
        self.Capacitancialabel.setText(x)
        x =str(self.TrecuperacionSlicer.value()) + " ms"
        self.TrecuperacionLabel.setText(x)
        
    def establecerValores(self):
        h = Hodgkin()
        Iin = self.CorrienteInicioSlicer.value()
        Ifn = self.CorrienteFinalSilicer.value()
        C = self.CapacitanciaSlicer.value()
        taou  = self.TrecuperacionSlicer.value()
        Vin = self.VoltajeEntradaSlicer.value()
        Rin = self.Recuperacionslicer.value()
        h.establecer(Iin,Ifn,C,taou,Vin,Rin)
        return h

    def graficarSimulacion(self):
        h = self.establecerValores()
        h.graficarMovimiento()

    def graficarAdams(self):
        h = self.establecerValores()
        h.graficarOde()
    def graficarrk(self):
        h = self.establecerValores()
        h.graficarRK()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

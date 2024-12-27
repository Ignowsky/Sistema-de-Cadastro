from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Maquinas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        ##########################################################
        # TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.left_Menu)
        ##########################################################

        ##########################################################
        # Páginas do Sistema
        self.btn_Home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Home))
        self.btn_Cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Cadastrar))
        self.btn_Contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Contatos))
        self.btn_Sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Sobre))

    def left_Menu(self):
        width = self.left_Container.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.left_Container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


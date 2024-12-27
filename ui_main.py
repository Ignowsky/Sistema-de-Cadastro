# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastros.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import iconsrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(913, 627)
        MainWindow.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255,255,255);\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_Container = QFrame(self.centralwidget)
        self.left_Container.setObjectName(u"left_Container")
        self.left_Container.setMinimumSize(QSize(0, 0))
        self.left_Container.setMaximumSize(QSize(0, 16777215))
        self.left_Container.setFrameShape(QFrame.StyledPanel)
        self.left_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.left_Container)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_3 = QLabel(self.left_Container)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_Container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 9)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(131, 131, 131);\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"	background-color: rgb(131, 131, 131);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(179, 179, 179);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 63, 467))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_Home = QPushButton(self.page)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(11)
        self.btn_Home.setFont(font)
        self.btn_Home.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.verticalLayout_5.addWidget(self.btn_Home)

        self.btn_Cadastrar = QPushButton(self.page)
        self.btn_Cadastrar.setObjectName(u"btn_Cadastrar")
        self.btn_Cadastrar.setMinimumSize(QSize(0, 20))
        self.btn_Cadastrar.setFont(font)
        self.btn_Cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_Cadastrar)

        self.btn_Contatos = QPushButton(self.page)
        self.btn_Contatos.setObjectName(u"btn_Contatos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Contatos.sizePolicy().hasHeightForWidth())
        self.btn_Contatos.setSizePolicy(sizePolicy)
        self.btn_Contatos.setMinimumSize(QSize(0, 20))
        self.btn_Contatos.setFont(font)
        self.btn_Contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_Contatos)

        self.btn_Sobre = QPushButton(self.page)
        self.btn_Sobre.setObjectName(u"btn_Sobre")
        self.btn_Sobre.setMinimumSize(QSize(0, 20))
        self.btn_Sobre.setFont(font)
        self.btn_Sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_Sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 159, 467))
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_11.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.left_Container)

        self.main_Container = QFrame(self.centralwidget)
        self.main_Container.setObjectName(u"main_Container")
        self.main_Container.setFrameShape(QFrame.StyledPanel)
        self.main_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.main_Container)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_Container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu-principal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_Frame = QFrame(self.main_Container)
        self.main_Frame.setObjectName(u"main_Frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_Frame.sizePolicy().hasHeightForWidth())
        self.main_Frame.setSizePolicy(sizePolicy1)
        self.main_Frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_Frame.setFrameShape(QFrame.StyledPanel)
        self.main_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_Frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_Frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_Home = QWidget()
        self.pg_Home.setObjectName(u"pg_Home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_Home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.pg_Home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(62, 62, 62);")

        self.verticalLayout_7.addWidget(self.label_5)

        self.Pages.addWidget(self.pg_Home)
        self.pg_Cadastrar = QWidget()
        self.pg_Cadastrar.setObjectName(u"pg_Cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_Cadastrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_Cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252,252,252);\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_15 = QVBoxLayout(self.tab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(149, 149, 149);\n"
"	font: 10px \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QLineEdit:placeholder {\n"
"	\n"
"	color: rgb(187, 187, 187);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_SistemaOperacional = QLineEdit(self.frame_4)
        self.txt_SistemaOperacional.setObjectName(u"txt_SistemaOperacional")
        self.txt_SistemaOperacional.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_SistemaOperacional, 5, 1, 1, 1)

        self.txt_Licenciado = QLineEdit(self.frame_4)
        self.txt_Licenciado.setObjectName(u"txt_Licenciado")
        self.txt_Licenciado.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Licenciado, 5, 2, 1, 1)

        self.txt_Marca = QLineEdit(self.frame_4)
        self.txt_Marca.setObjectName(u"txt_Marca")
        self.txt_Marca.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Marca, 4, 0, 1, 1)

        self.txt_Processador = QLineEdit(self.frame_4)
        self.txt_Processador.setObjectName(u"txt_Processador")
        self.txt_Processador.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Processador, 4, 1, 1, 1)

        self.txt_Service = QLineEdit(self.frame_4)
        self.txt_Service.setObjectName(u"txt_Service")
        self.txt_Service.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Service, 5, 0, 1, 1)

        self.txt_Cor = QLineEdit(self.frame_4)
        self.txt_Cor.setObjectName(u"txt_Cor")
        self.txt_Cor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Cor, 6, 2, 1, 1)

        self.txt_Setor = QLineEdit(self.frame_4)
        self.txt_Setor.setObjectName(u"txt_Setor")
        self.txt_Setor.setAlignment(Qt.AlignCenter)
        self.txt_Setor.setReadOnly(False)

        self.gridLayout.addWidget(self.txt_Setor, 2, 2, 1, 1)

        self.txt_DataAquisicao = QLineEdit(self.frame_4)
        self.txt_DataAquisicao.setObjectName(u"txt_DataAquisicao")
        self.txt_DataAquisicao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_DataAquisicao, 6, 1, 1, 1)

        self.btn_SalvarCadastro = QPushButton(self.frame_4)
        self.btn_SalvarCadastro.setObjectName(u"btn_SalvarCadastro")
        self.btn_SalvarCadastro.setMinimumSize(QSize(160, 30))
        self.btn_SalvarCadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_SalvarCadastro.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(194, 194, 194);\n"
"	border-radius: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243,243,243);\n"
"}")

        self.gridLayout.addWidget(self.btn_SalvarCadastro, 7, 0, 1, 4, Qt.AlignHCenter)

        self.txt_SSD = QLineEdit(self.frame_4)
        self.txt_SSD.setObjectName(u"txt_SSD")
        self.txt_SSD.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_SSD, 4, 3, 1, 1)

        self.txt_NomeDispositivo = QLineEdit(self.frame_4)
        self.txt_NomeDispositivo.setObjectName(u"txt_NomeDispositivo")
        self.txt_NomeDispositivo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_NomeDispositivo, 2, 1, 1, 1)

        self.txt_Colaborador = QLineEdit(self.frame_4)
        self.txt_Colaborador.setObjectName(u"txt_Colaborador")
        self.txt_Colaborador.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Colaborador, 2, 3, 1, 1)

        self.txt_Arquitetura = QLineEdit(self.frame_4)
        self.txt_Arquitetura.setObjectName(u"txt_Arquitetura")
        self.txt_Arquitetura.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Arquitetura, 5, 3, 1, 1)

        self.txt_AnoFabricacao = QLineEdit(self.frame_4)
        self.txt_AnoFabricacao.setObjectName(u"txt_AnoFabricacao")
        self.txt_AnoFabricacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_AnoFabricacao, 6, 0, 1, 1)

        self.txt_Id = QLineEdit(self.frame_4)
        self.txt_Id.setObjectName(u"txt_Id")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setBold(False)
        font1.setItalic(False)
        self.txt_Id.setFont(font1)
        self.txt_Id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Id, 2, 0, 1, 1)

        self.txt_IdDispositivo = QLineEdit(self.frame_4)
        self.txt_IdDispositivo.setObjectName(u"txt_IdDispositivo")
        self.txt_IdDispositivo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_IdDispositivo, 3, 0, 1, 4)

        self.txt_MemoriaRam = QLineEdit(self.frame_4)
        self.txt_MemoriaRam.setObjectName(u"txt_MemoriaRam")
        self.txt_MemoriaRam.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_MemoriaRam, 4, 2, 1, 1)

        self.tit_Cadastro = QLabel(self.frame_4)
        self.tit_Cadastro.setObjectName(u"tit_Cadastro")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tit_Cadastro.sizePolicy().hasHeightForWidth())
        self.tit_Cadastro.setSizePolicy(sizePolicy2)
        self.tit_Cadastro.setMaximumSize(QSize(16777215, 200))
        self.tit_Cadastro.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tit_Cadastro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tit_Cadastro, 1, 0, 1, 4)


        self.verticalLayout_15.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 16):
            self.tableWidget.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(131,131,131);\n"
"	border-radius: 15px;\n"
"	color: #ffffff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243,243,243);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(61,61,61);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_Excel = QPushButton(self.frame_3)
        self.btn_Excel.setObjectName(u"btn_Excel")
        self.btn_Excel.setMinimumSize(QSize(100, 30))
        self.btn_Excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_Excel)

        self.btn_Alterar = QPushButton(self.frame_3)
        self.btn_Alterar.setObjectName(u"btn_Alterar")
        self.btn_Alterar.setMinimumSize(QSize(100, 30))
        self.btn_Alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_Alterar)

        self.btn_Excluir = QPushButton(self.frame_3)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        self.btn_Excluir.setMinimumSize(QSize(100, 30))
        self.btn_Excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_Excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_Cadastrar)
        self.pg_Contatos = QWidget()
        self.pg_Contatos.setObjectName(u"pg_Contatos")
        self.verticalLayout_16 = QVBoxLayout(self.pg_Contatos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.pg_Contatos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_16.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_Contatos)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_16.addWidget(self.label_8)

        self.label_10 = QLabel(self.pg_Contatos)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_16.addWidget(self.label_10)

        self.label_12 = QLabel(self.pg_Contatos)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_16.addWidget(self.label_12)

        self.label_14 = QLabel(self.pg_Contatos)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)

        self.Pages.addWidget(self.pg_Contatos)
        self.pg_Sobre = QWidget()
        self.pg_Sobre.setObjectName(u"pg_Sobre")
        self.Pages.addWidget(self.pg_Sobre)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_Frame)

        self.footer_Frame = QFrame(self.main_Container)
        self.footer_Frame.setObjectName(u"footer_Frame")
        self.footer_Frame.setFrameShape(QFrame.StyledPanel)
        self.footer_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_Frame)


        self.verticalLayout_14.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.main_Container)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jo\u00e3o Pedro", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_Contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Responsavel:</span> Jo\u00e3o Pedro<br/></p><p align=\"center\"><span style=\" font-weight:600;\">Sistema: </span>Cadastro de M\u00e1quinas<br/></p><p align=\"center\"><span style=\" font-weight:600;\">Status:</span> Ativo</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/images.png\"/></p></body></html>", None))
        self.txt_SistemaOperacional.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SO", None))
        self.txt_Licenciado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Licenciado", None))
        self.txt_Marca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.txt_Processador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Processador", None))
        self.txt_Service.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.txt_Cor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cor", None))
        self.txt_Setor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Setor", None))
        self.txt_DataAquisicao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Aquisi\u00e7\u00e3o", None))
        self.btn_SalvarCadastro.setText(QCoreApplication.translate("MainWindow", u"Salvar Cadastro", None))
        self.txt_SSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SSD", None))
        self.txt_NomeDispositivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Dispositivo", None))
        self.txt_Colaborador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Colaborador", None))
        self.txt_Arquitetura.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Arquitetura", None))
        self.txt_AnoFabricacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ano de Fabrica\u00e7\u00e3o", None))
        self.txt_Id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.txt_IdDispositivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Dispositivo", None))
        self.txt_MemoriaRam.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Memoria RAM", None))
        self.tit_Cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Cadastro de M\u00e1quinas</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MAQUINAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome Dispositivo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Setor", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Arquitetura", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Processador", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Mem\u00f3ria Ram", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SSD", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SO", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Licenciado", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Colaborador", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Ano Fabrica\u00e7\u00e3o", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Data Aquisi\u00e7\u00e3o", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cor", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID Dispositivo", None));
        self.btn_Excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_Alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_Excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Maquinas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/whatsapp.png\"/><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">(61) 98152 - 5401</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/instagram.png\"/><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\"> jaossantana</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/linkedin.png\"/><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\"> Jo\u00e3o Pedro dos Santos Santana</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons8-microsoft-outlook-2019-48.png\"/><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">DevJoao@xz235.onmicrosoft.com</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Jo\u00e3o Pedro", None))
    # retranslateUi


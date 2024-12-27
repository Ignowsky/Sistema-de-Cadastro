from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from database import Data_base

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

        ##########################################################
        # Botão de Cadastrar Maquinas
        self.btn_SalvarCadastro.clicked.connect(self.cadastrar_maquinas)

        ##########################################################
        # Comando que irá preencher a tabela com os dados do banco
        self.buscar_maquinas()
        
        # Botão para atualizar
        self.btn_Alterar.clicked.connect(self.update_maquinas)

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


   # Método para limpar as entradas após o cadastro
    def limpar_entradas(self):
        self.txt_Id.clear()
        self.txt_NomeDispositivo.clear()
        self.txt_Setor.clear()
        self.txt_Colaborador.clear()
        self.txt_IdDispositivo.clear()
        self.txt_Marca.clear()
        self.txt_Processador.clear()
        self.txt_MemoriaRam.clear()
        self.txt_SSD.clear()
        self.txt_Service.clear()
        self.txt_SistemaOperacional.clear()
        self.txt_Licenciado.clear()
        self.txt_Arquitetura.clear()
        self.txt_AnoFabricacao.clear()
        self.txt_DataAquisicao.clear()
        self.txt_Cor.clear()

    def cadastrar_maquinas(self):
        db = Data_base()
        db.connect()
        fullDataSet = (
            self.txt_Id.text(),
            self.txt_NomeDispositivo.text(),
            self.txt_Setor.text(),
            self.txt_Colaborador.text(),
            self.txt_IdDispositivo.text(),
            self.txt_Marca.text(),
            self.txt_Processador.text(),
            self.txt_MemoriaRam.text(),
            self.txt_SSD.text(),
            self.txt_Service.text(),
            self.txt_SistemaOperacional.text(),
            self.txt_Licenciado.text(),
            self.txt_Arquitetura.text(),
            self.txt_AnoFabricacao.text(),
            self.txt_DataAquisicao.text(),
            self.txt_Cor.text()
        )
        ##########################################################
        # CADASTRAR NO BANCO DE DADOS
        resp = db.register_maquina(fullDataSet)

        if resp == "Dados inseridos com sucesso":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado com Sucesso")
            msg.setText("Cadastro Realizado com Sucesso")
            msg.exec()
            db.close_connection()
        ##########################################################
        # Atualiza a tabela automaticament após o cadastro
            self.buscar_maquinas()
            
        # Limpar as entradas após o cadastro
            self.limpar_entradas()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro ao Cadastrar")
            msg.setText("Erro ao Cadastrar")
            msg.exec()
            db.close_connection()
            return
    
    def buscar_maquinas(self):

        db = Data_base()
        db.connect()
        result = db.select_all_maquinas()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data, in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()
        
        
    def update_maquinas(self):
        
        dados = []
        update_dados = []
        
        
        for row in range (self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
                
            update_dados.append(dados)
            dados = []
            
        # Atualizar dados no banco de dados
        db = Data_base()
        db.connect()
        
        for maq in update_dados:
            db.update_maquina(tuple(maq))        
        db.close_connection()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Dados Atualizados com Sucesso")
        msg.setText("Dados Atualizados com Sucesso")
        msg.exec()
        
        self.tableWidget.reset()
        self.buscar_maquinas
    
if __name__ == "__main__":
    db = Data_base()
    db.connect()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


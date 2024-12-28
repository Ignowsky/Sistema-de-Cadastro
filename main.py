from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
import mysql.connector
from database import Data_base
import pandas as pd

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
        
        ##########################################################
        # Botão para atualizar
        self.btn_Alterar.clicked.connect(self.update_maquinas)
        
        ##########################################################
        # Botao para excluir os registros
        self.btn_Excluir.clicked.connect(self.deletar_maquina)
        
        ##########################################################
        # Botão para gerar o arquivo Excel
        self.btn_Excel.clicked.connect(self.gerar_excel)


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
            int(self.txt_Id.text()),
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
        # Obter a linha selecionada
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        
        if not selected_rows:
            # Se nenhuma linha estiver selecionada, exibir mensagem de erro
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Seleção necessária")
            msg.setText("Por favor, selecione uma linha para atualizar.")
            msg.exec()
            return

        # Obter os dados da linha selecionada
        row = selected_rows[0].row()  # Pega a primeira linha selecionada

        dados = []
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            dados.append(item.text() if item else '')  # Verificar se a célula está vazia

        # Adicionar o Id_Maquina como último dado, que será usado no WHERE
        id_maquina = dados[0]  # Supondo que o Id_Maquina seja a primeira coluna
        dados.append(id_maquina)

        # Atualizar dados no banco de dados
        db = Data_base()
        db.connect()

        # Passar os dados da linha selecionada para a função de atualização
        resultado = db.update_maquina(tuple(dados))

        db.close_connection()

        # Exibir mensagem de sucesso ou erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information if "sucesso" in resultado.lower() else QMessageBox.Critical)
        msg.setWindowTitle("Atualização")
        msg.setText(resultado)
        msg.exec()

        # Atualizar a tabela
        self.tableWidget.clearContents()
        self.buscar_maquinas()  # Refrescar os dados da tabela

    def deletar_maquina(self):
        db = Data_base()
        db.connect()

        # Configuração do QMessageBox para confirmação
        msg = QMessageBox()
        msg.setWindowTitle("Deletar Máquina")
        msg.setText("Este registro será excluído permanentemente.")
        msg.setInformativeText("Deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()  # Correto: Chamar o método exec()

        if resp == QMessageBox.Yes:  # Comparar com QMessageBox.Yes corretamente
            # Obtém o ID da máquina selecionada na tabela
            Id = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            
            # Chama o método para deletar a máquina
            result = db.delete_maquina(Id)

            # Atualiza a tabela após exclusão
            self.buscar_maquinas()

            # Exibe mensagem de sucesso
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Registro Excluído")
            msg.setText("Registro excluído com sucesso.")
            msg.exec()
        else:
            # Caso o usuário escolha "Não", nenhuma ação é tomada
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Operação Cancelada")
            msg.setText("A exclusão foi cancelada.")
            msg.exec()

        # Fecha a conexão com o banco de dados
        db.close_connection()
          
    def gerar_excel(self):
        
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='joao1301',
            database='bd_cadastros'
        )
            
        maquinas = pd.read_sql_query(
            """
            SELECT *
            FROM bd_cadastros.cadastro_maquinas
            """,
            cnx
        )
            
        maquinas.to_excel('maquinas.xlsx', sheet_name='Maquinas', index=False)
            
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Arquivo Gerado!")
        msg.setText("Arquivo gerado em Excel com sucesso!")
        msg.exec()
        
            
        
        
   
if __name__ == "__main__":
    db = Data_base()
    db.connect()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


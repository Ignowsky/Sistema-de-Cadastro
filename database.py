import mysql.connector

class Data_base:
    def __init__(self, host = 'localhost', user = 'root', password = 'joao1301', database = 'bd_cadastros'):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user = 'root',
            password = 'joao1301',
            database = 'bd_cadastros'
        )

        def connect(self):
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
        def close_connection(self):
            try:
                self.connection.close()
            except:
                pass

        def register_maquina(self, fullDataSet):

            campos_tabela = (
                'Id_Maquina',
                'Nome_Dispositivo',
                'Setor',
                'Colaborador',
                'ID_Dispositivo',
                'Marca',
                'Processador',
                'Memoria_Ram',
                'SSD',
                'Service',
                'SO',
                'Licenciado',
                'Arquitetura',
                'Ano_Fabricacao',
                'Data_Aquisicao',
                'cor'
            )

            qntd_campos = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
            cursor = self.connection.cursor()

            try:
                cursor.execute(f"""INSERTO INTO bd_cadastros.cadastro_Maquinas{campos_tabela}
                    VALUES({qntd_campos}),""",fullDataSet)
                return("Dados inseridos com sucesso")
            except:
                return "Erro ao inserir dados"
            
        def select_all_maquinas(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""SELECT *
                                FROM bd_cadastros.cadastro_Maquina
                                ORDER BY Id_Maquina""")
                maquinas = cursor.fetchall()
                return maquinas
            except:
                pass
            
        def delete_maquina(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""DELETE FROM bd_cadastros.cadastro_Maquina
                               WHERE Id_Maquina = {Id_Maquina}""")
                self.connection.commit()
                return "Dados deletados com sucesso"
            
            except:
                return "Erro ao deletar dados"
            
        def update_maquina(self, fullDataSet):
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"""
                    UPDATE bd_cadastros.cadastro_Maquina set
                            Id_Maquina = '{fullDataSet[0]},
                            Nome_Dispositivo = '{fullDataSet[1]},
                            Setor = '{fullDataSet[2]},
                            Colaborador = '{fullDataSet[3]},
                            ID_Dispositivo = '{fullDataSet[4]},
                            Marca = '{fullDataSet[5]},
                            Processador = '{fullDataSet[6]},
                            Memoria_Ram = '{fullDataSet[7]},
                            SSD = '{fullDataSet[8]},
                            Service = '{fullDataSet[9]},
                            SO = '{fullDataSet[10]},
                            Licenciado = '{fullDataSet[11]},
                            Arquitetura = '{fullDataSet[12]},
                            Ano_Fabricacao = '{fullDataSet[13]},
                            Data_Aquisicao = '{fullDataSet[14]},
                            cor = '{fullDataSet[15]}
                            WHERE Id_Maquina = {fullDataSet[0]}""")
                
                self.connection.commit()
                return "Dados atualizados com sucesso"
            
            except:
                return "Erro ao atualizar dados"
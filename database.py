import mysql.connector

class Data_base:
    def __init__(self, host='localhost', user='root', password='joao1301', database='bd_cadastros'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexão estabelecida com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão encerrada.")

    def register_maquina(self, fullDataSet):
        campos_tabela = (
            'Id_Maquina', 'Nome_Dispositivo', 'Setor', 'Colaborador',
            'ID_Dispositivo', 'Marca', 'Processador', 'Memoria_Ram', 'SSD',
            'Service', 'SO', 'Licenciado', 'Arquitetura', 'Ano_Fabricacao',
            'Data_Aquisicao', 'cor'
        )
        placeholders = ", ".join(["%s"] * len(campos_tabela))  # Para substituir cada campo
        query = f"INSERT INTO cadastro_maquinas ({', '.join(campos_tabela)}) VALUES ({placeholders})"
        
        try:
            self.cursor.execute(query, fullDataSet)
            self.connection.commit()
            return "Dados inseridos com sucesso"
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")
            return "Erro ao inserir dados"
        # Atualiza a tabela automaticament após o cadastro
        self.buscar_maquinas()
        
    def select_all_maquinas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM cadastro_maquinas ORDER BY Id_Maquina")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Erro ao buscar dados: {err}")
            return None
            
    def delete_maquina(self, Id_Maquina):
        try:
            query = """DELETE FROM cadastro_maquinas WHERE Id_Maquina = %s"""
            self.cursor.execute(query, (Id_Maquina,))
            self.connection.commit()
            return "Dados deletados com sucesso"
        except mysql.connector.Error as err:
            print(f"Erro ao deletar dados: {err}")
            return "Erro ao deletar dados"
            
    def update_maquina(self, fullDataSet):
        query = """
            UPDATE cadastro_maquinas
            SET Nome_Dispositivo = %s,
                Setor = %s,
                Colaborador = %s,
                ID_Dispositivo = %s,
                Marca = %s,
                Processador = %s,
                Memoria_Ram = %s,
                SSD = %s,
                Service = %s,
                SO = %s,
                Licenciado = %s,
                Arquitetura = %s,
                Ano_Fabricacao = %s,
                Data_Aquisicao = %s,
                cor = %s
            WHERE Id_Maquina = %s
        """
        try:
            self.cursor.execute(query, fullDataSet)
            self.connection.commit()
            return "Dados atualizados com sucesso"
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar dados: {err}")
            return "Erro ao atualizar dados"
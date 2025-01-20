# Sistema de Cadastro de Máquinas

## Descrição do Projeto
Este projeto é uma aplicação de desktop desenvolvida em Python com a biblioteca **PySide6**, que permite o gerenciamento de informações sobre máquinas, incluindo cadastro, visualização e atualização dos dados. A interface gráfica é interativa e moderna, oferecendo animações e facilidade de uso.

O projeto também utiliza um banco de dados para persistência das informações, permitindo o armazenamento seguro e eficiente de registros.

---

## Funcionalidades
- Cadastro de máquinas com informações detalhadas, como:
  - Nome do dispositivo
  - Setor
  - Colaborador associado
  - Processador, Memória RAM, SSD, entre outros.
- Visualização de todas as máquinas cadastradas em uma tabela.
- Atualização das informações diretamente na interface.
- Animação para exibição e ocultação do menu lateral.
- Mensagens de sucesso ou erro ao interagir com o banco de dados.

---

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **PySide6**: Para criação da interface gráfica.
- **SQLite/MySQL**: Para armazenamento dos dados.
- **QMessageBox**: Para exibição de mensagens ao usuário.

---

## Requisitos para Instalação
Certifique-se de ter os seguintes itens instalados em sua máquina:
- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.

Pacotes necessários:
```bash
pip install PySide6
```

# Sistema de Cadastro de Máquinas

## Descrição do Projeto
Este projeto é uma aplicação de desktop desenvolvida em Python com a biblioteca **PySide6**, que permite o gerenciamento de informações sobre máquinas, incluindo cadastro, visualização e atualização dos dados. A interface gráfica é interativa e moderna, oferecendo animações e facilidade de uso.

O projeto também utiliza um banco de dados para persistência das informações, permitindo o armazenamento seguro e eficiente de registros.

---

## Funcionalidades
- Cadastro de máquinas com informações detalhadas, como:
  - Nome do dispositivo
  - Setor
  - Colaborador associado
  - Processador, Memória RAM, SSD, entre outros.
- Visualização de todas as máquinas cadastradas em uma tabela.
- Atualização das informações diretamente na interface.
- Animação para exibição e ocultação do menu lateral.
- Mensagens de sucesso ou erro ao interagir com o banco de dados.

---

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **PySide6**: Para criação da interface gráfica.
- **SQLite/MySQL**: Para armazenamento dos dados.
- **QMessageBox**: Para exibição de mensagens ao usuário.

---

## Requisitos para Instalação
Certifique-se de ter os seguintes itens instalados em sua máquina:
- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.

Pacotes necessários:
```bash
pip install PySide6
```

## Como Executar o Projeto
### 1. Clone o Repositório
```
git clone https://github.com/seu-usuario/sistema-cadastro-maquinas.git
cd sistema-cadastro-maquinas
```


### 2. Configure o Banco de Dados

Certifique-se de configurar o banco de dados no arquivo Data_base.py.
Ajuste as credenciais, caso esteja utilizando um banco como MySQL ou PostgreSQL.

### 3. Execute a Aplicação
No terminal, execute:
```
python main.py
```

## Estrutura do Projeto
```
sistema-cadastro-maquinas/
│
├── database/
│   └── Data_base.py          # Classe responsável pela conexão com o banco de dados
│
├── ui/
│   └── ui_main.py            # Arquivo gerado pelo Qt Designer
│
├── main.py                   # Arquivo principal que inicializa a aplicação
├── requirements.txt          # Lista de dependências do projeto
└── README.md                 # Documentação do projeto
```

## Principais Arquivos e Funções
### main.py
Este arquivo contém a lógica da interface gráfica. Aqui estão os destaques:

  - **cadastrar_maquinas**: Lê os dados do formulário e os insere no banco de dados.
  - **buscar_maquinas**: Preenche a tabela com os registros do banco de dados.
  - **update_maquinas**: Atualiza os registros diretamente a partir da tabela.
  
### Data_base.py

Arquivo responsável pela comunicação com o banco de dados. Principais funções:

  - **connect**: Estabelece a conexão com o banco de dados.
  - **register_maquina**: Insere um novo registro no banco.
  - **select_all_maquinas**: Retorna todos os registros do banco.
  - **update_maquina**: Atualiza informações de uma máquina específica


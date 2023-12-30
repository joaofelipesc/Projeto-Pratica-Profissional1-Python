from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,QMessageBox,
    QWidget)
import qdarkstyle
import pyodbc
from datetime import date, timedelta
from OFICIAL_ui import Ui_MainWindow
global Banco
class Banco:
    def __init__(self):
        self.connection = pyodbc.connect(driver='SQL Server', server='regulus.cotuca.unicamp.br',
                                         database='BD23319', uid='BD23319', pwd='BD23319')
        self.cursor = self.connection.cursor()
class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.banco = Banco()
        self.BotaoCadastro.clicked.connect(self.Cadastro)
        self.inserirDadoTabela()
        self.inserirDadoMatricula()
        self.BOXPLANOS.currentIndexChanged.connect(self.labelPlanos)
        self.BotaoDelCliente.clicked.connect(self.apagarcliente)
        self.ButaoDelMatric.clicked.connect(self.apagarmatricula)
        self.pushButton.clicked.connect(self.matricular)
        self.BotaoPesquisa.clicked.connect(self.Pesquisar)
        self.Refresh.clicked.connect(self.atualizar)
        self.BotaoPesquisaClient.clicked.connect(self.PesquisarCliente)
        self.Refresh_2.clicked.connect(self.atualizar2)

    def apagarcliente(self):
        if self.TabelaCliente.selectedItems():
            row = self.TabelaCliente.currentRow()
            idCliente = int(self.TabelaCliente.item(row, 0).text())
            consultaSql = "DELETE FROM ACADEMIA.Clientes WHERE Id_Cliente = ?"
            self.banco.cursor.execute(consultaSql, idCliente)
            self.banco.connection.commit()
            self.inserirDadoTabela()
            QMessageBox.information(self, "Realizado", "Cliente excluído com sucesso.")
        else:
            QMessageBox.warning(self, "Erro", "Selecione um cliente para excluir.")

    def inserirDadoTabela(self):
        self.banco.cursor.execute("SELECT Id_Cliente, Nome, FORMAT(DataNasc, 'dd/MM/yyyy') AS DataNasc, Sexo, Telefone, Email, Endereco FROM ACADEMIA.Clientes") 
        dados = self.banco.cursor.fetchall()
        if dados:
            self.TabelaCliente.setRowCount(len(dados))
            self.TabelaCliente.setColumnCount(len(dados[0]))

            for row, record in enumerate(dados):
                for column, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.TabelaCliente.setItem(row, column, item)

    def inserirDadoMatricula(self):
        consultaSql = '''
    SELECT M.Id_Matricula, C.Id_Cliente, C.Nome AS NomeCliente, M.Id_Plano,
    FORMAT(M.DataInicio, 'dd/MM/yyyy') AS DataInicio,
    FORMAT(M.DataFim, 'dd/MM/yyyy') AS DataFim
    FROM ACADEMIA.Matricula AS M
    INNER JOIN ACADEMIA.Clientes AS C ON M.Id_Cliente = C.Id_Cliente
        '''
        self.banco.cursor.execute(consultaSql)
        dados = self.banco.cursor.fetchall()

        if dados:
            self.TabelMatricula.setRowCount(len(dados))
            self.TabelMatricula.setColumnCount(len(dados[0]))

            for row, record in enumerate(dados):
                for column, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.TabelMatricula.setItem(row, column, item)

    def apagarmatricula(self):
        if self.TabelMatricula.selectedItems():
            row = self.TabelMatricula.currentRow()
            idmatricula = int(self.TabelMatricula.item(row, 0).text())
            consultaSql = "DELETE FROM ACADEMIA.Matricula WHERE Id_Matricula = ?"
            self.banco.cursor.execute(consultaSql, idmatricula)
            self.banco.connection.commit()
            self.inserirDadoMatricula()
            QMessageBox.information(self, "Realizado", "Matricula excluída com sucesso.")
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma matricula para excluir.")

    def labelPlanos(self, index):
        planoselecionado = self.BOXPLANOS.currentText()
        if planoselecionado == "Academia Geral":
            self.label_10.setText("Plano de Academia")
            self.descplanos.setText("Inclui acesso a todas as atividades e instalações da academia, como musculação,\ncardio, aulas em grupo, entre outros.\nOs professores especializados em academia estarão disponíveis para fornecer \norientação e assistência em diferentes áreas de treinamento.")
            self.labelvalor.setText("Valor: R$200")
            self.labeldura.setText("Duração: 1 Mês")
            self.labelId.setText("Id: 3")

        elif planoselecionado == "Selecione o Plano":
            self.label_10.setText("Selecione o Plano")
            self.descplanos.setText(" ")
            self.labeldura.setText(" ")
            self.labelvalor.setText(" ")
            self.labelId.setText(" ")
        elif planoselecionado == "Plano de Dança":
            self.label_10.setText("Plano de Dança")
            self.descplanos.setText("Inclui aulas de dança em diferentes estilos, como ballet, hip-hop, salsa, dança\n contemporânea, entre outros.\nOs professores especializados em dança estarão presentes para ensinar técnicas, \n coreografias e proporcionar um ambiente divertido para os alunos.")
            self.labelvalor.setText("Valor: R$150")
            self.labeldura.setText("Duração: 1 Mês")
            self.labelId.setText("Id: 4")
        elif planoselecionado == "Plano de Artes Marciais":
            self.label_10.setText("Plano de Artes Marciais")
            self.descplanos.setText("Inclui treinamento em diversas artes marciais, como karatê, taekwondo, jiu-jitsu,\n boxe, entre outras.\n Os professores especializados em artes marciais estarão disponíveis para ensinar \ntécnicas de defesa pessoal, aprimorar habilidades físicas e promover disciplina.")
            self.labelvalor.setText("Valor: R$180")
            self.labeldura.setText("Duração: 1 Mês")
            self.labelId.setText("Id: 5")
        elif planoselecionado == "Plano de Pilates":
            self.label_10.setText("Plano de Pilates")
            self.descplanos.setText("Inclui aulas de Pilates com foco no fortalecimento do núcleo, \nalongamento e melhoria da postura.\n Os professores especializados em Pilates estarão presentes para fornecer orientações \nsobre os exercícios, corrigir posturas e adaptar os movimentos às necessidades\n individuais dos alunos.")
            self.labelvalor.setText("Valor: R$120")        
            self.labeldura.setText("Duração: 1 Mês")
            self.labelId.setText("Id: 6")
        elif planoselecionado == "Plano Combinado":
            self.label_10.setText("Plano Combinado")
            self.descplanos.setText("Inclui acesso à academia em geral, bem como aulas de dança em diferentes estilos.\n Os professores especializados em academia e dança estarão disponíveis para fornecer\n treinamento nas respectivas áreas.")
            self.labelvalor.setText("Valor: R$250")
            self.labeldura.setText("Duração: 1 Mês")
            self.labelId.setText("Id: 7")
    def Cadastro(self):
        Nome = self.NomeLinha.text()
        Nascimento = self.DataNascLinha.text()
        if self.CaixaSexo.currentText() == "Masculino":
            sexo = "M"
        else:
            sexo = "F"
        celular = self.TelefoLinha.text()
        email = self.Emailinha.text()
        endereco = self.Endereo.text()
        if not Nome:
            QMessageBox.information(self,"Erro","Digite o nome")
        else:
            self.banco.cursor.execute("SELECT MAX(Id_Cliente) FROM ACADEMIA.Clientes")
        resultado = self.banco.cursor.fetchone()
        idCliente = resultado[0] + 1 if resultado[0] is not None else 100
        ConsultaSql = f"INSERT INTO ACADEMIA.Clientes (Id_Cliente, Nome, DataNasc, Sexo, Telefone, Email, Endereco) VALUES (?, ?, CONVERT(DATE, ?, 103), ?, ?, ?, ?)"
        
        self.banco.cursor.execute(ConsultaSql, idCliente, Nome, Nascimento, sexo, celular, email, endereco)
        self.banco.connection.commit()
        self.NomeLinha.clear()
        self.DataNascLinha.clear()
        self.TelefoLinha.clear()
        self.Emailinha.clear()
        self.Endereo.clear()
        self.inserirDadoTabela()
        QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso!")

    def matricular(self):
        idplano = self.BOXPLANOS.currentText()
        if idplano == "Academia Geral":
            idplano = 3
        elif idplano == "Plano de Dança":
            idplano = 4
        elif idplano == "Plano de Artes Marciais":
            idplano = 5
        elif idplano == "Plano de Pilates":
            idplano = 6
        elif idplano == "Plano Combinado":
            idplano = 7
        else:
            QMessageBox.information(self, "Erro", "Selecione um Plano para fazer a matrícula!")

        datainicio = date.today().strftime("%Y/%m/%d")
        datafim = (date.today() + timedelta(days=30)).strftime("%Y/%m/%d")


        if self.TabelaCliente.selectedItems():
            row = self.TabelaCliente.currentRow()
            idcliente = int(self.TabelaCliente.item(row, 0).text())
        else:
            QMessageBox.information(self, "Erro", "Por favor slecione um cliente na tabela para matricular!")

        self.banco.cursor.execute("SELECT MAX(Id_Matricula) FROM ACADEMIA.Matricula")
        resultado = self.banco.cursor.fetchone()
        idmatricula = resultado[0] + 1 if resultado[0] is not None else 1001

        consultaSql = "INSERT INTO ACADEMIA.Matricula (Id_Cliente, Id_Plano, Id_Matricula, DataInicio, DataFim) VALUES (?, ?, ?, ?, ?)"
        self.banco.cursor.execute(consultaSql, idcliente, idplano, idmatricula, datainicio, datafim)
        self.banco.connection.commit()
        self.inserirDadoMatricula()
        QMessageBox.information(self, "Matrícula", "Matrícula realizada com sucesso!")

    def Pesquisar(self):
        pesquisa = self.BuscadorTabelMatric.text()
        consultaSql = '''
            SELECT M.Id_Matricula, C.Id_Cliente, C.Nome AS NomeCliente, M.Id_Plano,
            FORMAT(M.DataInicio, 'dd/MM/yyyy') AS DataInicio,
            FORMAT(M.DataFim, 'dd/MM/yyyy') AS DataFim
            FROM ACADEMIA.Matricula AS M
            INNER JOIN ACADEMIA.Clientes AS C ON M.Id_Cliente = C.Id_Cliente
            WHERE C.Nome LIKE ? OR CAST(C.Id_Cliente AS VARCHAR) = ? OR CAST(M.Id_Plano AS VARCHAR) = ?
        '''
        self.banco.cursor.execute(consultaSql, f'%{pesquisa}%', pesquisa, pesquisa)
        dados = self.banco.cursor.fetchall()
        if dados:
            self.TabelMatricula.setRowCount(len(dados))
            self.TabelMatricula.setColumnCount(len(dados[0]))

            for row, record in enumerate(dados):
                for column, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.TabelMatricula.setItem(row, column, item)
        else:
            self.TabelMatricula.clearContents()

        self.BuscadorTabelMatric.clear()


    def PesquisarCliente(self):
        pesquisa = self.BuscadorTabelClient.text()
        consultasql = '''
        SELECT * 
        FROM ACADEMIA.Clientes
        WHERE Nome LIKE ? OR Id_Cliente LIKE ?
        
        
        '''

        self.banco.cursor.execute(consultasql, f'%{pesquisa}%', pesquisa)
        dados = self.banco.cursor.fetchall()
        if dados:
            self.TabelaCliente.setRowCount(len(dados))
            self.TabelaCliente.setColumnCount(len(dados[0]))

            for row, record in enumerate(dados):
                for column, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.TabelaCliente.setItem(row, column, item)
        else:
            self.TabelaCliente.clearContents()

        self.BuscadorTabelClient.clear()



    def atualizar(self):
        self.inserirDadoMatricula()
        
    def atualizar2(self):
        self.inserirDadoTabela()





if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    janela = Janela()
    janela.show()
    app.exec()
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OFICIAL.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 821)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(520, 270, 351, 51))
        font = QFont()
        font.setFamilies([u"Oswald"])
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.BOXPLANOS = QComboBox(self.centralwidget)
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.addItem("")
        self.BOXPLANOS.setObjectName(u"BOXPLANOS")
        self.BOXPLANOS.setGeometry(QRect(810, 470, 251, 22))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 260, 481, 355))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setPointSize(14)
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.DataNascLinha = QDateEdit(self.layoutWidget)
        self.DataNascLinha.setObjectName(u"DataNascLinha")

        self.horizontalLayout_5.addWidget(self.DataNascLinha)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.TelefoLinha = QLineEdit(self.layoutWidget)
        self.TelefoLinha.setObjectName(u"TelefoLinha")

        self.horizontalLayout_3.addWidget(self.TelefoLinha)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Malgun Gothic"])
        font2.setPointSize(15)
        self.label_6.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.CaixaSexo = QComboBox(self.layoutWidget)
        self.CaixaSexo.addItem("")
        self.CaixaSexo.addItem("")
        self.CaixaSexo.setObjectName(u"CaixaSexo")

        self.horizontalLayout_4.addWidget(self.CaixaSexo)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.NomeLinha = QLineEdit(self.layoutWidget)
        self.NomeLinha.setObjectName(u"NomeLinha")
        self.NomeLinha.setMaxLength(30)

        self.horizontalLayout_6.addWidget(self.NomeLinha)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.Emailinha = QLineEdit(self.layoutWidget)
        self.Emailinha.setObjectName(u"Emailinha")
        self.Emailinha.setMaxLength(50)

        self.horizontalLayout_2.addWidget(self.Emailinha)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout.addWidget(self.label_9)

        self.Endereo = QLineEdit(self.layoutWidget)
        self.Endereo.setObjectName(u"Endereo")
        self.Endereo.setMaxLength(100)

        self.horizontalLayout.addWidget(self.Endereo)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.BotaoCadastro = QPushButton(self.layoutWidget)
        self.BotaoCadastro.setObjectName(u"BotaoCadastro")

        self.verticalLayout.addWidget(self.BotaoCadastro)

        self.descplanos = QLabel(self.centralwidget)
        self.descplanos.setObjectName(u"descplanos")
        self.descplanos.setGeometry(QRect(560, 330, 491, 91))
        font3 = QFont()
        font3.setPointSize(9)
        self.descplanos.setFont(font3)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 460, 231, 51))
        self.labelvalor = QLabel(self.centralwidget)
        self.labelvalor.setObjectName(u"labelvalor")
        self.labelvalor.setGeometry(QRect(860, 270, 231, 51))
        self.labelvalor.setFont(font)
        self.labeldura = QLabel(self.centralwidget)
        self.labeldura.setObjectName(u"labeldura")
        self.labeldura.setGeometry(QRect(560, 440, 141, 16))
        font4 = QFont()
        font4.setFamilies([u"Mosk Bold 700"])
        font4.setPointSize(9)
        self.labeldura.setFont(font4)
        self.labelId = QLabel(self.centralwidget)
        self.labelId.setObjectName(u"labelId")
        self.labelId.setGeometry(QRect(990, 430, 55, 16))
        self.Refresh = QPushButton(self.centralwidget)
        self.Refresh.setObjectName(u"Refresh")
        self.Refresh.setGeometry(QRect(980, 70, 41, 28))
        icon = QIcon()
        icon.addFile(u"icones/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Refresh.setIcon(icon)
        self.TabelMatricula = QTableWidget(self.centralwidget)
        if (self.TabelMatricula.columnCount() < 6):
            self.TabelMatricula.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TabelMatricula.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.TabelMatricula.setObjectName(u"TabelMatricula")
        self.TabelMatricula.setGeometry(QRect(570, 50, 401, 192))
        self.BotaoPesquisa = QPushButton(self.centralwidget)
        self.BotaoPesquisa.setObjectName(u"BotaoPesquisa")
        self.BotaoPesquisa.setGeometry(QRect(970, 20, 93, 29))
        icon1 = QIcon()
        icon1.addFile(u"icones/LUPA.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotaoPesquisa.setIcon(icon1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(501, 11, 102, 46))
        font5 = QFont()
        font5.setFamilies([u"Oswald"])
        font5.setPointSize(16)
        self.label_2.setFont(font5)
        self.ButaoDelMatric = QPushButton(self.centralwidget)
        self.ButaoDelMatric.setObjectName(u"ButaoDelMatric")
        self.ButaoDelMatric.setGeometry(QRect(980, 130, 106, 28))
        self.BuscadorTabelMatric = QLineEdit(self.centralwidget)
        self.BuscadorTabelMatric.setObjectName(u"BuscadorTabelMatric")
        self.BuscadorTabelMatric.setGeometry(QRect(610, 23, 351, 22))
        self.BuscadorTabelMatric.setMaxLength(50)
        self.BuscadorTabelClient = QLineEdit(self.centralwidget)
        self.BuscadorTabelClient.setObjectName(u"BuscadorTabelClient")
        self.BuscadorTabelClient.setGeometry(QRect(100, 10, 241, 22))
        self.BuscadorTabelClient.setMaxLength(50)
        self.BotaoPesquisaClient = QPushButton(self.centralwidget)
        self.BotaoPesquisaClient.setObjectName(u"BotaoPesquisaClient")
        self.BotaoPesquisaClient.setGeometry(QRect(350, 10, 93, 29))
        self.BotaoPesquisaClient.setIcon(icon1)
        self.Refresh_2 = QPushButton(self.centralwidget)
        self.Refresh_2.setObjectName(u"Refresh_2")
        self.Refresh_2.setGeometry(QRect(410, 50, 41, 28))
        self.Refresh_2.setIcon(icon)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 73, 21))
        self.label.setFont(font5)
        self.TabelaCliente = QTableWidget(self.centralwidget)
        if (self.TabelaCliente.columnCount() < 7):
            self.TabelaCliente.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TabelaCliente.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.TabelaCliente.setObjectName(u"TabelaCliente")
        self.TabelaCliente.setGeometry(QRect(10, 40, 391, 192))
        self.BotaoDelCliente = QPushButton(self.centralwidget)
        self.BotaoDelCliente.setObjectName(u"BotaoDelCliente")
        self.BotaoDelCliente.setGeometry(QRect(411, 137, 79, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Escolher Plano", None))
        self.BOXPLANOS.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o Plano", None))
        self.BOXPLANOS.setItemText(1, QCoreApplication.translate("MainWindow", u"Academia Geral", None))
        self.BOXPLANOS.setItemText(2, QCoreApplication.translate("MainWindow", u"Plano de Dan\u00e7a", None))
        self.BOXPLANOS.setItemText(3, QCoreApplication.translate("MainWindow", u"Plano de Artes Marciais", None))
        self.BOXPLANOS.setItemText(4, QCoreApplication.translate("MainWindow", u"Plano de Pilates", None))
        self.BOXPLANOS.setItemText(5, QCoreApplication.translate("MainWindow", u"Plano Combinado", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.TelefoLinha.setInputMask(QCoreApplication.translate("MainWindow", u"(99)99999-9999", None))
        self.TelefoLinha.setText(QCoreApplication.translate("MainWindow", u"()-", None))
        self.TelefoLinha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu N\u00famero de Celular", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.CaixaSexo.setItemText(0, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.CaixaSexo.setItemText(1, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.CaixaSexo.setCurrentText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.NomeLinha.setText("")
        self.NomeLinha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu Nome", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Emailinha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu Email", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.Endereo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu Endere\u00e7o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dados Pessoais", None))
        self.BotaoCadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar ", None))
        self.descplanos.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Matricular", None))
        self.labelvalor.setText("")
        self.labeldura.setText("")
        self.labelId.setText("")
        self.Refresh.setText("")
        ___qtablewidgetitem = self.TabelMatricula.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id Matr\u00edcula", None));
        ___qtablewidgetitem1 = self.TabelMatricula.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Id Cliente", None));
        ___qtablewidgetitem2 = self.TabelMatricula.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NomeCliente", None));
        ___qtablewidgetitem3 = self.TabelMatricula.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Id Plano", None));
        ___qtablewidgetitem4 = self.TabelMatricula.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data de inicio", None));
        ___qtablewidgetitem5 = self.TabelMatricula.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data Final", None));
        self.BotaoPesquisa.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00e1triculas", None))
        self.ButaoDelMatric.setText(QCoreApplication.translate("MainWindow", u"Deletar Matr\u00edcula", None))
        self.BuscadorTabelMatric.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.BuscadorTabelClient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.BotaoPesquisaClient.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Refresh_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem6 = self.TabelaCliente.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem7 = self.TabelaCliente.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem8 = self.TabelaCliente.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem9 = self.TabelaCliente.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem10 = self.TabelaCliente.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem11 = self.TabelaCliente.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem12 = self.TabelaCliente.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        self.BotaoDelCliente.setText(QCoreApplication.translate("MainWindow", u"Deletar Cliente", None))
    # retranslateUi


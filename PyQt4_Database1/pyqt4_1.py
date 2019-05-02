# -*- coding: utf-8 -*-

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from validacion import *

from database import DataBase

import  _mysql_exceptions

# DATABASE

# const DB
HOST = 'localhost'
USER = 'root'
PASS = 'pedroluis' #change password
DB   = 'dbpyqt4'

# tables DB
TABLE_NAME = {'person': 'Person'}

#const error
(ERROR, INFOR, WARN) = (100, 101, 102)

# function size_desktop_local -----------------
    # return QSize
def desktop():
    return QApplication.desktop().size()

# class: gui pyqt4 ----------------------------

# const widget
NON = 9  # None
PRE = 10 # presentation
OPU = 11 # op user
VID = 12 #view all data

# const user op
(INSERT, UPDATE, REMOVE) = (1000, 1001, 1002)

class GUI_PyQt4(QMainWindow):
    
    def __init__(self, title, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(title)
        
        self.__initGuiPyQt4()
        self.setWindowIcon(QIcon('icon-pyqt4.jpg'))
        size = desktop()
        height = size.height()
        width  = size.width()
        self.setGeometry(width/4, height/6, 
            600, 500);
        self.setMaximumSize(600, 500);
        self.setMinimumSize(600, 500);
        self.setVisible(True)
        
        self.db = DataBase(HOST, USER, PASS, DB)
    
    def __initGuiPyQt4(self):
        # declarations components
        self.typeWidgetL = NON
        self.typeWidgetA = PRE
        self.operationA = NON
        self.centralWidget = QWidget(self)
        self.preSis  = QWidget(self.centralWidget)
        self.userOp  = QWidget(self.centralWidget) 
        self.dataVi  = QWidget(self.centralWidget) 
        self.menuBar = QMenuBar(self)
        self.toolBar = QToolBar(self) 
        self.statusBar = QStatusBar(self)        
        
        self.lcentralMain = QVBoxLayout(self.centralWidget)
        self.centralWidget.setContentsMargins(50, 50, 50, 0)
        self.table = QTableWidget(self.dataVi)
        self.table.resize(480, 300)
        self.table.setSortingEnabled(False)
        self.table.resizeColumnsToContents()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # init menubar
        menus = [QMenu('&Sistema DB', self.menuBar), QMenu('&Usuario', self.menuBar), 
            QMenu('&Ayuda', self.menuBar)]
        
        actionsSDB = [QAction('Ir a  Inicio', menus[0]), QAction('Salir', menus[0])]
        self.connect(actionsSDB[0], SIGNAL('triggered()'), self.slotInicio)
        self.connect(actionsSDB[1], SIGNAL('triggered()'), qApp, SLOT('quit()'))
        actionsSDB[0].setShortcut('Ctrl+I')
        actionsSDB[1].setShortcut('Ctrl+Q')
        menus[0].addActions(actionsSDB)

        actionsUser = [QAction(QString.fromUtf8('Operaciones de Usuario'), menus[1]), QAction('Ver Datos', menus[1])]
        actionsUser[0].setShortcut('Ctrl+U')
        actionsUser[1].setShortcut('Ctrl+V')
        self.connect(actionsUser[0], SIGNAL('triggered()'), self.userOperations)
        self.connect(actionsUser[1], SIGNAL('triggered()'), self.viewAllData)
        menus[1].addActions(actionsUser)
        
        actionsH = [QAction('A cerca de...', menus[2])]
        menus[2].addActions(actionsH)
        
        self.menuBar.addMenu(menus[0])
        self.menuBar.addMenu(menus[1])
        self.menuBar.addMenu(menus[2])
        
        # init toolbar
        self.titleAction = QLabel(self.toolBar) 
        self.titleAction.setFont(QFont('System', 12, -1, False))
        self.toolBar.setFloatable(False)
        self.toolBar.setMovable(False)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.titleAction)
        
        # init presis
        imageP = QLabel("""<b><center>PyQT4 - Data Base</center></b>""", self.preSis)
        imageP.setTextFormat(Qt.RichText)
        imageP.setFont(QFont('System', 32, 50))
        imageP.resize(480, 280)
        imageP.setFrameStyle(QFrame.WinPanel | QFrame.Sunken)
        imageP.setStyleSheet(QString.fromUtf8("background-image: url(icon-pyqt4.jpg)"))
        
        bnlvF = QHBoxLayout(self.preSis) 
        
        self.buttonO = QCommandLinkButton(QString.fromUtf8('Operaciones de Usuario'))
        
        self.buttonV = QCommandLinkButton(QString.fromUtf8('Ver Datos de la BD'))
        
        self.connect(self.buttonO, SIGNAL('clicked()'), self.userOperations)
        self.connect(self.buttonV, SIGNAL('clicked()'), self.viewAllData)
        
        bnlvF.addWidget(self.buttonO, 0, Qt.AlignBottom | Qt.AlignRight)
        bnlvF.addWidget(self.buttonV, 0, Qt.AlignBottom | Qt.AlignRight)
        
        # init userop
        lhmain = QHBoxLayout(self.userOp) 
        lvder  = QVBoxLayout()
        lvcen  = QVBoxLayout()
        lvizq  = QVBoxLayout()
        
        self.leDni     = QLineEdit(self.userOp) 
        self.leNames   = QLineEdit(self.userOp) 
        self.leSurname = QLineEdit(self.userOp) 
        self.leDate    = QLineEdit(self.userOp)
        
        self.leDni.setMaxLength(8)
        self.leDni.installEventFilter(FilterInteger(self))
        
        self.leNames.setMaxLength(50)
        self.leNames.installEventFilter(FilterNames(self))
        
        self.leSurname.setMaxLength(50)
        self.leSurname.installEventFilter(FilterNames(self))
        
        self.leDate.setMaxLength(10)
        self.leDate.installEventFilter(FilterDate(self))
        
        self.leDni.setToolTip('format: <b>type</b>=Int, <b>len</b>=8')
        self.leNames.setToolTip('format: <b>Nombre_1</b> {<b>Nombre_2</b> [<b>Nombre_3</b>]}')
        self.leSurname.setToolTip('format: <b>Apellido_1 Apellido_2</b>')
        self.leDate.setToolTip('Format: <b>a&ntilde;o</b>-<b>mes</b>-<b>d&iacute;a</b>')
        
        self.obuttons = [QPushButton('Buscar', self.userOp), QPushButton('Insertar', self.userOp),
            QPushButton('Actualizar', self.userOp), QPushButton('Remover', self.userOp),
            QPushButton('Aceptar', self.userOp), QPushButton('Cancelar', self.userOp)]
        
        self.obuttons[2].setEnabled(False)
        self.obuttons[3].setEnabled(False)        
        self.obuttons[4].setEnabled(False)        
        self.obuttons[5].setEnabled(False)        
        
        lvizq.addWidget(self.obuttons[0])
        lvizq.addWidget(self.obuttons[1])
        lvizq.addWidget(self.obuttons[2])
        lvizq.addWidget(self.obuttons[3])
        lvizq.addWidget(self.obuttons[4])
        lvizq.addWidget(self.obuttons[5])
        
        # clicked
        self.connect(self.obuttons[0], SIGNAL('clicked()'), self.slotSearch)
        self.connect(self.obuttons[1], SIGNAL('clicked()'), self.slotInsert)
        self.connect(self.obuttons[2], SIGNAL('clicked()'), self.slotUpdate)
        self.connect(self.obuttons[3], SIGNAL('clicked()'), self.slotRemove)
        self.connect(self.obuttons[4], SIGNAL('clicked()'), self.slotAcept)
        self.connect(self.obuttons[5], SIGNAL('clicked()'), self.slotCancel)
        
        lvcen.addWidget(self.leDni)
        lvcen.addWidget(self.leNames)
        lvcen.addWidget(self.leSurname)
        lvcen.addWidget(self.leDate)
        
        lvder.addWidget(QLabel('Dni: '))
        lvder.addWidget(QLabel('Nombres: '))
        lvder.addWidget(QLabel('Apellidos: '))
        lvder.addWidget(QLabel('Fecha Nac: '))
        
        lhmain.addLayout(lvder)
        lhmain.addLayout(lvcen)
        lhmain.addWidget(QLabel())
        f = QFrame(self.userOp);
        f.setFrameStyle(QFrame.VLine | QFrame.Sunken);
        lhmain.addWidget(f)
        lhmain.addWidget(QLabel())
        lhmain.addLayout(lvizq)
        
        # init back next
        bnlh = QHBoxLayout()        
        self.buttonR = QCommandLinkButton(QString.fromUtf8('Salir de la Aplicación'))
        self.connect(self.buttonR, SIGNAL('clicked()'), qApp, SLOT('quit()'))
        
        bnlh.addWidget(self.buttonR, 0, Qt.AlignBottom | Qt.AlignLeft)
        
        # set components central
        self.userOp.setVisible(False)
        self.dataVi.setVisible(False)
        
        ltoph = QHBoxLayout()
        ltoph.addWidget(self.preSis)
        ltoph.addWidget(self.userOp)
        ltoph.addWidget(self.dataVi)
        
        self.lcentralMain.addLayout(ltoph, 1)
        self.lcentralMain.addLayout(bnlh)
        self.centralWidget.setLayout(self.lcentralMain)
        
        # set components
        self.setCentralWidget(self.centralWidget)
        self.setMenuBar(self.menuBar)
        self.addToolBar(self.toolBar)
        self.setStatusBar(self.statusBar)
    
    def showMessage(self, message, type):
        title = self.windowTitle()
        if type == WARN:
           QMessageBox.warning(self, title, message) 
        elif type == ERROR: 
            QMessageBox.critical(self, title, message)
        else: 
           QMessageBox.information(self, title, message) 
           
    def getData(self, command):
        try:
            self.db.connect()
        except _mysql_exceptions.OperationalError, ex_c:
            self.showMessage(str(ex_c), ERROR)
            return None
        
        cursor = None
        try:
            cursor  = self.db.execute(command)
        except _mysql_exceptions.ProgrammingError, ex_q:
            self.showMessage(str(ex_q), ERROR)
            return None
        except _mysql_exceptions.OperationalError, ex_w:
            self.showMessage(str(ex_w), WARN)
            return None
        
        self.db.close()
        
        # get data 
        data = []
        while (True):
            row = cursor.fetchone()
            if row == None:
                break
            data.append(row)
        
        cursor.close()
        del cursor
        return data
    
    # slots ------------------------------------------------------------------
    def slotInicio(self):
        self.switchWidget(PRE)
        self.statusBar.showMessage('')
        
    def userOperations(self):
        self.switchWidget(OPU)
        self.statusBar.showMessage('')
        
    def viewAllData(self):
        command = "select * from " + TABLE_NAME['person']
        data = self.getData(command) 
        if data == None:
           return
        elif data == []:
            self.statusBar.showMessage('Last Action: Table Empty')
            print 'Last Action: Table Empty'
            return
        # rows and columns
        num_rows = len(data)
        num_cols = len(data[0])
        
        self.table.clearContents()
        
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)
        
        # set data table
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem()
                #item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled )
                item.setText(str(data[i][j]))
                self.table.setItem(i, j, item)
        
        self.table.setHorizontalHeaderLabels(['Dni', 'Nombres', 
                                              'Apellidos', 'Fecha Nacimiento'])
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
                
        self.reset()
        self.switchWidget(VID)
        
    def slotSearch(self):
        txtdni = self.leDni.text()
        if len(txtdni) <> 8:
            self.statusBar.showMessage('Last Action: Dni incorrecta')
            print 'Last Action: Cell Dni data incorrect'
            self.clearCells()
            return
        else:
            self.search(txtdni)
            
    def slotInsert(self):
        self.updateButtons_IUR()
        self.operationA = INSERT
        self.titleAction.setText('Operation: Insertar Nueva Persona')
        print 'Operation: Insert New Person Data Base'
        
    def slotUpdate(self):
        self.updateButtons_IUR()
        self.operationA = UPDATE
        self.titleAction.setText('Operation: Actualizar Datos Persona')
        print 'Operation: Update Person Data Base'
        
    def slotRemove(self):
        self.updateButtons_IUR()
        self.operationA = REMOVE
        self.titleAction.setText('Operation: Remover Datos Persona')
        print 'Operation: Remove Person Data Base'
        
    def slotAcept(self):
        self.chooseOperation(self.operationA)
        
    def slotCancel(self):
        self.reset()
        self.operationA = NON
    
    # -------------------------------------------------------------------------
    def updateButtons_IUR(self):
        self.obuttons[4].setEnabled(True)
        self.obuttons[5].setEnabled(True)
        for i in range(4):
            self.obuttons[i].setEnabled(False)
        self.statusBar.showMessage('')
        
    def up_reOp(self):
        self.obuttons[1].setEnabled(False)
        self.obuttons[2].setEnabled(True)
        self.obuttons[3].setEnabled(True)
        self.obuttons[4].setEnabled(False)
        self.obuttons[5].setEnabled(True)
        
    def reset(self):
        self.obuttons[0].setEnabled(True)
        self.obuttons[1].setEnabled(True)
        for i in range(2, 6):
            self.obuttons[i].setEnabled(False)
        self.titleAction.setText('')
        self.statusBar.showMessage('')
        
    def search (self, dni):
        commse = "select * from " + TABLE_NAME['person'] + " where Per_Dni='"+ str(dni) +"'"
        datav = self.getData(commse)
        if datav == None:
           self.clearCells()
           return
        elif datav == []:
            mense = "Last Action: No existe dni = [" + dni + "]" 
            self.statusBar.showMessage(mense)
            print mense
            self.clearCells()
            return
        else:
            self.leNames.setText(datav[0][1])
            self.leSurname.setText(datav[0][2])
            self.leDate.setText(str(datav[0][3]))
            self.up_reOp()
            self.statusBar.showMessage('')
            
    def chooseOperation(self, op):
        if op==NON:
            return
        
        if self.valcellWhites() == False:
            return
        ddb = [str(self.leDni.text()), str(self.leNames.text()),
            str(self.leSurname.text()), str(self.leDate.text())]
        
        commdb = "" 
        
        if op == INSERT:
            commdb = "insert into "+TABLE_NAME['person']+" values('"+ddb[0]+"','" + ddb[1] + "','" +ddb[2] + "','" + ddb[3] + "')"
        elif op == UPDATE:
            commdb = "update "+TABLE_NAME['person']+" set Per_Names='"+ddb[1]+"', Per_Surname='"+ddb[2]+"', Per_Date='"+ddb[3]+"' where Per_Dni='"+ddb[0]+"'"
        elif op == REMOVE:
            commdb = "delete from "+TABLE_NAME['person']+" where Per_Dni='"+ddb[0]+"'"
        
        print 'sql: ' + commdb
        
        try:
            self.db.connect()
        except _mysql_exceptions.OperationalError, ex_c:
            self.showMessage(str(ex_c), ERROR)
            print str(ex_c)
            return
        
        correct = True        
        
        try:
            self.db.execute(commdb)
            self.db.commit();
        except _mysql_exceptions.ProgrammingError, ex_q:
            self.showMessage(str(ex_q), ERROR)
            print str(ex_q)
            correct = False
        except _mysql_exceptions.OperationalError, ex_w:
            self.showMessage(str(ex_w), WARN)
            print str(ex_w)
            self.db.rollback();
            correct = False
        except _mysql_exceptions.IntegrityError, ex_i:
            self.showMessage(str(ex_i), WARN)
            print str(ex_i)
            correct = False
            
        self.db.close();
        
        if correct:
            self.reset();
            self.statusBar.showMessage('Operation Correct')
            print 'Operation Correct'
        
    def switchWidget(self, type):
        if self.typeWidgetA == type:
            return
        
        self.typeWidgetL = self.typeWidgetA
        self.typeWidgetA = type 
        
        if type == PRE:
            self.userOp.setVisible(False)
            self.dataVi.setVisible(False)
            self.preSis.setVisible(True)
        elif type == OPU:
            self.dataVi.setVisible(False)
            self.preSis.setVisible(False)
            self.userOp.setVisible(True)
        elif type == VID:
            self.preSis.setVisible(False)
            self.userOp.setVisible(False)
            self.dataVi.setVisible(True)
            
    def clearCells(self):
        self.leNames.setText('')
        self.leSurname.setText('')
        self.leDate.setText('')
        
    def valcellWhites(self):
        if self.leDni.text().size() == 0:
            self.statusBar.showMessage('Last Action: Dni incorrecta')
            print 'Last Action: Cell Dni incorrect'
            return False
        elif self.leNames.text().size() == 0:
            self.statusBar.showMessage('Last Action: Nombres incorrectos')
            print 'Last Action: Cell Names incorrect'
            return False 
        elif self.leSurname.text().size() == 0:
            self.statusBar.showMessage('Last Action: Apellidos incorrectos')
            print 'Last Action: Cell Surname incorrect'
            return False 
        elif self.leDate.text().size() == 0:
            self.statusBar.showMessage('Last Action: Fecha Nacimiento incorrecta')
            print 'Last Action: Cell Date incorrect'
            return False
        else:
            return True
# end_class: gui pyqt4  

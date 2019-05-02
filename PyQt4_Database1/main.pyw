# -*- coding: utf-8 -*-
"""
@author: pedroluis
main application
"""

from PyQt4.QtGui  import QApplication
from PyQt4.QtCore import QString

from pyqt4_1 import *
from database import DataBase

import _mysql_exceptions
import sys

# main ----------------------------------------

def main():    
    app = QApplication(sys.argv)
    
    w = GUI_PyQt4(QString('GUI PyQt4'))
    
    db = DataBase(HOST, USER, PASS, DB);
    try:
        db.connect()
        db.close()
    except _mysql_exceptions.DatabaseError, ex_c:
        w.showMessage(str(ex_c), ERROR)
        sys.exit(0)
    
    w.show()

    sys.exit(app.exec_())

# end main

# execute main

if __name__ == '__main__':
    
    main()
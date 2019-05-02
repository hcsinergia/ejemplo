# -*- coding: utf-8 -*-

"""
Created on Thu Aug 16 14:34:38 2012

@author: pedroluis
"""

from PyQt4.QtCore import QObject, QEvent

class FilterInteger(QObject):
    
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        
    def eventFilter(self, parent, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == 16777219:
                return False
            elif not event.text().at(0).isDigit():
                return True
        return QObject.eventFilter(self, parent, event)
        
class FilterNames(QObject):
    
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        
    def eventFilter(self, parent, event):
        if event.type() == QEvent.KeyPress: 
            if event.key() == 16777219:
                return False
            elif not event.text().at(0).isLetter() and not event.text().at(0).isSpace():
                return True
        return QObject.eventFilter(self, parent, event)
        
class FilterDate(QObject):
    
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        
    def eventFilter(self, parent, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == 16777219:
                return False
            elif not event.text().at(0).isDigit() and not (event.text() == "-"):
                return True
        return QObject.eventFilter(self, parent, event)

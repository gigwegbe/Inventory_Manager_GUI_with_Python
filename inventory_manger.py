from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets 
from PyQt5.QtCore import * 
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow 
from PyQt5.QtWidgets import QApplication 


import sys 
from os import path
from PyQt5.uic import loadUiType 

FORM_CLASS, _ = loadUiType(path.join(path.dirname('__file__'), "main.ui"))

import sqlite3 

class Main(QMainWindow, FORM_CLASS): 
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
    
    def Handel_Buttons(self):
        pass 

def main(): 
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__=='__main__': 
    main()
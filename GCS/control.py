import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("Controller.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

#ser = serial.Serial('com3',9600)



class container(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        Popen([executable, 'cansatplot - Copy.py'], creationflags=CREATE_NEW_CONSOLE)
        Popen([executable, 'try.py'], creationflags=CREATE_NEW_CONSOLE)
        
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = container()
    dv.show()
    app.exec_()


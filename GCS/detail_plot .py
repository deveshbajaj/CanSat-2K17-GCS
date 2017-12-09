from PyQt5.uic import loadUiType
import sys 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
#from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import  QApplication
import numpy as np
import time
Ui_MainWindow, QMainWindow = loadUiType('detail_plot _2.ui')

print('hi')

class Main(QMainWindow, Ui_MainWindow):
    list_main=[]
    list_alt=[]
    list_tem=[]
    i=0
    k=0
    value=0
    
    def __init__(self ):
        super(Main, self).__init__()
        self.setupUi(self)
        #self.setWindowState(QtCore.Qt.WindowMaximized)
        fig1 = Figure(facecolor='white', edgecolor='red')
        fig2 = Figure(facecolor='white', edgecolor='red')

        self.canvas1 = FigureCanvas(fig1)
        self.canvas2 = FigureCanvas(fig2)
      
        self.navi_toolbar = NavigationToolbar(self.canvas1, self)
        self.navi_toolbar_temp= NavigationToolbar(self.canvas2, self)
        
        
        self.detail_alt.addWidget(self.canvas1)
        self.detail_alt.addWidget(self.navi_toolbar)
        
        self.detail_temp.addWidget(self.canvas2)
        self.detail_temp.addWidget(self.navi_toolbar_temp)
        
        
        self.detail_temp = fig1.add_subplot('111', axisbg='white')
        self.detail_alt = fig2.add_subplot('111', axisbg='white')
        
    
        self.pushButton.clicked.connect(self.change)
        self.make_altitude()
    
        


    def change(self):
        
        self.make_altitude()
       
        
    def make_altitude(self):
        #self.plot_main.clear()
        f=open("seds_rock.txt",'r')
        yo=[j for j in f]
        for i in range(0,len(yo),2):
            data=[x for x in yo[i].split(',')]
            self.list_alt.append(data[3])
            self.list_tem.append(data[4])
        self.canvas1.draw()
        self.detail_temp.clear()
        self.detail_temp.set_title('detail_plot')
        self.detail_temp.set_xlabel('Time in sec')
        self.detail_temp.plot(self.list_alt,'b-')
        
        self.canvas2.draw()
        self.detail_alt.clear()
        self.detail_alt.set_title('detail_plot')
        self.detail_alt.set_xlabel('Time in sec')
        
        self.detail_alt.plot(self.list_tem,'g-')
        #self.plot_main.text(1.1, 1.1, 'deveesh bajaj', horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
        self.detail_temp.text(1.0, 1.0, '---- Temprature ',
            verticalalignment='bottom', horizontalalignment='right',
            transform=self.detail_temp.transAxes,
            color='blue', fontsize=15)
        self.detail_alt.text(1.0, 1.05, '---- Altitude ',
            verticalalignment='bottom', horizontalalignment='right',
            transform=self.detail_alt.transAxes,
            color='green', fontsize=15)

      
        

 
if __name__ == '__main__':
    
    import numpy as np
    app =QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

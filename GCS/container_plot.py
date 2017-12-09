from PyQt5.uic import loadUiType
import sys 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import  QApplication
import numpy as np
import time
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

Ui_MainWindow, QMainWindow = loadUiType('container_plot.ui')

#print('hi')

class Main(QMainWindow, Ui_MainWindow):
    list_main=[]
    list_alt=[]
    list_tem=[]
    i=0
    k=0
    value=0
    
    def __init__(self ):
        super(Main, self).__init__()
        #self.setWindowState(QtCore.Qt.WindowMaximized)
        
        self.setupUi(self)
        fig1 = Figure(facecolor='white', edgecolor='red')
        fig2 = Figure(facecolor='white', edgecolor='red')
        fig3 = Figure(facecolor='white', edgecolor='red')
    
        self.canvas1 = FigureCanvas(fig1)
        self.canvas2 = FigureCanvas(fig2)
        self.canvas3 = FigureCanvas(fig3)
        
        self.real_display.addWidget(self.canvas1)
        self.altitude.addWidget(self.canvas2)
        self.temp.addWidget(self.canvas3)
        
        self.plot_main = fig1.add_subplot('111', axisbg='white')
        self.plot_alt = fig2.add_subplot(111)
        self.plot_temp = fig3.add_subplot(111)

        self.make_altitude()
        self.make_temp()
        
        a=5
##        self.label_17.mousePressEvent=self.change
##        self.label_14.mousePressEvent=self.change
##        self.label_15.mousePressEvent=self.change
##        #self.label_25.mousePressEvent=self.change
##        #self.label_26.mousePressEvent=self.change
##        self.label_24.mousePressEvent=self.change
        self.label_10.mousePressEvent=self.detail_plot
        self.label_18.mousePressEvent=self.detail_plot
        self.label_21.mousePressEvent=self.detail_plot
        
        #self.widget_3.mousePressEvent=self.change
        #self.label_17.clicked.connect(self.detail_plot)
        #self.label_17.mousePressEvent = lambda: self.detail_plot
        #self.pushButton.clicked.connect(lambda: self.change())
        #self.pushButton_2.clicked.connect(lambda: self.change())
    def detail_plot(self,event):
        Popen([executable, 'detail_plot .py'], creationflags=CREATE_NEW_CONSOLE)

        
    def change(self,event):
        self.value+=1
        self.value=self.value%2
        self.plot_main.clear()
    def dev(self,event):
        print("hi devvedhidk")
        
       
        
    def make_altitude(self):
        f=open("seds_temp.txt",'r')
        yo=[j for j in f]
        data=[x for x in yo[0].split(',')]
        print(data)
        f.close()
        if len(self.list_alt)>5:
            del(self.list_alt[0])
            #print(self.list_alt)
            self.canvas2.draw()
            self.plot_alt.clear()
            self.plot_alt.plot(self.list_alt,'g')
            self.plot_alt.axes.get_xaxis().set_visible(False)
            self.plot_alt.axes.get_yaxis().set_visible(False)
            #self.label_22.setText(data[3])
            
            self.list_alt.append(int(data[3]))
        else:
            self.canvas2.draw()
            self.plot_alt.clear()
            self.plot_alt.plot(self.list_alt,'g')
            self.list_alt.append(int(data[3]))
            #self.label_22.setText(data[3])
            self.plot_alt.axes.get_xaxis().set_visible(False)
            self.plot_alt.axes.get_yaxis().set_visible(False)
            
      
        
        if self.value == 0:
            if len(self.list_alt)>5:
                self.canvas1.draw()
                self.plot_main.clear()
                #self.plot_main.set_title('Altitude')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Altitide in meter')
                self.plot_main.plot(self.list_alt,'g')
                #self.plot_main.text(0.9, 0.9, 'Altitide %s m'%str(data[3]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
##                self.label_31.setText(data[4])
##        
##                self.label_30.setText(data[2])
##
##                self.label_33.setText(data[3])
##                    
##                self.label_32.setText(data[0])
##                    
##                self.label_34.setText(data[1])
            else:
                self.canvas1.draw()
                self.plot_main.clear()
                #self.plot_main.set_title('Altitude')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Altitide in meter')
                self.plot_main.plot(self.list_alt,'g')
                #self.plot_main.text(0.9, 0.9, 'Altitide %s m'%str(data[3]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)

##                self.label_31.setText(data[4])
##        
##                self.label_30.setText(data[2])
##
##                self.label_33.setText(data[3])
##                    
##                self.label_32.setText(data[0])
##                    
##                self.label_34.setText(data[1])
##

        QtCore.QTimer.singleShot(500, lambda: self.make_altitude())
      
        
    def make_temp(self):
        fo=open("seds_temp.txt",'r')
        yoo=[j for j in fo]
        data=[x for x in yoo[0].split(',')]
        fo.close()
        self.list_tem.append(int(data[2]))
        if len(self.list_tem)>5:
            del(self.list_tem[0])
            
            self.k+=2
            self.canvas3.draw()
            self.plot_temp.clear()
            self.plot_temp.plot(self.list_tem,'b')
            self.plot_temp.axes.get_xaxis().set_visible(False)
            self.plot_temp.axes.get_yaxis().set_visible(False)
            #self.label_26.setText(data[2])
        else:
            self.k+=2
            self.canvas3.draw()
            self.plot_temp.clear()
            self.plot_temp.plot(self.list_tem,'b')
            self.plot_temp.axes.get_xaxis().set_visible(False)
            self.plot_temp.axes.get_yaxis().set_visible(False)
            #self.label_26.setText(data[2])
            
        
        if self.value == 1:
            if len(self.list_tem)>5:
                
                self.canvas1.draw()
                self.plot_main.clear()
                #self.plot_main.set_title('Temprature')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Temprature in Kelvin')
                self.plot_main.plot(self.list_tem,'b')
                #self.plot_main.text(0.9, 0.9, 'Temprature %s K'%str(data[2]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
##                self.label_31.setText(data[4])
##        
##                self.label_30.setText(data[2])
##
##                self.label_33.setText(data[3])
##                    
##                self.label_32.setText(data[0])
##                    
##                self.label_34.setText(data[1])
            else :
                
                self.canvas1.draw()
                self.plot_main.clear()
                #self.plot_main.set_title('Temprature')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Temprature in Kelvin')
                self.plot_main.plot(self.list_tem,'b')
                #self.plot_main.text(0.9, 0.9, 'Temprature %s K'%str(data[2]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
##                self.label_31.setText(data[4])
##        
##                self.label_30.setText(data[2])
##
##                self.label_33.setText(data[3])
##                    
##                self.label_32.setText(data[0])
##                    
##                self.label_34.setText(data[1])
##                
        QtCore.QTimer.singleShot(500, lambda: self.make_temp())
        
 
if __name__ == '__main__':
    
    import numpy as np
    app =QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

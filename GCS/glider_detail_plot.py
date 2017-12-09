from PyQt5.uic import loadUiType
import sys 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
#from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import  QApplication
import numpy as np
import time
Ui_MainWindow, QMainWindow = loadUiType('glider_detail_plot.ui')



class Main(QMainWindow, Ui_MainWindow):
    list_alt=[]
    list_tem=[]
    list_pre=[]
    list_speed=[]
    list_heading=[]
    list_voltage=[]
    i=0
    k=0
    value=0
    
    def __init__(self ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        fig1 = Figure(facecolor='white', edgecolor='red')
        fig2 = Figure(facecolor='white', edgecolor='red')
        fig3 = Figure(facecolor='white', edgecolor='red')
        
        fig4 = Figure(facecolor='white', edgecolor='red')
        fig5 = Figure(facecolor='white', edgecolor='red')
        fig6 = Figure(facecolor='white', edgecolor='red')

        self.canvas1 = FigureCanvas(fig1)
        self.canvas2 = FigureCanvas(fig2)
        self.canvas3 = FigureCanvas(fig3)
        self.canvas4 = FigureCanvas(fig4)
        self.canvas5 = FigureCanvas(fig5)
        self.canvas6 = FigureCanvas(fig6)
      
      
        self.navi_toolbar_alt = NavigationToolbar(self.canvas1, self)
        self.navi_toolbar_temp= NavigationToolbar(self.canvas2, self)
        self.navi_toolbar_pre = NavigationToolbar(self.canvas3, self)
        self.navi_toolbar_speed= NavigationToolbar(self.canvas4, self)
        self.navi_toolbar_heading= NavigationToolbar(self.canvas5, self)
        self.navi_toolbar_voltage= NavigationToolbar(self.canvas6, self)
        
        
        self.altitude.addWidget(self.canvas1)
        self.altitude.addWidget(self.navi_toolbar_alt)
        
        self.temp.addWidget(self.canvas2)
        self.temp.addWidget(self.navi_toolbar_temp)

        self.pressure.addWidget(self.canvas3)
        self.pressure.addWidget(self.navi_toolbar_pre)

        self.speed.addWidget(self.canvas4)
        self.speed.addWidget(self.navi_toolbar_speed)

        self.heading.addWidget(self.canvas5)
        self.heading.addWidget(self.navi_toolbar_heading)

        self.voltage.addWidget(self.canvas6)
        self.voltage.addWidget(self.navi_toolbar_voltage)
        
        self.detail_alt = fig1.add_subplot('111', axisbg='white')
        self.detail_temp = fig2.add_subplot('111', axisbg='white')
        self.detail_pre = fig3.add_subplot('111', axisbg='white')
        self.detail_speed = fig4.add_subplot('111', axisbg='white')                      
        self.detail_heading = fig5.add_subplot('111', axisbg='white')
        self.detail_voltage = fig6.add_subplot('111', axisbg='white')
        
    
        self.pushButton.clicked.connect(self.change)
        self.make_altitude()
    
        


    def change(self):
        
        self.make_altitude()
       
        
    def make_altitude(self):
        #self.plot_main.clear()
        """
list_alt=[]
    list_tem=[]
    list_pre=[]
    list_speed=[]
    list_heading=[]
    list_voltage=[]
    """
        f=open("seds_rock.txt",'r')
        yo=[j for j in f]
        for i in range(0,len(yo),2):
            data=[x for x in yo[i].split(',')]
            self.list_alt.append(data[3])
            self.list_tem.append(data[4])
            self.list_pre.append(data[5])
            self.list_speed.append(data[6])
            self.list_heading.append(data[7])
            self.list_voltage.append(data[0])
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
                      
        self.canvas3.draw()
        self.detail_pre.clear()
        self.detail_pre.set_title('detail_plot')
        self.detail_pre.set_xlabel('Time in sec')
        self.detail_pre.plot(self.list_alt,'r-')

        self.canvas4.draw()
        self.detail_speed.clear()
        self.detail_speed.set_title('detail_plot')
        self.detail_speed.set_xlabel('Time in sec')
        self.detail_speed.plot(self.list_alt,'c-')

        self.canvas5.draw()
        self.detail_heading.clear()
        self.detail_heading.set_title('detail_plot')
        self.detail_heading.set_xlabel('Time in sec')
        self.detail_heading.plot(self.list_alt,'m-')

        self.canvas6.draw()
        self.detail_voltage.clear()
        self.detail_voltage.set_title('detail_plot')
        self.detail_voltage.set_xlabel('Time in sec')
        self.detail_voltage.plot(self.list_alt,'k-')

                      
        self.detail_voltage.text(1.0, 1.0, '---- Temprature ',
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


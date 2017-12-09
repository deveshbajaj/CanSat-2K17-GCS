from PyQt5 import uic
from PyQt5.uic import loadUiType
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5 import  QtCore,QtGui,QtWidgets

from PyQt5.QtWidgets import  QApplication
import numpy as np
import time
import threading

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE


import os
import sys
qtCreatorFile = "cansatplot.ui" 


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
ptop=0
ttop=0
sptop=0
htop=0
vtop=0
xplot=[]
yplotp=[]
yplott=[]
yplots=[]
yploth=[]
yplotv=[]
time_count =0 
ymain=yplotp
class MyMplCanvas(FigureCanvas):
    

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.patch.set_facecolor('white')
        self.axes = self.fig.add_subplot(111)
        
        self.axes.hold(False)

        self.compute_initial_figure()

        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
##
##        FigureCanvas.setSizePolicy(self,
##                                   QtGui.QSizePolicy.Expanding,
##                                   QtGui.QSizePolicy.Expanding)
##        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, a,b,colorp,*args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1)
        self.x=a
        self.y=b
        self.c=colorp
    def compute_initial_figure(self):
        self.axes.plot([0], [0], 'r')

    def update_figure(self):
        
        self.axes.plot(self.x, self.y, color=self.c)
        
        self.draw()




class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    con_int=1
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.plot_type='pressure'
        
        self.pressure_button.mousePressEvent = self.pressure_on
        self.temp_button.mousePressEvent = self.temp_on
        self.speed_button.mousePressEvent = self.speed_on
        self.heading_button.mousePressEvent = self.heading_on
        self.voltage_button.mousePressEvent = self.voltage_on
        self.telemetry_heading.mousePressEvent = self.detail_plot
        
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        
        self.canvas_mainp = MyDynamicMplCanvas(xplot,yplotp,'#117DBB',width=8, height=5, dpi=100)
        self.mplvl.addWidget(self.canvas_mainp)
        self.temp=self.canvas_mainp
        self.telemetry_heading.setText("Pressure")
        ctimer = QtCore.QTimer(self) #update telemetery
        ctimer.timeout.connect(self.update_telemetry)
        ctimer.start(1)
        self.canvas_pressure = MyDynamicMplCanvas(xplot,yplotp,'#117DBB',self.pressure_plot, width=1.3, height=0.8, dpi=100)
        self.canvas_pressure.axes.get_xaxis().set_visible(False)
        self.canvas_pressure.axes.get_yaxis().set_visible(False)
        self.canvas_pressure.axes.spines['bottom'].set_color('#117DBB')
        self.canvas_pressure.axes.spines['top'].set_color('#117DBB')
        self.canvas_pressure.axes.spines['left'].set_color('#117DBB')
        self.canvas_pressure.axes.spines['right'].set_color('#117DBB')
        self.canvas_temp = MyDynamicMplCanvas(xplot,yplott,'#8B12AE',self.temp_plot, width=1.3, height=0.8, dpi=100)
        self.canvas_temp.axes.get_xaxis().set_visible(False)
        self.canvas_temp.axes.get_yaxis().set_visible(False)
        self.canvas_temp.axes.spines['bottom'].set_color('#8B12AE')
        self.canvas_temp.axes.spines['top'].set_color('#8B12AE')
        self.canvas_temp.axes.spines['left'].set_color('#8B12AE')
        self.canvas_temp.axes.spines['right'].set_color('#8B12AE')
        self.canvas_speed = MyDynamicMplCanvas(xplot,yplots,'#4DA60C',self.speed_plot, width=1.3, height=0.8, dpi=100)
        self.canvas_speed.axes.get_xaxis().set_visible(False)
        self.canvas_speed.axes.get_yaxis().set_visible(False)
        self.canvas_speed.axes.spines['bottom'].set_color('#4DA60C')
        self.canvas_speed.axes.spines['top'].set_color('#4DA60C')
        self.canvas_speed.axes.spines['left'].set_color('#4DA60C')
        self.canvas_speed.axes.spines['right'].set_color('#4DA60C')        
        self.canvas_heading = MyDynamicMplCanvas(xplot,yploth,'#A74F01',self.heading_plot, width=1.3, height=0.8, dpi=100)
        self.canvas_heading.axes.get_xaxis().set_visible(False)
        self.canvas_heading.axes.get_yaxis().set_visible(False)
        self.canvas_heading.axes.spines['bottom'].set_color('#A74F01')
        self.canvas_heading.axes.spines['top'].set_color('#A74F01')
        self.canvas_heading.axes.spines['left'].set_color('#A74F01')
        self.canvas_heading.axes.spines['right'].set_color('#A74F01')  
        self.canvas_voltage = MyDynamicMplCanvas(xplot,yplotv,'#dddddd',self.voltage_plot, width=1.3, height=0.8, dpi=100)
        self.canvas_voltage.axes.get_xaxis().set_visible(False)
        self.canvas_voltage.axes.get_yaxis().set_visible(False)
        self.canvas_voltage.axes.spines['bottom'].set_color('#dddddd')
        self.canvas_voltage.axes.spines['top'].set_color('#dddddd')
        self.canvas_voltage.axes.spines['left'].set_color('#dddddd')
        self.canvas_voltage.axes.spines['right'].set_color('#dddddd')
        
        self.temps=self.canvas_pressure
        self.temps.fig.patch.set_facecolor('#CDE8FF')
    def detail_plot(self,event):
        Popen([executable, 'detail_plot .py'], creationflags=CREATE_NEW_CONSOLE)
        
    def pressure_on(self,event):
        self.telemetry_heading.setText("Pressure")
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        self.temp_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.speed_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.heading_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.voltage_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.canvas_pressure.fig.patch.set_facecolor('#CDE8FF')
        self.temps.fig.patch.set_facecolor('white')
        self.canvas_mainp.setParent(self.main_plot)
        self.mplvl.removeWidget(self.temp)
        

        self.temp.close()
        
        self.canvas_mainp = MyDynamicMplCanvas(xplot,yplotp,'#117DBB',width=8, height=5, dpi=100)
        
        self.temps=self.canvas_pressure
        self.temp=self.canvas_mainp
        
        self.mplvl.addWidget(self.temp)
    def update_telemetry(self):
        self.pressure_value.setText('%.3f' %yplotp[-1])
        self.temprature_value.setText('%.3f' %yplott[-1])
        self.voltage_value.setText('%.3f' %yplotv[-1])
        self.speed_value.setText('%.3f' %yplots[-1])
        self.heading_value.setText('%.3f' %yploth[-1])
        
        
        
    def temp_on(self,event):
        self.telemetry_heading.setText("Temperature")
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.temp_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        self.speed_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.heading_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.voltage_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.canvas_temp.fig.patch.set_facecolor('#CDE8FF')
        self.temps.fig.patch.set_facecolor('white')
        self.mplvl.removeWidget(self.temp)
        self.temp.close()
        
        self.canvas_maint = MyDynamicMplCanvas(xplot,yplott,'#117DBB',width=8, height=5, dpi=100)
        
        self.temps=self.canvas_temp
        self.temp=self.canvas_maint
        
        self.mplvl.addWidget(self.temp)
        
    def speed_on(self,event):
        self.telemetry_heading.setText("Speed")
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.temp_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.speed_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        self.heading_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.voltage_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.canvas_speed.fig.patch.set_facecolor('#CDE8FF')
        self.temps.fig.patch.set_facecolor('white')
        self.mplvl.removeWidget(self.temp)
        self.temp.close()
        self.canvas_speed.fig.patch.set_facecolor('#CDE8FF')
        self.temps.fig.patch.set_facecolor('white')
        self.canvas_mains = MyDynamicMplCanvas(xplot,yplots,'#117DBB',width=8, height=5, dpi=100)
        
        self.temps=self.canvas_speed
        self.temp=self.canvas_mains
        
        self.mplvl.addWidget(self.temp)
    def heading_on(self,event):
        self.telemetry_heading.setText("Heading")
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.temp_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.speed_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.heading_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        self.voltage_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.temps.fig.patch.set_facecolor('white')
        self.canvas_heading.fig.patch.set_facecolor('#CDE8FF')
        
        self.mplvl.removeWidget(self.temp)
        self.temp.close()
        
        self.canvas_mainh = MyDynamicMplCanvas(xplot,yploth,'#117DBB',width=8, height=5, dpi=100)
        
        self.temps=self.canvas_heading
        self.temp=self.canvas_mainh
        
        self.mplvl.addWidget(self.temp)
    def voltage_on(self,event):
        self.telemetry_heading.setText("Voltage")
        self.pressure_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.temp_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.speed_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.heading_button.setStyleSheet("QLabel { background-color :rgb(255,255,255);}")
        self.voltage_button.setStyleSheet("QLabel { background-color :rgb(205,232,255);}")
        self.temps.fig.patch.set_facecolor('white')
        self.canvas_voltage.fig.patch.set_facecolor('#CDE8FF')
        self.mplvl.removeWidget(self.temp)
        self.temp.close()
        
        self.canvas_mainv = MyDynamicMplCanvas(xplot,yplotv,'#117DBB',width=8, height=5, dpi=100)
        
        self.temps=self.canvas_voltage
        self.temp=self.canvas_mainv
        
        self.mplvl.addWidget(self.temp)



app = QApplication(sys.argv)
window = MyApp()




class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        
    def run(self):
       if 1:
           
           time_count=0
           i=0
           while 1:
               
               output=[101.325+(np.sin(3.14*i/3)+np.sin(3.14*i/4)),25+(np.sin(3.14*i/3)/np.sin(3.14*i/4)),np.sin(3.14*i/3)+np.sin(3.14*i/4),np.tan(i),1/np.cos(i)]
               xplot.append(i)
               ptop=output[0]
               ttop=output[1]
               sptop=output[2]
               htop=output[3]
               vtop=output[4]
               
               yplotp.append(output[0])
               yplott.append(output[1])
               yplots.append(output[2])
               yploth.append(output[3])
               yplotv.append(output[4])
               i=i+1
               
               time.sleep(1)
               time_count=time_count+1
               
             
thread_for_keystrokes=myThread()
thread_for_keystrokes.start()                
             

window.show()
sys.exit(app.exec_())



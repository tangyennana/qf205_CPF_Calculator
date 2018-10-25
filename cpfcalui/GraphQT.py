import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from random import randint

class GraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initApp()
        self.createGraph()
        
        # create a test button to add new data
        self.button = QPushButton('Add data', self)
        self.button.clicked.connect(self.buttonCallback)
        self.button.move(500,0)
        self.currentage = 25

    def initApp(self):
        self.resize(600, 600)
        self.move(300,300)
        self.setWindowTitle('Graph')

    # function to create graph widget
    def createGraph(self):
        self.c = PlotCanvas(self, width=5, height=5)

    # test button to generate data and refresh graph. ignore
    def buttonCallback(self):
        self.c.addDataAndPlot((self.currentage, randint(100,1000), randint(100,1000),  randint(100,1000)))
        self.currentage+=1

# widget for plotting graph
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        # create empty list
        # data format: (age, current, special, medisave)
        self.data = []
        #self.data = [(25,100,100,100),(26,250,230,100), (27,300,240,120),(28,400,240,120)]
        

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self,self.fig)
        # setting parent of the graph widget to the base widget
        self.setParent(parent)
        # set size policy 
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.generate_plot()

    # after adding new data, replot the data 
    def addDataAndPlot(self, newdata):
        self.data.append(newdata)
        self.axes.clear()
        self.generate_plot()

    def addData(self, newdata):
        self.data.append(newdata)

    def generate_plot(self):
        self.axes.clear()
        if len(self.data)!=0:
            xaxis_values = [i[0] for i in self.data]
            self.axes.plot(xaxis_values,[i[1] for i in self.data], 'r-', label='Current account')
            self.axes.plot(xaxis_values,[i[2] for i in self.data], 'b-', label='Special account')
            self.axes.plot(xaxis_values,[i[3] for i in self.data], 'g-', label='Medisave')
            max_xlim = max(xaxis_values)+5 # +5 years for margin
            self.axes.set_xlim([max(min(xaxis_values), max_xlim-30), max_xlim]) # x axis shows 30 years only
            #self.axes.set_xlim([min(xaxis_values), max_xlim])
            self.axes.set_ylim([0, max([max(i[1:4]) for i in self.data])+100]) # +100 for margin
        
        # default display
        else:
            self.axes.set_xlim([0,25])
            self.axes.set_ylim([0,1000])
        
        self.axes.set_xlabel('Age in years')
        self.axes.set_ylabel('Amount of money in SGD')
        self.axes.set_title('CPF contribution over the years')
        self.axes.legend()
        self.figure.canvas.draw_idle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GraphApp()
    w.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from random import randint
import copy
from functools import reduce

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

    def addMonthlyPayment(self, monthlypayment):
        monthlypayment = copy.deepcopy(monthlypayment)
        monthlypayment = [payment*12 for payment in monthlypayment]
        self.cumMonthlyPayment = reduce(lambda c, x: c + [c[-1] + x], monthlypayment, [0])[1:]

    def refresh(self):
        self.data = []
        self.cumMonthlyPayment = []

    def generate_plot(self):
        self.axes.clear()
        if len(self.data)!=0:
            xaxis_values, ca, sa, med = zip(*self.data)
            next_xaxis_values = [(max(xaxis_values)+i+1) for i in range(len(self.cumMonthlyPayment))]
            self.axes.plot(xaxis_values, ca, 'r-', label='Current account')
            self.axes.plot(xaxis_values, sa, 'b-', label='Special account')
            self.axes.plot(xaxis_values, med, 'g-', label='Medisave')
            self.axes.plot(next_xaxis_values, self.cumMonthlyPayment, 'm-', label='Annual Payout after 55 years old')
            total_xaxis_values = list(xaxis_values)
            total_xaxis_values.extend(next_xaxis_values)
            max_xlim = max(total_xaxis_values)
            self.axes.set_xlim([max(min(total_xaxis_values), max_xlim-60), max_xlim]) # x axis shows 60 years only
            self.axes.set_ylim([0, max(list(ca)+list(sa)+list(med)+self.cumMonthlyPayment)+100]) # +100 for margin
        
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

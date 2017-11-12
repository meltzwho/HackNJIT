from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt
import numpy as np
import requests

app = QApplication([])
w = QWidget()
layout = QGridLayout(w)

def rangeRequest(startStr, endStr):
    resp = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start='+startStr+'&end='+endStr)
    #print(resp.)
    dataSet = resp.json()
    return dataSet

def arrToGraph(datDict):
    x = np.linspace(0, len(datDict['bpi']), len(datDict['bpi']))
    y = datDict['bpi'].values()
    plt.plot(x,y)

def selectionchanged():
    print(cb.currentText())
    lst.append(lst[-1]+1)
    print(lst)
    ax.clear()
    ax.plot(lst, '+-')
    canvas = FigureCanvas(figure)
    layout.addWidget(canvas, 0, 0)
    w.update()
# call funct with date range


cb = QComboBox()
cb.addItems(['TODAY', '7D', '1M', '3M', '1Y', 'ALL'])
cb.setFixedSize(75,30)
cb.activated.connect(selectionchanged)

figure = Figure()
canvas = FigureCanvas(figure)
ax = figure.gca()
ax.clear()
lst=[1,2,3]
ax.plot(lst, '+-')
layout.addWidget(canvas, 0, 0)
layout.addWidget(cb, 1, 0)

w.show()

app.exec_()

from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt
import numpy as np
import requests
from datetime import *
import time
from multiprocessing import Process
import dayDataGet
import json
import sys
from threading import Thread

app = QApplication([])
w = QWidget()
layout = QGridLayout(w)

def liveGraph(axL, figureL, canvasL):
    inF = open('dayDataFloat.txt', 'r')
    fullData = inF.read()
    data = json.loads(fullData)
    inF.close()
    x = np.linspace(0, len(data['price']), len(data['price']))
    y = data['price']
    axL.plot(x, y)
    canvasL = FigureCanvas(figureL)
    layout.addWidget(canvasL, 0, 1)
    w.update()
    return (axL, figureL, canvasL)


def graphCon(axL, figureL, canvasL):
    sendTup = (axL, figureL, canvasL)
    while True:
        sendTup = liveGraph(sendTup[0], sendTup[1], sendTup[2])
        time.sleep(60)

class refGra(Thread, sendTup):
    def run(self):
        while True:
           sendTup =  liveGraph(sendTup[0], sendTup[1], sendTup[2])
           time.sleep(60)



p1 = Process(target=dayDataGet.liveData)
def rangeRequest(startStr, endStr):
    resp = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start='+startStr+'&end='+endStr)
    dataSet = resp.json()
    return dataSet

def arrToGraph(datDict):
    x = np.linspace(0, len(datDict['bpi']), len(datDict['bpi']))
    y = sorted(datDict['bpi'])
    y = [datDict['bpi'][k] for k in y]
    ax.clear()
    ax.plot(x,y)

def selectionchanged():
    end = datetime.today()-timedelta(days=1)
    s = str(cb.currentText())
    options = {'7D':timedelta(weeks=1), '1M':timedelta(weeks=4), '3M':timedelta(weeks=12), '1Y':timedelta(weeks=52)}
    endStr = datetime.strftime(end, '%Y-%m-%d')
    if s in options:
        delta = options[s]
        startStr = datetime.strftime((end-delta), '%Y-%m-%d')
        arrToGraph(rangeRequest(startStr, endStr))
    elif s == 'ALL':
        arrToGraph(rangeRequest('2010-07-19', endStr))
    canvas = FigureCanvas(figure)
    layout.addWidget(canvas, 0, 0)
    w.update()
# call funct with date range


cb = QComboBox()
cb.addItems(['7D', '1M', '3M', '1Y', 'ALL'])
cb.setFixedSize(75,30)
cb.activated.connect(selectionchanged)

figure = Figure()
canvas = FigureCanvas(figure)
ax = figure.gca()
ax.clear()
layout.addWidget(canvas, 0, 0)
layout.addWidget(cb, 1, 0)

figureL = Figure()
canvasL = FigureCanvas(figureL)
axL = figureL.gca()
axL.clear()
layout.addWidget(canvasL, 0, 1)

#liveGraph(axL, figureL, canvasL)
#p0 = Process(graphCon(axL, figureL, canvasL))
p1.start()
def run():
    refGra(axL, figureL, canvasL).start()


w.show()

#p0.start()

app.exec_()
sys.exit()

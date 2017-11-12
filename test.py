from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app = QApplication([])
w = QWidget()
layout = QGridLayout(w)


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

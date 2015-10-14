__author__ = 'mainczjs'

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(dial, SIGNAL("valueChanged(int)"), zerospinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        self.connect(zerospinbox, SIGNAL("atzero"), self.announce)
        self.connect(zerospinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.setWindowTitle('Signals and Slots')

    def announce(selfself, zeros):
        print("ZeroSpinBox has ben at zero %d times" % zeros)


class ZeroSpinBox(QSpinBox):
    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero"), self.zeros)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

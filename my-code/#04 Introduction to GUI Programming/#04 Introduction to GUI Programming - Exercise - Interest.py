#!/usr/bin/python
# coding: UTF-8
__author__ = 'mainczjs'

import sys
import logging

from PyQt4.QtGui import *
from PyQt4.QtCore import *


# enable logging abilities
logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('Interest.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create Labels
        self.lbl_amount = QLabel("Amount:")
        self.lbl_rate = QLabel("Rate:")
        self.lbl_years = QLabel("Years:")
        self.lbl_result = QLabel("Result:")

        # Create Input Boxes
        self.box_amount = QDoubleSpinBox()
        self.box_amount.setSuffix(' €')
        self.box_amount.setRange(1.00, 1000000.00)
        self.box_amount.setSingleStep(100.00)
        self.box_amount.setValue(100.00)

        self.box_rate = QDoubleSpinBox()
        self.box_rate.setSuffix(' %')
        self.box_rate.setSingleStep(0.25)

        self.box_years = QComboBox()
        self.box_years.addItem("1 year")
        self.box_years.addItems(["{} years".format(x) for x in range(2, 26)])

        self.lbl_result_calc = QLabel()

        # Create Layout
        grid = QGridLayout()
        grid.addWidget(self.lbl_amount, 0, 0)
        grid.addWidget(self.box_amount, 0, 1)
        grid.addWidget(self.lbl_rate, 1, 0)
        grid.addWidget(self.box_rate, 1, 1)
        grid.addWidget(self.lbl_years, 2, 0)
        grid.addWidget(self.box_years, 2, 1)
        grid.addWidget(self.lbl_result, 3, 0)
        grid.addWidget(self.lbl_result_calc, 3, 1)
        self.setLayout(grid)

        # Connect Signals
        self.connect(self.box_amount, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.box_rate, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.box_years, SIGNAL("currentIndexChanged(int)"), self.update_ui)

        self.setWindowTitle("Interest Rates")
        self.update_ui()

    def update_ui(self):
        result = self.box_amount.value() * ((1 + (self.box_rate.value() / 100)) ** (self.box_years.currentIndex() + 1))
        self.lbl_result_calc.setText('{:.2f} €'.format(result))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

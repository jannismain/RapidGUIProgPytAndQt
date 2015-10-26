#!/usr/bin/env python3
# encoding: utf-8

import sys

from PyQt5.QtWidgets import *


class Form(QMdiArea):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # continue

    def funct(self):
        pass


# execute application
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

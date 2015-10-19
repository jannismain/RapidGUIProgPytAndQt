__author__ = 'mainczjs'

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        width_label = QLabel("&Width:")
        self.width_spinbox = QSpinBox()
        width_label.setBuddy(self.width_spinbox)
        self.width_spinbox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.width_spinbox.setRange(0, 24)

        self.beveled_checkbox = QCheckBox("&Beveled Edges")
        style_label = QLabel("&Style:")
        self.style_combobox = QComboBox()
        style_label.setBuddy(self.style_combobox)
        self.style_combobox.addItems(["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])

        ok_button = QPushButton("&OK")
        cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout = QGridLayout()
        layout.addWidget(width_label, 0, 0)
        layout.addWidget(self.width_spinbox, 0, 1)
        layout.addWidget(self.beveled_checkbox, 0, 2)
        layout.addWidget(style_label, 1, 0)
        layout.addWidget(self.style_combobox, 1, 1, 1, 2)
        layout.addLayout(button_layout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.connect(ok_button, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(cancel_button, SIGNAL("clicked()"), self, SLOT("reject()"))
        self.setWindowTitle("Pen Properties")


app = QApplication(sys.argv)
Form = PenPropertiesDlg()
Form.show()
app.exec_()

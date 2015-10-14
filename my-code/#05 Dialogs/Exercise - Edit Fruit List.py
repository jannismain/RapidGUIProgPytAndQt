__author__ = 'mainczjs'

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class StringListDlg(QDialog):
    def __init__(self, type, list=None, parent=None):
        super(StringListDlg, self).__init__(parent)

        self.type = type
        self.list = list

        # creating list and add content to list
        self.listWidget = QListWidget(self)
        if list is not None:
            self.listWidget.addItems(list)
            self.listWidget.setCurrentRow(0)

        buttonLayout = QVBoxLayout()
        # Creating and Wiring Buttons with For-Loop
        for text, slot in (("Add", self.add),
                           ("Edit", self.edit),
                           ("Remove", self.remove),
                           ("Up", self.up),
                           ("Down", self.down),
                           ("Sort", self.listWidget.sortItems),
                           ("Close", self.accept)):
            button = QPushButton(text)
            buttonLayout.addWidget(button)
            self.connect(button, SIGNAL("clicked()"), slot)

        # # Classical Button Creating and Wiring
        # # creating buttons
        # addButton = QPushButton("Add...")
        # editButton = QPushButton("Edit...")
        # remButton = QPushButton("Remove...")
        # upButton = QPushButton("Up")
        # downButton = QPushButton("Down")
        # sortButton = QPushButton("Sort")
        # closeButton = QPushButton("Close")
        # closeButton.setAutoDefault(True)
        # # adding buttons to layout
        # buttonLayout.addWidget(addButton)
        # buttonLayout.addWidget(editButton)
        # buttonLayout.addWidget(remButton)
        # buttonLayout.addWidget(upButton)
        # buttonLayout.addWidget(downButton)
        # buttonLayout.addWidget(sortButton)
        # buttonLayout.addWidget(closeButton)
        #
        # self.connect(sortButton, SIGNAL("clicked()"), self.listWidget.sortItems)
        # self.connect(closeButton, SIGNAL("clicked()"), self.close)
        # self.connect(addButton, SIGNAL("clicked()"), self.addFruit)

        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.setWindowTitle("Edit {} List".format(self.type))

    def add(self):
        row = self.listWidget.currentRow()
        title = "Add {}".format(self.type)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string:
            self.listWidget.insertItem(row, string)

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.currentItem()
        if item is not None:
            title = "Edit {}".format(self.type)
            string, ok = QInputDialog.getText(self, title, title, QLineEdit.Normal, item.text())
            if ok and string:
                item.setText(string)

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {}".format(
            self.type), "Remove {} `{}'?".format(
            self.type, item.text()),
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def up(self):
        row = self.listWidget.currentRow()
        if row >= 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentItem(item)

    def down(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentItem(item)

    def reject(self):
        self.accept()

    def accept(self):
        self.list = []
        for row in range(self.listWidget.count()):
            self.list.append(self.listWidget.item(row).text())
        self.emit(SIGNAL("acceptedList(QStringList)"), self.list)
        QDialog.accept(self)


class addFruitDlg(QDialog):
    def __init__(self, parent=None):
        super(addFruitDlg, self).__init__(parent)

        form = QInputDialog()
        form.setTextValue("Type...")
        form.show()


if __name__ == "__main__":
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig", "Guava", "Mango", \
             "Honeydew Melon", "Date", "Watermelon", "Tangerine", "Ugli Fruit", "Juniperberry", \
             "Kiwi", "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]

    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", fruit)
    form.exec_()
    print("\n".join([x for x in form.list]))

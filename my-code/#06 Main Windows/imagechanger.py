#!/usr/bin

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__version__ = "1.0.0"
__author__ = "mainczjs"


class MainWindow(QMdiArea):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvert = False
        self.mirroredhori = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        self.printer = None

        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

        # Set up the File, Edit and Help Menus
        fileNewAction = self.createAction("&New...", self.fileNew, QKeySequence.New, \
                                          "filenew", "Create an image file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen, QKeySequence.Open, \
                                           "fileopen", "Open a file")
        fileSaveAction = self.createAction("&Save", self.fileSave, QKeySequence.Save, \
                                           "filesave", "Save a file")
        fileSaveAsAction = self.createAction("Save &As...", self.fileSave, QKeySequence.SaveAs, \
                                             "filesave", "Save the file")
        filePrintAction = self.createAction("&Print...", self.filePrint, QKeySequence.Print, "fileprint", \
                                            "Print a file")
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q", "filequit", \
                                           "Close the application")
        editZoomAction = self.createAction("&Zoom...", self.editZoom, "Alt+Z", "editzoom", \
                                           "Zoom the page")
        editInvertAction = self.createAction("&Invert", self.editInvert, "Ctrl+I", "editinvert", \
                                             "Invert the images' colors", True, "toggled(bool)")
        editMirroredVert = self.createAction("&Mirror vertical", self.mirroredvert, "Ctrl+V", \
                                             "mirrorvert", "Mirror the image vertically", True, \
                                             "toggled(bool)")
        editMirroredHori = self.createAction("&Mirror horizontal", self.mirroredhori, "Ctrl+H", \
                                             "mirrorhori", "Mirror the image horizontally", True, \
                                             "toggled(bool)")
        mirrorGroup = QActionGroup(self)
        mirrorGroup.addAction(editMirroredHori, editMirroredVert)

        helpAbout = self.createAction("&About...", self.helpabout, None, "about", "About the developers")
        helpHelp = self.createAction("&Help...", self.helphelp, None, "help", "Get help")

        editMenu = self.menuBar().addMenu("&Edit")
        self.addActions(editMenu, (editInvertAction, editZoomAction))

        helpMenu = self.menuBar().addMenu("&Help")
        self.addActions(helpMenu, (helpAbout, helpHelp))

        fileMenu = self.menuBar().addMenu("&File")
        self.fileMenuActions = (fileNewAction,
        fileOpenAction, fileSaveAction, fileSaveAsAction, \
        None, filePrintAction, fileQuitAction)
        self.connect(self.fileMenu, SIGNAL("aboutToShow()"), self.updateFileMenu)
        self.addActions(fileMenu, (fileNewAction, fileQuitAction, fileSaveAsAction))

        mirrorMenu = editMenu.addMenu(QIcon(":/editmirror.png"), "&Mirror")
        self.addActions(mirrorMenu, (editMirroredVert, editMirroredHori))

        # Set up the toolbar
        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolBar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction, fileSaveAsAction))

        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolBar")
        self.addActions(editToolbar, (editInvertAction, editMirroredHori, editMirroredVert))
        # Spinbox for ease of use
        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setRange(1, 400)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setToolTip("Zoom the image")
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.connect(self.zoomSpinBox, SIGNAL("valueChanged(int)"), self.showImage)
        editToolbar.addWidget(self.zoomSpinBox)

        self.addActions(self.imageLabel, (editInvertAction, editMirroredHori, editMirroredVert))

        self.resetableActions = ((editInvertAction, False), (editMirroredHori, False), (editMirroredVert, False))

    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, \
                     signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeperator()
            else:
                target.addAction(action)

    def main(self):
        app = QApplication(sys.argv)
        app.setOrganizationName("Qtrac Ltd.")
        app.setOrganizationDomain("qtrac.eu")
        app.setApplicationName("Image Changer")
        app.setWindowIcon(QIcon(":/icon.png"))
        form = MainWindow()
        form.show()
        app.exec_()

        settings = QSettings()
        self.recentFiles = settings.value("Recent Files").toStringList()
        size = settings.value("MainWindow/Size", QVariant(QSize(600, 500))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position", QVariant(QPoint(0, 0))).toPoint()
        self.move(position)
        self.setWindowTitle("Image Changer")
        self.updateFileMenu()



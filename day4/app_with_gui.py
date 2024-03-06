from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from gui import Ui_MainWindow

# Learn more at:
# https://www.pythonguis.com/pyside2-tutorial/

app = QApplication(sys.argv)
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)

def clear_list():
    ui.listWidget.clear()

ui.clearButton.clicked.connect(clear_list)

w.show()
app.exec()
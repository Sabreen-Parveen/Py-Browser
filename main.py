from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import NavBar

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        # Adding Navigation Bar
        NavBar.add_navBar(self)

        # Open the window in full screen mode
        self.showMaximized()

app = QApplication(sys.argv)

# Setting Application Name
app.setApplicationName("Py-Browser")

window = MainWindow()

app.exec_()

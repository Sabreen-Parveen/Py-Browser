from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setWindowTitle("Py-Browser")

        self.browser.urlChanged.connect(self.bar_update)

        #Address Bar
        tb=QToolBar("url")        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.redirect_to_url)
        tb.addWidget(self.urlbar)
        self.addToolBar(tb)
        #-----------------------------


        self.setCentralWidget(self.browser)

        self.show()

    #Function called for navigation after pressing return
    def redirect_to_url(self): 
  
    # To get web address object 
        ads = QUrl(self.urlbar.text()) 
  
    
        if ads.scheme() == "":
            
            ads.setScheme("http")
  
     
        self.browser.setUrl(ads)

    #Function called for updating urlbar
    def bar_update(self, ads): 
  
        # web address in the box
        ts=ads.toString()
        self.urlbar.setText(ts) 
  
        # setting pointer position 
        self.urlbar.setCursorPosition(0) 

app = QApplication(sys.argv)

app.setApplicationName("Py-Browser")
window = MainWindow()

app.exec_()

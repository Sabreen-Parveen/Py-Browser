from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl

def add_navBar(main_window):
    """Add Navigation Bar"""
    nav_bar = QToolBar()
    main_window.addToolBar(nav_bar)

    # Adding back button to navigation bar
    back_button = QAction(QtGui.QIcon("Images/left-arrow.png"), 'Click to go back', main_window)
    back_button.triggered.connect(main_window.browser.back)
    nav_bar.addAction(back_button)

    # Adding forward button to navigation bar
    frwd_button = QAction(QtGui.QIcon("Images/right-arrow.png"), 'Click to go forward', main_window)
    frwd_button.triggered.connect(main_window.browser.forward)
    nav_bar.addAction(frwd_button)

    # Adding reload button to navigation bar
    reload_button = QAction(QtGui.QIcon("Images/refresh.png"), 'Refresh this page', main_window)
    reload_button.triggered.connect(main_window.browser.reload)
    nav_bar.addAction(reload_button)

    # Adding home button to navigation bar
    home_button = QAction(QtGui.QIcon("Images/home.png"), 'Home page', main_window)
    home_button.triggered.connect(lambda : main_window.browser.setUrl(QUrl('http://google.com')))
    nav_bar.addAction(home_button)

    # Adding Address Bar
    main_window.url_bar = QLineEdit()
    main_window.url_bar.returnPressed.connect(lambda : nav_to_url(main_window))
    nav_bar.addWidget(main_window.url_bar)

    # Update the URL in Address Bar
    main_window.browser.urlChanged.connect(lambda url : main_window.url_bar.setText(url.toString())or main_window.url_bar.setCursorPosition(0))


def nav_to_url(main_win):
    """Navigate to URL"""
    url = QUrl(main_win.url_bar.text()) 

    if url.scheme() == "":
        url.setScheme("http")  

    main_win.browser.setUrl(url)

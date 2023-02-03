import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget


class TabWidget(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QT Tabs')
        self.setFixedSize(QSize(500, 500))
        tabs = QTabWidget()
        tabs.setStyleSheet('background-color: green')
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)  # for mac os only
        tabs.setTabShape(QTabWidget.TabShape.Rounded)
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab1.setStyleSheet('background-color: cyan')
        tab2.setStyleSheet('background-color: blue')
        tab3.setStyleSheet('background-color: yellow')
        tabs.setFont(QFont('Times', 18))
        tabs.addTab(tab1, 'Tab 1')
        tabs.addTab(tab2, 'Tab 2')
        tabs.addTab(tab3, 'Tab 3')
        self.setCentralWidget(tabs)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidget()
    sys.exit(app.exec())

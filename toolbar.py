import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QToolBar, QApplication, QStatusBar
from PyQt6.QtGui import QIcon, QAction


class ToolBar(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QT Toolbar')
        toolbar = QToolBar('File')
        action_button = QAction(QIcon("icons/file_icon.png"), 'File', self)
        action_button.setStatusTip('open file')
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolbar.addAction(action_button)
        self.addToolBar(toolbar)
        action_button.setCheckable(True)
        self.setStatusBar(QStatusBar(self))
        menu = self.menuBar()
        menu.addAction(action_button)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToolBar()
    sys.exit(app.exec())

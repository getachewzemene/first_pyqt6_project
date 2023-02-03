import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Dialog')
        self.setWindowIcon(QIcon('incons/file_icon.png'))
        self.setGeometry(100, 100, 300, 300)
        button_open_file_dialog = QPushButton('Open File Dialog', self)
        button_open_file_dialog.move(50, 50)
        button_open_file_dialog.clicked.connect(self.open_file_dialog)
        self.setCentralWidget(button_open_file_dialog)
        self.show()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        if file_dialog.exec():
            print(file_dialog.selectedFiles())
        else:
            print('Canceled')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

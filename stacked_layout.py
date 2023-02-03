import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedLayout, QLabel
from PyQt6.QtCore import QSize


class StackLaout(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        stack_layout = QStackedLayout()
        label = QLabel('This is a label')
        label.setFixedSize(QSize(200, 200))
        label.setStyleSheet('background-color: red')
        button = QPushButton('Click me')
        button.setStyleSheet('background-color: blue')
        stack_layout.addWidget(label)
        stack_layout.addWidget(button)
        container = QWidget()
        container.setLayout(stack_layout)
        self.setCentralWidget(container)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StackLaout()
    sys.exit(app.exec())

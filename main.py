import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QPushButton, QGridLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('QT Calculator')
        grid_layout = QGridLayout()
        line_edit = QLineEdit()
        line_edit.setFixedHeight(50)
        line_edit.setFixedWidth(350)
        line_edit.setPlaceholderText('0')
        ac_button = QPushButton('ac')
        pow_button = QPushButton('x^2')
        mod_button = QPushButton('%')
        abs_button = QPushButton('|x|')
        grid_layout.addWidget(line_edit, 0, 0)
        grid_layout.addWidget(ac_button, 1, 0)
        grid_layout.addWidget(pow_button, 1, 1)
        grid_layout.addWidget(mod_button, 1, 2)
        grid_layout.addWidget(abs_button, 1, 3)
        for i in range(3, 13):
            if i == 12:
                button = QPushButton('0')
            else:
                button = QPushButton(str(i-2))
            grid_layout.addWidget(button, i // 3 + 1, i % 3)
            grid_layout.addWidget(QPushButton('+'), 2, 3)
            grid_layout.addWidget(QPushButton('-'), 3, 3)
            grid_layout.addWidget(QPushButton('*'), 4, 3)
            grid_layout.addWidget(QPushButton('/'), 5, 3)
            grid_layout.addWidget(QPushButton('='), 5, 2)
            grid_layout.addWidget(QPushButton('.'), 5, 1)
            # button.clicked.connect(
            #     self.on_button_clicked(button.text(), line_edit))
        container = QWidget()
        container.setLayout(grid_layout)
        self.setCentralWidget(container)
        self.setFixedSize(QSize(400, 400))
        # show the window
        self.show()

    # def on_button_clicked(self, value, line_edit):
    #     self.line_edit.setText(line_edit.text() + value)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())

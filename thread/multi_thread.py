from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi Thread")
        self.counter = 0
        self.l = QLabel()
        layout = QVBoxLayout()
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.l)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.show_time)

    def button_clicked(self):
        time.sleep(5)

    def show_time(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()

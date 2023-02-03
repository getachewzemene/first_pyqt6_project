from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, QRunnable, QThreadPool, pyqtSlot
import time


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        print("Thread Start")
        time.sleep(5)
        print("Thread Done")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi Thread")
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())
        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Mutli Threading is cool!")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)

        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def change_message(self):
        self.message = "OH NO"

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()

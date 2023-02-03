import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QHBoxLayout, QListWidget,
                             QCheckBox, QLineEdit, QLabel, QDateEdit, QDateTimeEdit, QComboBox, QDial, QDoubleSpinBox, QLCDNumber, QFontComboBox, QProgressBar, QSlider, QSpinBox)


class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QT Widgets')
        check_box = QCheckBox("Check me")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText('Enter your name')
        label = QLabel('This is a label')
        date_edit = QDateEdit()
        date_time_edit = QDateTimeEdit()
        combo_box = QComboBox()
        combo_box.addItems(['One', 'Two', 'Three'])
        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.InsertPolicy.InsertAtTop)
        list = QListWidget()
        list.addItems(['List1', 'List2', 'List3'])
        dial = QDial()
        double_spin_box = QDoubleSpinBox()
        lcd_number = QLCDNumber(5)
        font_box = QFontComboBox()
        progress_bar = QProgressBar()
        slider = QSlider()
        spin_box = QSpinBox()
        button = QPushButton('Click me')
        widgets = [check_box, line_edit, label, date_edit, date_time_edit, combo_box, list, dial,
                   double_spin_box, lcd_number, font_box, progress_bar, slider, spin_box, button]
    # adding wrapper layout
        vertical_layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(vertical_layout)
        for widget in widgets:
            vertical_layout.addWidget(widget)
        self.setFixedSize(QSize(500, 600))
        self.setCentralWidget(container)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())

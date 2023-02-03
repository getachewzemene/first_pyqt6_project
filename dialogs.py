import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QPushButton, QDialog,
                             QDialogButtonBox,
                             QColorDialog,
                             QInputDialog,
                             QHBoxLayout,
                             QVBoxLayout, QLabel)


class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Custom Dialog')
        self.setFixedSize(QSize(300, 300))
        self.setFont(QFont('Times', 18))
        vertical_layout = QVBoxLayout()
        label = QLabel('This is a custom dialog')
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        vertical_layout.addWidget(label)
        vertical_layout.addWidget(buttons)
        self.setLayout(vertical_layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QT Dialogs')
        self.setFixedSize(QSize(500, 500))
        self.move(300, 300)
        horizontal_layout_1 = QHBoxLayout()
        horizontal_layout_2 = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        container = QWidget()
        button_open = QPushButton('Open Dialog')
        button_integer = QPushButton('Integer Dialog')
        button_float = QPushButton('Float Dialog')
        button_color = QPushButton('Color Dialog')
        button_select = QPushButton('Select Dialog')
        button_string = QPushButton('String Dialog')
        button_text = QPushButton('Text Dialog')
        # add action to buttons
        button_open.clicked.connect(self.open_custom_dialog)
        button_integer.clicked.connect(self.open_integer_dialog)
        button_float.clicked.connect(self.open_float_dialog)
        button_color.clicked.connect(self.open_color_dialog)
        button_select.clicked.connect(self.open_select_dialog)
        button_string.clicked.connect(self.open_string_dialog)
        button_text.clicked.connect(self.open_text_dialog)
        # add buttons to layouts
        horizontal_layout_1.addWidget(button_open)
        horizontal_layout_1.addWidget(button_integer)
        horizontal_layout_1.addWidget(button_float)
        horizontal_layout_2.addWidget(button_color)
        horizontal_layout_2.addWidget(button_select)
        horizontal_layout_2.addWidget(button_string)
        horizontal_layout_2.addWidget(button_text)
        vertical_layout.addLayout(horizontal_layout_1)
        vertical_layout.addLayout(horizontal_layout_2)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        # add layout to container
        container.setLayout(vertical_layout)
        self.setCentralWidget(container)
        # show main window
        self.show()

    def open_custom_dialog(self):
        dialog = CustomDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            print('Accepted')
        else:
            print('Rejected')

    def open_integer_dialog(self):
        integer_dialog = QInputDialog(self)
        integer_dialog.setFixedSize(QSize(300, 300))
        integer_dialog.setWindowTitle('Integer Dialog')
        integer_dialog.setLabelText('Enter an integer')
        integer_dialog.setIntRange(0, 100)
        integer_dialog.setIntValue(50)
        integer_dialog.setIntStep(5)
        integer_dialog.setOkButtonText('OK')
        integer_dialog.setCancelButtonText('Cancel')
        integer_dialog.setFont(QFont('Times', 18))
        if integer_dialog.exec() == QDialog.DialogCode.Accepted:
            print(integer_dialog.intValue())
        else:
            print('Rejected')

    def open_float_dialog(self):
        float_dialog = QInputDialog(self)
        float_dialog.setFixedSize(QSize(300, 300))
        float_dialog.setWindowTitle('Float Dialog')
        float_dialog.setLabelText('Enter a float')
        float_dialog.setDoubleRange(0.0, 100.0)
        float_dialog.setDoubleValue(50.0)
        float_dialog.setDoubleDecimals(2)
        float_dialog.setOkButtonText('OK')
        float_dialog.setCancelButtonText('Cancel')
        float_dialog.setFont(QFont('Times', 18))
        if float_dialog.exec() == QDialog.DialogCode.Accepted:
            print(float_dialog.doubleValue())
        else:
            print('Rejected')

    def open_color_dialog(self):
        color_dialgog = QColorDialog(self)
        color_dialgog.setFixedSize(QSize(300, 300))
        color_dialgog.setWindowTitle('Color Dialog')
        color_dialgog.setCurrentColor(Qt.GlobalColor.red)
        color_dialgog.setOption(
            QColorDialog.ColorDialogOption.ShowAlphaChannel)
        color_dialgog.setOption(
            QColorDialog.ColorDialogOption.DontUseNativeDialog)
        color_dialgog.setOption(QColorDialog.ColorDialogOption.NoButtons)
        color_dialgog.setFont(QFont('Times', 18))
        if color_dialgog.exec() == QDialog.DialogCode.Accepted:
            print(color_dialgog.currentColor().name())
        else:
            print('Rejected')

    def open_select_dialog(self):
        select_dialog = QInputDialog(self)
        select_dialog.setFixedSize(QSize(300, 300))
        select_dialog.setWindowTitle('Select Dialog')
        select_dialog.setLabelText('Select an item')
        select_dialog.setComboBoxItems(['Item 1', 'Item 2', 'Item 3'])
        select_dialog.setOkButtonText('OK')
        select_dialog.setCancelButtonText('Cancel')
        select_dialog.setFont(QFont('Times', 18))
        if select_dialog.exec() == QDialog.DialogCode.Accepted:
            print(select_dialog.textValue())
        else:
            print('Rejected')

    def open_string_dialog(self):
        string_dialog = QInputDialog(self)
        string_dialog.setFixedSize(QSize(300, 300))
        string_dialog.setWindowTitle('String Dialog')
        string_dialog.setLabelText('Enter a string')
        string_dialog.setTextValue('Hello')
        string_dialog.setOkButtonText('OK')
        string_dialog.setCancelButtonText('Cancel')
        string_dialog.setFont(QFont('Times', 18))
        if string_dialog.exec() == QDialog.DialogCode.Accepted:
            print(string_dialog.textValue())
        else:
            print('Rejected')

    def open_text_dialog(self):
        text_dialog = QInputDialog(self)
        text_dialog.setFixedSize(QSize(300, 300))
        text_dialog.setWindowTitle('Text Dialog')
        text_dialog.setLabelText('Enter a text')
        text_dialog.setTextValue('Hello')
        text_dialog.setOkButtonText('OK')
        text_dialog.setCancelButtonText('Cancel')
        text_dialog.setFont(QFont('Times', 18))
        if text_dialog.exec() == QDialog.DialogCode.Accepted:
            print(text_dialog.textValue())
        else:
            print('Rejected')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

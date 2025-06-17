import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# Handles button actions
class Actions:
    def __init__(self, label: QLabel):
        self.label = label
        self.expression = ""

    def update_label(self):
        self.label.setText(self.expression)

    def action_append(self, char):
        self.expression += char
        self.update_label()

    def action_clear(self):
        self.expression = ""
        self.update_label()

    def action_del(self):
        self.expression = self.expression[:-1]
        self.update_label()

    def action_equal(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except:
            self.expression = "Error"
        self.update_label()


# Main Window and Buttons
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 360, 350)

        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setStyleSheet("border: 4px solid black; background: white;")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))

        self.actions = Actions(self.label)

        self.create_buttons()

        self.show()

    def create_buttons(self):
        # Button text & positions
        buttons = {
            "0": (5, 300), ".": (95, 300), "=": (275, 300),
            "1": (5, 150), "2": (95, 150), "3": (185, 150),
            "4": (5, 200), "5": (95, 200), "6": (185, 200),
            "7": (5, 250), "8": (95, 250), "9": (185, 250),
            "+": (275, 250), "-": (275, 200),
            "*": (275, 150), "/": (185, 300),
            "Clear": (5, 100), "Del": (210, 100),
        }

        for btn_text, pos in buttons.items():
            btn = QPushButton(btn_text, self)
            if btn_text == "Clear":
                btn.setGeometry(pos[0], pos[1], 200, 40)
            elif btn_text == "Del":
                btn.setGeometry(pos[0], pos[1], 145, 40)
            else:
                btn.setGeometry(pos[0], pos[1], 80, 40)

            btn.clicked.connect(lambda checked, txt=btn_text: self.handle_click(txt))

    def handle_click(self, txt):
        if txt == "Clear":
            self.actions.action_clear()
        elif txt == "Del":
            self.actions.action_del()
        elif txt == "=":
            self.actions.action_equal()
        else:
            self.actions.action_append(txt)


# Run Application
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QPushButton, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 400, 500)
        self.setWindowIcon(QIcon("calculator.webp"))

        self.currentOperation = None

        grid = QGridLayout()

        s1Label = QLabel(text="First number: ")
        self.s1LineEdit = QLineEdit()

        s2Label = QLabel(text="Second number: ")
        self.s2LineEdit = QLineEdit()

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Choose")
        self.comboBox.model().item(0).setEnabled(False)
        self.comboBox.addItem("Addition")
        self.comboBox.addItem("Subtraction")
        self.comboBox.addItem("Multiplication")
        self.comboBox.addItem("Division")
        self.comboBox.currentIndexChanged.connect(self.decision)

        self.pushButton = QPushButton("Choose an Operation!")
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.clicked.connect(self.warning)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        grid.addWidget(s1Label, 0, 0)
        grid.addWidget(self.s1LineEdit, 0, 1)
        grid.addWidget(s2Label, 1, 0)
        grid.addWidget(self.s2LineEdit, 1, 1)
        grid.addWidget(self.comboBox, 2, 0, 1, 2)
        grid.addWidget(self.pushButton, 3, 0, 1, 2)
        grid.addWidget(self.textEdit, 4, 0, 1, 2)

        self.addLog("Application has been launched.")

        self.setLayout(grid)

    def addLog(self, message):
        self.textEdit.append(message)
    
    def warning(self):
        if self.currentOperation: self.pushButton.clicked.disconnect(self.warning)
        else: self.addLog("You must select an operation first!")
    
    def decision(self):
        item = self.comboBox.currentText()
        self.addLog(f"{item} operation selected!")
        self.pushButton.setText(item)

        if self.currentOperation: self.pushButton.clicked.disconnect(self.currentOperation)

        if item == "Addition": 
            self.currentOperation = self.addition
            self.pushButton.clicked.connect(self.currentOperation)
        elif item == "Subtraction": 
            self.currentOperation = self.subtraction
            self.pushButton.clicked.connect(self.currentOperation)
        elif item == "Multiplication": 
            self.currentOperation = self.multiplication
            self.pushButton.clicked.connect(self.currentOperation)
        elif item == "Division": 
            self.currentOperation = self.division
            self.pushButton.clicked.connect(self.currentOperation)
        else: 
            self.currentOperation = None
            self.addLog("How did you do that?")

    def addition(self):   
        self.s1 = self.s1LineEdit.text()
        self.s2 = self.s2LineEdit.text()     
        try:
            s1 = float(self.s1)
            s2 = float(self.s2)
            result = s1+s2
            result = str(result)

            if result[-1] == "0":
                results = result.split(".")
                self.addLog(f"Result: {results[0]}")
            else:
                self.addLog(f"Result: {result}")

        except ValueError:
            self.addLog("Please enter valid values.")

    def subtraction(self): 
        self.s1 = self.s1LineEdit.text()
        self.s2 = self.s2LineEdit.text()
        try:
            s1 = float(self.s1)
            s2 = float(self.s2)
            result = s1-s2
            result = str(result)

            if result[-1] == "0":
                results = result.split(".")
                self.addLog(f"Result: {results[0]}")
            else:
                self.addLog(f"Result: {result}")

        except ValueError:
            self.addLog("Please enter valid values.")

    def multiplication(self):
        self.s1 = self.s1LineEdit.text()
        self.s2 = self.s2LineEdit.text()
        try:
            s1 = float(self.s1)
            s2 = float(self.s2)
            result = s1*s2
            result = str(result)

            if result[-1] == "0":
                results = result.split(".")
                self.addLog(f"Result: {results[0]}")
            else:
                self.addLog(f"Result: {result}")

        except ValueError:
            self.addLog("Please enter valid values.")

    def division(self):
        self.s1 = self.s1LineEdit.text()
        self.s2 = self.s2LineEdit.text()
        try:
            s1 = float(self.s1)
            s2 = float(self.s2)
            result = s1/s2
            result = str(result)

            if result[-1] == "0":
                results = result.split(".")
                self.addLog(f"Result: {results[0]}")
            else:
                self.addLog(f"Result: {result}")

        except ValueError:
            self.addLog("Please enter valid values.")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

from PyQt5 import QtWidgets
from home_dialog import HomeDialog

class ParentDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()

        b1 = HomeDialog()
        b2 = HomeDialog()

        layout.addWidget(b1)
        layout.addWidget(b2)

        self.setLayout(layout)
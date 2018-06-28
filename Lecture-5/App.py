from PyQt5 import QtWidgets
from parent_dialog import ParentDialog

app = QtWidgets.QApplication([])

parent = ParentDialog()

parent.show()

exit(app.exec_())
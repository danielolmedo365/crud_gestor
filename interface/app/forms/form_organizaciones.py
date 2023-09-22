from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class DialogoEmerUpdateOrgs(QDialog):
    def __init__(self, parent=None):
        self.parent=parent
        super().__init__()

        # Cargar el archivo .ui
        uic.loadUi("interface/ui/emergente_update_organizaciones.ui", self)






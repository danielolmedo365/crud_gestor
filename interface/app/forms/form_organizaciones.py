from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class DialogoEmerUpdateOrgs(QDialog):
    def __init__(self, parent=None):
        self.parent=parent
        super().__init__()      

        # Cargar el archivo .ui
        uic.loadUi("interface/ui/emergente_update_organizaciones.ui", self)
        self.pushButton.clicked.connect(self.set_id_busqueda)
        
    def set_id_busqueda(self):
        return self.lnd_id_org.text()
        






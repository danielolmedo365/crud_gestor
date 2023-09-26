from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class DialogoEmerUpdateOrgs(QDialog):
    def __init__(self, parent=None):
        self.parent=parent
        super().__init__()      

        # Cargar el archivo .ui
        uic.loadUi("interface/ui/emergente_update_organizaciones.ui", self)
        self.pbtn_ir.clicked.connect(self.get_id_busqueda)
        self.frame_2.setEnabled(False)

        
    def get_id_busqueda(self):
        return self.lnd_id_org.text()

        






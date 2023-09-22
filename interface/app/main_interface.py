from PyQt5 import QtWidgets, uic
import os
import time
from validaciones import ValidacionesOrganizaciones
from dbpostgresql import DBPostgresql
from forms.form_organizaciones import DialogoEmerUpdateOrgs

validador = ValidacionesOrganizaciones()

from dborganizaciones import DBOrganizaciones


class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('interface/ui/main.ui', self)
        # Changing the background color 
        self.setStyleSheet("background-color: #f2f2f2;")
        self.pushButton_2.clicked.connect(self.add_element_dict_data)
        self.dborganizaciones=DBOrganizaciones(self)
        self.emergente_update_organizaciones=DialogoEmerUpdateOrgs(self) 
        self.emergente_update_organizaciones.pushButton.clicked.connect(self.printea)        
        
    def check_registro_data(self,message, data_name, force = True):
        print(message)
        input_data = input()
        if not force and not input_data:
            return
        try:
            getattr(validador, f'validate{data_name.capitalize()}')(input_data)
            return input_data
        except ValueError as err:
            print(err)
            return  self.check_registro_data(message, data_name, force)
    def printea(self):
        id=self.emergente_update_organizaciones.lnd_id_org.text()
        self.label_2.setText(id)
        
    def add_element_dict_data(self):
        self.emergente_update_organizaciones.show()
        self.emergente_update_organizaciones.label_4.setText("Inserta el ID de la organizacion que quieres modificar")
        #self.id_org = self.emergente_update_organizaciones.get_id_busqueda()
               
        """
        data = {}
        nombre_organizacion = self.check_registro_data('introduce un nombre de organizacion (vacío para mantener el nombre actual):', 'nom_org', False)
        if nombre_organizacion:
            data['nom_org'] = nombre_organizacion
        """

            
        
    def update_registro(self,id_org,data):        
              
        try:
            res = self.dborganizaciones.update_org(id_org, data)
            if res:                
                self.label_2.setText(f'Estatus: {res}')
        except Exception as err:
            print(err)
            time.sleep(1)
            self.update_registro()
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainPage()
    ventana.show()
    sys.exit(app.exec_())
    
    

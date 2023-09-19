from PyQt5 import QtWidgets, uic
import os
import time
from validaciones import ValidacionesOrganizaciones

validador = ValidacionesOrganizaciones()

from dborganizaciones import DBOrganizaciones

dborganizaciones=DBOrganizaciones()





class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('interface/ui/main.ui', self)

        # Changing the background color 
        self.setStyleSheet("background-color: #f2f2f2;")
        self.pushButton.clicked.connect(self.update_registro)
        
    def editar_registro(self):
        print("Agregando nuevo registro")
        
        
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
    def update_registro(self):
        #list_contacts()

        print('Introduce el id del contacto que quieres actualizar:')
        id_org = input()
        
        
        
        
        

        data = {}
        nombre_organizacion = self.check_registro_data('introduce un nombre de organizacion (vacío para mantener los apellidos actuales):', 'nom_org', False)
        if nombre_organizacion:
            data['nom_org'] = nombre_organizacion
        
        try:
            res = dborganizaciones.update(id_org, data)
            if res:
                print('Contacto actualizado con éxito')
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
    
    

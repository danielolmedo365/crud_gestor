from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
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
        
        self.pushButton_2.clicked.connect(self.abrir_emergente_update)
        self.dborganizaciones=DBOrganizaciones(self)
        self.emergente_update_organizaciones=DialogoEmerUpdateOrgs(self) 
        self.selector_organizacion()

        
        # Configurar la tabla para no permitir la edición de celdas
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.emergente_update_organizaciones.pbtn_ir.clicked.connect(self.habilitar_edicion)
        
        self.emergente_update_organizaciones.pushButton.clicked.connect(self.update_registro)
    
      
        
                
    def check_registro_data(self,message, data_name, force = True):
        self.emergente_update_organizaciones.label_4.setText(message)
        input_data = input()
        if not force and not input_data:
            return
        try:
            getattr(validador, f'validate{data_name.capitalize()}')(input_data)
            return input_data
        except ValueError as err:
            print(err)
            return  self.check_registro_data(message, data_name, force)
        
    def abrir_emergente_update(self):
        self.emergente_update_organizaciones.show()
        self.emergente_update_organizaciones.label_4.setText("Inserta el ID de la organizacion que quieres modificar")
        self.emergente_update_organizaciones.lnd_id_org.clear()
        self.emergente_update_organizaciones.frame_2.setEnabled(False)
        self.emergente_update_organizaciones.pushButton.setEnabled(False)
        if self.id_org_actual:
            # Insertar por default el ID de la organizacion actual
            self.emergente_update_organizaciones.lnd_id_org.setText(self.id_org_actual)            

        
    def habilitar_edicion(self):
        id_org=self.emergente_update_organizaciones.get_id_busqueda()
        df_organizaciones=self.df_organizaciones
        filtrado=df_organizaciones[df_organizaciones['id_org'] == id_org]
        if not filtrado.empty:
            print(filtrado)
            id_org_valido=id_org
            self.emergente_update_organizaciones.frame_2.setEnabled(True)        
            self.emergente_update_organizaciones.label_4.setText(f'{id_org} ES UN ID VALIDO')
            self.emergente_update_organizaciones.pushButton.setEnabled(True)
        else:
            self.emergente_update_organizaciones.label_4.setText(f'{id_org} NO ES UN ID VALIDO')
            self.emergente_update_organizaciones.frame_2.setEnabled(False)
            self.emergente_update_organizaciones.pushButton.setEnabled(False)
       
    def update_registro(self):
        id_org=0                    
        data = {}
        nombre_organizacion = self.check_registro_data('introduce un nombre de organizacion (vacío para mantener el nombre actual):', 'nom_org', False)
        if nombre_organizacion:
            data['nom_org'] = nombre_organizacion     
        
        try:
            res = self.dborganizaciones.update_org(id_org, data)
            if res:                
                self.label_2.setText(f'Estatus: {res}')
        except Exception as err:
            print(err)
            time.sleep(1)
            self.update_registro()


    
    def selector_organizacion(self):
        
        try:
            self.df_organizaciones=self.dborganizaciones.get_df_orgs()
            self.insertar_columna_en_combobox(self.comboBox,self.df_organizaciones, 'nom_org')
            self.insertar_dataframe_en_tabla()      
            self.comboBox.currentIndexChanged.connect(self.insertar_dataframe_en_tabla) 
        except Exception as e:
            self.label_2.setText(f'Estatus: Error{e}')
            
   
        
    
    def insertar_dataframe_en_tabla(self):
        opcion_seleccionada = self.comboBox.currentText()
        self.id_current_organization = self.df_organizaciones.loc[self.df_organizaciones['nom_org'] == opcion_seleccionada]
        if opcion_seleccionada != "Todas las organizaciones":
            self.id_org_actual = self.id_current_organization['id_org'].values[0]
            dataframe=self.dborganizaciones.get_df_orgs(id=self.id_org_actual)        
        else:
            self.id_org_actual=None
            dataframe=self.dborganizaciones.get_df_orgs()
        # Obtener el número de filas y columnas del DataFrame
        self.label_3.setText(f'ID de la organización actual: {self.id_org_actual}')
        
        num_filas, num_columnas = dataframe.shape

        # Configurar la tabla para tener el mismo número de filas y columnas que el DataFrame
        self.tableWidget.setRowCount(num_filas)
        self.tableWidget.setColumnCount(num_columnas)

        # Configurar los encabezados de columna con los nombres de las columnas del DataFrame
        columnas = dataframe.columns.tolist()
        self.tableWidget.setHorizontalHeaderLabels(columnas)

        # Convertir el DataFrame en una lista de listas
        data_list = dataframe.values.tolist()

        # Llenar la tabla en lotes
        for row in range(num_filas):
            for col in range(num_columnas):
                item = QTableWidgetItem(str(data_list[row][col]))
                self.tableWidget.setItem(row, col, item)
   
    def insertar_columna_en_combobox(self,comboBox_object, dataframe, columna):
        # Obtener la columna del DataFrame
        columna_data = dataframe[columna]
        # Iterar a través de los elementos de la columna y agregarlos al QComboBox
        for elemento in columna_data:
            comboBox_object.addItem(str(elemento))  
    
                   

    




        

            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainPage()
    ventana.show()
    sys.exit(app.exec_())
    
    

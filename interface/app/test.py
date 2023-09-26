import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

# Ejemplo de un DataFrame de Pandas
data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

df = pd.DataFrame(data)

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.insertar_dataframe_en_tabla(df)

    def insertar_dataframe_en_tabla(self, dataframe):
        # Obtener el número de filas y columnas del DataFrame
        num_filas, num_columnas = dataframe.shape

        # Configurar la tabla para tener el mismo número de filas y columnas que el DataFrame
        self.table_widget.setRowCount(num_filas)
        self.table_widget.setColumnCount(num_columnas)

        # Convertir el DataFrame en una lista de listas
        data_list = dataframe.values.tolist()

        # Llenar la tabla en lotes
        for row in range(num_filas):
            for col in range(num_columnas):
                item = QTableWidgetItem(str(data_list[row][col]))
                self.table_widget.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())

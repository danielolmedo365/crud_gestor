import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView
from PyQt5.QtCore import QUrl

class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia del widget QWebEngineView
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(0, 0, 800, 600)  # Establece la geometría del widget
        self.setCentralWidget(self.web_view)

        # Cargar una página web, como Google Maps
        self.web_view.setUrl(QUrl("https://www.google.com/maps"))

def main():
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

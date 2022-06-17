from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import sys
import os
import subprocess

os.chdir(os.getcwd()+'\\Desktop')
ruta = str(os.getcwd()).replace("\\", "/")
folderName = "Prueba"


class MainWindow(QWidget):
    def __init__(self):
        # Constructor de la ventana
        super().__init__()
        self.init_UI()

    def init_UI(self):
        # Configuracion de la ventana
        self.setGeometry(1000, 600, 600, 500)
        self.setWindowTitle("Web Builder")
        self.setStyleSheet('background-color: rgb(160, 160, 160);')
        self.setUpMainWindow()
        # Muestra la ventana
        self.show()

    def setUpMainWindow(self):
        def createFiles(self):
            try:
                os.mkdir(folderName)
                os.chdir(ruta+"/"+folderName)
                html_f = open('index.html', 'x')
                js_f = open('script.js', 'x')
                css_f = open('style.css', 'x')

                html_f.write('''
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Test</title>
                        <link type="text/css" href="style.css" rel="stylesheet" />
                        <script defer src="script.js">
                        </script>
                    </head>
                    <body>
                    </body>
                </html>''')

                js_f.write(''' 'strict mode' ''')

                css_f.write('''body{background:rgb(220, 220, 220)}''')

                html_f.close()
                js_f.close()
                css_f.close()
                os.chdir("../..")
                subprocess.Popen(
                    ['C:/Users/PC-INTEL/AppData/Local/Programs/Microsoft VS Code/Code.exe', '-new-tab'])
                # os.startfile("D:/Programacion/Proyectos/Py Web Builder/archivo.html") ejecutar archivo
                status_txt.setText('Status: Created')
            except FileExistsError as err:
                status_txt.setText('Status: Failed')

        # Muestra los Qlabels en la ventana principal
        status_txt = QLabel(self)
        status_txt.setGeometry(50, 60, 100, 30)
        status_txt.setText('Status:')
        status_txt.setStyleSheet(
            'background-color: rgb(240, 240, 240);padding:2px 5px')

        createBtn = QPushButton(self)
        createBtn.setStyleSheet('background-color: rgb(10, 160, 160);')
        createBtn.setText('Create')
        createBtn.setGeometry(265, 435, 90, 40)
        createBtn.clicked.connect(createFiles)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec())

# la app permite agregar tags html para crear el archivo

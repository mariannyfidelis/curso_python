import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'/c/users/maria/',
            options=QFileDialog.DontUseNativeDialog
        )


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
import sys, os  # sys нужен для передачи argv в QApplication
# sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import math
import viewsPy.cocomo_welcome_view as cocomo_welcome
import cocomo_2
import cocomo_base
import cocomo_intermediate
import cocomo_license


class CocomoWelcome(QtWidgets.QMainWindow, cocomo_welcome.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.action_3.setCheckable(True)
        self.action_3.toggled.connect(self.isShowProgrammers)
        self.action.triggered.connect(self.showDocument)
        self.pushButton.clicked.connect(self.startCocomoBase)
        self.pushButton_2.clicked.connect(self.startCocomoIntermediate)
        self.pushButton_3.clicked.connect(self.startCocomo2)

        self.action_4.triggered.connect(self.startLicenseWindow)

        self.label.hide()

    def startLicenseWindow(self):
        self.window = cocomo_license.CocomoLicense()
        self.window.show()
        # self.close()

    def showDocument(self):
        # app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
        app_dir = os.path.abspath(__file__)
        os.system(os.path.join("file.pdf"))

    def isShowProgrammers(self):
        if (self.action_3.isChecked()):
            self.label.show()
        else:
            self.label.hide()

    def startCocomoBase(self):
        self.window = cocomo_base.CocomoBase()
        self.window.show()
        self.close()

    def startCocomoIntermediate(self):
        self.window = cocomo_intermediate.CocomoIntermediate()
        self.window.show()
        self.close()

    def startCocomo2(self):
        self.window = cocomo_2.Cocomo2()
        self.window.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CocomoWelcome()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
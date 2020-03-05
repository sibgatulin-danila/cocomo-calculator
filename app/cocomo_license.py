import sys, os  # sys нужен для передачи argv в QApplication
sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import viewsPy.cocomo_license_view as cocomo_license
import cocomo_welcome

class CocomoLicense(QtWidgets.QMainWindow, cocomo_license.Ui_mainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.goMainWindow)

    def goMainWindow(self):
        self.mainWindow = cocomo_welcome.CocomoWelcome()
        # self.mainWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CocomoLicense()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
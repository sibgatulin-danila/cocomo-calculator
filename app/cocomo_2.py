import sys, os  # sys нужен для передачи argv в QApplication
sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import math
import viewsPy.cocomo_2_view as cocomo_2



class Cocomo2(QtWidgets.QMainWindow, cocomo_2.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.currentTab = 0

        # ограничение количества цифр
        self.spinBox.setRange(1, 999)

        # Начальная вкладка для отображения
        self.tabWidget.setCurrentIndex(0)

    # функционал и связи логики с отображением

        # навигация по программе
        self.tabWidget.currentChanged.connect(self.checkTabIndex)
        

    def checkTabIndex(self):
        if (self.tabWidget.currentIndex() == 7):
                self.getResult()

    def nextTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)

    def prevTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    def getResult(self):
       pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Cocomo2()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
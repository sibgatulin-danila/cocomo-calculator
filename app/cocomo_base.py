import sys, os  # sys нужен для передачи argv в QApplication
sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import math
import viewsPy.cocomo_base_view as cocomo_base
import cocomo_welcome


class CocomoBase(QtWidgets.QMainWindow, cocomo_base.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.projectType = [
            [2.4, 1.05, 2.5, 0.38],
            [3.0, 1.12, 2.5, 0.35],
            [3.6, 1.20, 2.5, 0.32],
        ]
        # Настройки и флаги
        self.difficultLevel = 0
        self.currentTab = 0

        # ограничение количества цифр
        self.spinBox.setRange(1, 999)

        # Начальная вкладка для отображения
        self.tabWidget.setCurrentIndex(0)

    # функционал и связи логики с отображением
        # Выбор уровня сложности

        self.comboBox.currentIndexChanged.connect(self.selectDifficultLvl)


        # навигация по программе
        self.pushButton.clicked.connect(self.nextTab)

        self.pushButton_3.clicked.connect(self.prevTab)
        self.pushButton_2.clicked.connect(self.nextTab)

        self.pushButton_4.clicked.connect(self.goMainWindow)

        self.tabWidget.currentChanged.connect(self.checkTabIndex)
        

    def checkTabIndex(self):
        if (self.tabWidget.currentIndex() == 2):
                self.getResult()

    def nextTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)

    def prevTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    def selectDifficultLvl(self):
        self.difficultLevel = self.comboBox.currentIndex()

    def getResult(self):
        # расчет трудоёмкости
        a = self.projectType[self.difficultLevel][0]
        size = self.spinBox.value()
        b = self.projectType[self.difficultLevel][1]
        pm = round(a * size ** b, 2)
        self.label_4.setNum(pm) 

        # расчет времени разработки
        c = self.projectType[self.difficultLevel][2]
        d = self.projectType[self.difficultLevel][3]
        tm = round(c * pm ** d, 2)
        self.label_6.setNum(tm) 

    def goMainWindow(self):
        self.mainWindow = cocomo_welcome.CocomoWelcome()
        self.mainWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CocomoBase()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
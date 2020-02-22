import sys, os  # sys нужен для передачи argv в QApplication
sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import math
import viewsPy.cocomo_intermediate_view as cocomo_intermediate



class CocomoIntermediate(QtWidgets.QMainWindow, cocomo_intermediate.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        # коэффициенты для типа продукта
        self.projectType = [
            [3.2, 1.05],
            [3.0, 1.12],
            [2.8, 1.20],
        ]

        # Атрибуты стоимости с выбором коэффициентов
        self.product = [
            [0.75, 0.88, 1.0, 1.15, 1.4],
            [0.94, 1.0, 1.08, 1.16],
            [0.7, 0.85, 1.0, 1.15, 1.30, 1.65],
        ]

        self.AO = [
            [1.0, 1.11, 1.3, 1.66],
            [1.0, 1.06, 1.21, 1.56],
            [0.85, 1.0, 1.15, 1.30],
            [0.87, 1.0, 1.07, 1.15],
        ]

        self.personal = [
            [1.46, 1.19, 1.0, 0.86, 0.71],
            [1.29, 1.13, 1.00, 0.91, 0.82],
            [1.42, 1.17, 1.00, 0.86, 0.70],
            [1.21, 1.10, 1.00, 0.9 ],
            [1.14, 1.07, 1.00, 0.95],
        ]

        self.project = [
            [1.24, 1.10, 1.00, 0.91, 0.82],
            [1.24, 1.10, 1.00, 0.91, 0.83],
            [1.23, 1.08, 1.00, 1.04, 1.10],
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

        self.pushButton_5.clicked.connect(self.prevTab)
        self.pushButton_6.clicked.connect(self.nextTab)

        self.pushButton_7.clicked.connect(self.prevTab)
        self.pushButton_8.clicked.connect(self.nextTab)

        self.pushButton_9.clicked.connect(self.prevTab)
        self.pushButton_10.clicked.connect(self.nextTab)

        self.pushButton_11.clicked.connect(self.prevTab)
        self.pushButton_12.clicked.connect(self.nextTab)

        self.pushButton_4.clicked.connect(self.prevTab)

        self.tabWidget.currentChanged.connect(self.checkTabIndex)
        

    def checkTabIndex(self):
        if (self.tabWidget.currentIndex() == 6):
                self.getResult()

    def nextTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)

    def prevTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    def selectDifficultLvl(self):
        self.difficultLevel = self.comboBox.currentIndex()

    def getResult(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CocomoIntermediate()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
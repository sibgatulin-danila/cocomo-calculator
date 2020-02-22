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
            [3.2, 1.05, 2.5, 0.38],
            [3.0, 1.12, 2.5, 0.35],
            [2.8, 1.20, 2.5, 0.32],
        ]

        # Атрибуты стоимости с выбором коэффициентов
        self.product = [
            [0.75, 0.88, 1.0, 1.15, 1.4],
            [0.94, 1.0, 1.08, 1.16],
            [0.7, 0.85, 1.0, 1.15, 1.30, 1.65],
            [1.0, 1.11, 1.3, 1.66],
            [1.0, 1.06, 1.21, 1.56],
            [0.85, 1.0, 1.15, 1.30],
            [0.87, 1.0, 1.07, 1.15],
            [1.46, 1.19, 1.0, 0.86, 0.71],
            [1.29, 1.13, 1.00, 0.91, 0.82],
            [1.42, 1.17, 1.00, 0.86, 0.70],
            [1.21, 1.10, 1.00, 0.9 ],
            [1.14, 1.07, 1.00, 0.95],
            [1.24, 1.10, 1.00, 0.91, 0.82],
            [1.24, 1.10, 1.00, 0.91, 0.83],
            [1.23, 1.08, 1.00, 1.04, 1.10],
        ]

        # Настройки и флаги
        self.difficultLevel = 0
        self.currentTab = 0

        # Параметры
        self.pars = {
            'par_1': 0,
            'par_2': 0,
            'par_3': 0,
            'par_4': 0,
            'par_5': 0,
            'par_6': 0,
            'par_7': 0,
            'par_8': 0,
            'par_9': 0,
            'par_10': 0,
            'par_11': 0,
            'par_12': 0,
            'par_13': 0,
            'par_14': 0,
            'par_15': 0,
        }
        


        # ограничение количества цифр
        self.spinBox.setRange(1, 999)

        # Начальная вкладка для отображения
        self.tabWidget.setCurrentIndex(0)

    # функционал и связи логики с отображением
        # Выбор уровня сложности
        self.comboBox.currentIndexChanged.connect(self.selectDifficultLvl)

        # Выбор рейтингов в селекторах
        self.comboBox_2.currentIndexChanged.connect(self.selectPar1)
        self.comboBox_18.currentIndexChanged.connect(self.selectPar2)
        self.comboBox_19.currentIndexChanged.connect(self.selectPar3)

        self.comboBox_7.currentIndexChanged.connect(self.selectPar4)
        self.comboBox_5.currentIndexChanged.connect(self.selectPar5)
        self.comboBox_20.currentIndexChanged.connect(self.selectPar6)
        self.comboBox_21.currentIndexChanged.connect(self.selectPar7)

        self.comboBox_11.currentIndexChanged.connect(self.selectPar8)
        self.comboBox_22.currentIndexChanged.connect(self.selectPar9)
        self.comboBox_23.currentIndexChanged.connect(self.selectPar10)
        self.comboBox_24.currentIndexChanged.connect(self.selectPar11)
        self.comboBox_25.currentIndexChanged.connect(self.selectPar12)

        self.comboBox_15.currentIndexChanged.connect(self.selectPar13)
        self.comboBox_26.currentIndexChanged.connect(self.selectPar14)
        self.comboBox_27.currentIndexChanged.connect(self.selectPar15)

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

    # Соединение селекторов
    def selectPar1(self):
        self.pars['par_1'] = self.comboBox_2.currentIndex()
        
    def selectPar2(self):
        self.pars['par_2'] = self.comboBox_18.currentIndex()

    def selectPar3(self):
        self.pars['par_3'] = self.comboBox_19.currentIndex()

    def selectPar4(self):
        self.pars['par_4'] = self.comboBox_7.currentIndex()

    def selectPar5(self):
        self.pars['par_5'] = self.comboBox_5.currentIndex()

    def selectPar6(self):
        self.pars['par_6'] = self.comboBox_20.currentIndex()

    def selectPar7(self):
        self.pars['par_7'] = self.comboBox_21.currentIndex()

    def selectPar8(self):
        self.pars['par_8'] = self.comboBox_11.currentIndex()

    def selectPar9(self):
        self.pars['par_9'] = self.comboBox_22.currentIndex()

    def selectPar10(self):
        self.pars['par_10'] = self.comboBox_23.currentIndex()

    def selectPar11(self):
        self.pars['par_11'] = self.comboBox_24.currentIndex()

    def selectPar12(self):
        self.pars['par_12'] = self.comboBox_25.currentIndex()

    def selectPar13(self):
        self.pars['par_13'] = self.comboBox_15.currentIndex()

    def selectPar14(self):
        self.pars['par_14'] = self.comboBox_26.currentIndex()

    def selectPar15(self):
        self.pars['par_15'] = self.comboBox_27.currentIndex()


    def getResult(self):
        eaf = 1.0
        size = self.spinBox.value()
        a = self.projectType[self.difficultLevel][0]
        b = self.projectType[self.difficultLevel][1]
        for i in range(len(self.product)):
            eaf *= self.product[i][self.pars['par_' + str(i + 1)]]
        
        # Расчет трудоёмкости разработки человек в месяц
        pm = math.ceil(eaf * a * size ** b)
        self.label_4.setNum(pm) 

        # Расчет времени разработки в месяцах
        c = self.projectType[self.difficultLevel][2]
        d = self.projectType[self.difficultLevel][3]
        tm = round(c * pm ** d, 2)
        self.label_6.setNum(tm) 



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CocomoIntermediate()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
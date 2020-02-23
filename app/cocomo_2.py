import sys, os  # sys нужен для передачи argv в QApplication
sys.path.append(os.path.abspath(os.path.join('..', 'viewsPy')))
from PyQt5 import QtWidgets
import math
import viewsPy.cocomo_2_view as cocomo_2
import cocomo_welcome


class Cocomo2(QtWidgets.QMainWindow, cocomo_2.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # Факторы масштаба
        self.SF = [
            [6.20, 4.96, 3.72, 2.48, 1.24, 0.00, ],
            [5.07, 4.05, 3.04, 2.03, 1.01, 0.00, ],
            [7.07, 5.65, 4.24, 2.83, 1.41, 0.00, ],
            [5.48, 4.38, 3.29, 2.19, 1.10, 0.00, ],
            [7.80, 6.24, 4.68, 3.12, 1.56, 0.00, ],
        ]

        # Для предварительной оценки
        self.A_1 = 2.94 

        # Для детальной оценки
        self.A_2 = 2.45 

        self.B = 0.91
        self.C = 3.67
        self.D = 0.28

        self.pars_sf = {
            'par_1': 0,
            'par_2': 0,
            'par_3': 0,
            'par_4': 0,
            'par_5': 0,
        }

        self.pars_first = {
            'par_1': 0,
            'par_2': 0,
            'par_3': 0,
            'par_4': 0,
            'par_5': 0,
            'par_6': 0,
            'par_7': 0,
        }

        self.pars_second = {
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
            'par_16': 0,
            'par_17': 0,
        }

        # Множители трудоёмкости предварительной оценки
        self.MT_FIRST = [
            [ 2.12, 1.62, 1.26, 1.00, 0.83, 0.63, 0.50, ],
            [ 1.59, 1.33, 1.22, 1.00, 0.87, 0.74, 0.62, ],
            [ 0.49, 0.60, 0.83, 1.00, 1.33, 1.91, 2.72, ],
            [ 0.95, 1.00, 1.07, 1.15, 1.24, ],
            [ 0.87, 1.00, 1.29, 1.81, 2.61, ],
            [ 1.43, 1.30, 1.10, 1.00, 0.87, 0.73, 0.62, ],
            [ 1.43, 1.14, 1.00, 1.00, ],
        ]

        self.MT_SECOND = [
            [ 1.42, 1.29, 1.00, 0.85, 0.71, ],
            [ 1.22, 1.10, 1.00, 0.88, 0.81, ],
            [ 1.34, 1.15, 1.00, 0.88, 0.76, ],
            [ 1.29, 1.12, 1.00, 0.90, 0.81, ],
            [ 1.19, 1.09, 1.00, 0.91, 0.85, ],
            [ 1.20, 1.09, 1.00, 0.91, 0.84, ],
            [ 0.84, 0.92, 1.00, 1.10, 1.26, ],
            [ 0.23, 1.00, 1.14, 1.28, ],
            [ 0.73, 0.87, 1.00, 1.17, 1.34, 1.74, ],
            [ 0.95, 1.00, 1.07, 1.15, 1.24, ],
            [ 0.81, 0.91, 1.00, 1.11, 1.23, ],
            [ 1.00, 1.11, 1.29, 1.63, ],
            [ 1.00, 1.05, 1.17, 1.46, ],
            [ 0.87, 1.00, 1.15, 1.30, ],
            [ 1.17, 1.09, 1.00, 0.90, 0.78, ],
            [ 1.22, 1.09, 1.00, 0.93, 0.86, 0.80, ],
            [ 1.43, 1.14, 1.00, 1.00, 1.00, ],
        ]
                

        self.currentTab = 0

        # ограничение количества цифр
        self.spinBox.setRange(1, 999999)

        # Начальная вкладка для отображения
        self.tabWidget.setCurrentIndex(0)

    # функционал и связи логики с отображением

        # навигация по программе
        self.tabWidget.currentChanged.connect(self.checkTabIndex)

        self.pushButton_2.clicked.connect(self.nextTab)

        self.pushButton_4.clicked.connect(self.prevTab)
        self.pushButton_5.clicked.connect(self.nextTab)
        
        self.pushButton.clicked.connect(lambda : self.tabWidget.setCurrentIndex(7))

        self.pushButton_6.clicked.connect(self.prevTab)
        self.pushButton_7.clicked.connect(self.nextTab)

        self.pushButton_9.clicked.connect(self.prevTab)
        self.pushButton_10.clicked.connect(self.nextTab)

        self.pushButton_11.clicked.connect(self.prevTab)
        self.pushButton_12.clicked.connect(self.nextTab)

        self.pushButton_13.clicked.connect(self.prevTab)
        self.pushButton_14.clicked.connect(self.nextTab)

        self.pushButton_15.clicked.connect(self.prevTab)
        self.pushButton_16.clicked.connect(self.nextTab)

        self.pushButton_8.clicked.connect(self.goMainWindow)

        # соединение селекторов с параметрами
        
        # pars_sf
        self.comboBox_2.currentIndexChanged.connect(self.selectParsSf1)
        self.comboBox_3.currentIndexChanged.connect(self.selectParsSf2)
        self.comboBox_4.currentIndexChanged.connect(self.selectParsSf3)
        self.comboBox_5.currentIndexChanged.connect(self.selectParsSf4)
        self.comboBox_6.currentIndexChanged.connect(self.selectParsSf5)

        # pars_first
        self.comboBox_8.currentIndexChanged.connect(self.selectParsFirst1)
        self.comboBox_10.currentIndexChanged.connect(self.selectParsFirst2)
        self.comboBox_25.currentIndexChanged.connect(self.selectParsFirst3)
        self.comboBox_7.currentIndexChanged.connect(self.selectParsFirst4)
        self.comboBox_9.currentIndexChanged.connect(self.selectParsFirst5)
        self.comboBox_11.currentIndexChanged.connect(self.selectParsFirst6)
        self.comboBox_12.currentIndexChanged.connect(self.selectParsFirst7)

        # pars_second
        self.comboBox_14.currentIndexChanged.connect(self.selectParsSecond1)
        self.comboBox_17.currentIndexChanged.connect(self.selectParsSecond2)
        self.comboBox_13.currentIndexChanged.connect(self.selectParsSecond3)
        self.comboBox_16.currentIndexChanged.connect(self.selectParsSecond4)
        self.comboBox_18.currentIndexChanged.connect(self.selectParsSecond5)
        self.comboBox_15.currentIndexChanged.connect(self.selectParsSecond6)

        self.comboBox_19.currentIndexChanged.connect(self.selectParsSecond7)
        self.comboBox_24.currentIndexChanged.connect(self.selectParsSecond8)
        self.comboBox_22.currentIndexChanged.connect(self.selectParsSecond9)
        self.comboBox_20.currentIndexChanged.connect(self.selectParsSecond10)
        self.comboBox_21.currentIndexChanged.connect(self.selectParsSecond11)

        self.comboBox_29.currentIndexChanged.connect(self.selectParsSecond12)
        self.comboBox_28.currentIndexChanged.connect(self.selectParsSecond13)
        self.comboBox_26.currentIndexChanged.connect(self.selectParsSecond14)

        self.comboBox_30.currentIndexChanged.connect(self.selectParsSecond15)
        self.comboBox_31.currentIndexChanged.connect(self.selectParsSecond16)
        self.comboBox_27.currentIndexChanged.connect(self.selectParsSecond17)


# Подбор параметров

    # pars_sf
    def selectParsSf1(self):
        self.pars_sf['par_1'] = self.comboBox_2.currentIndex()
    
    def selectParsSf2(self):
        self.pars_sf['par_2'] = self.comboBox_3.currentIndex()
    
    def selectParsSf3(self):
        self.pars_sf['par_3'] = self.comboBox_4.currentIndex()
    
    def selectParsSf4(self):
        self.pars_sf['par_4'] = self.comboBox_5.currentIndex()
    
    def selectParsSf5(self):
        self.pars_sf['par_5'] = self.comboBox_6.currentIndex()


    #pars_first
    def selectParsFirst1(self):
        self.pars_first['par_1'] = self.comboBox_8.currentIndex()

    def selectParsFirst2(self):
        self.pars_first['par_2'] = self.comboBox_10.currentIndex()

    def selectParsFirst3(self):
        self.pars_first['par_3'] = self.comboBox_25.currentIndex()

    def selectParsFirst4(self):
        self.pars_first['par_4'] = self.comboBox_7.currentIndex()

    def selectParsFirst5(self):
        self.pars_first['par_5'] = self.comboBox_9.currentIndex()

    def selectParsFirst6(self):
        self.pars_first['par_6'] = self.comboBox_11.currentIndex()

    def selectParsFirst7(self):
        self.pars_first['par_7'] = self.comboBox_12.currentIndex()


    # pars_second
    def selectParsSecond1(self):
        self.pars_second['par_1'] = self.comboBox_14.currentIndex()

    def selectParsSecond2(self):
        self.pars_second['par_2'] = self.comboBox_17.currentIndex()

    def selectParsSecond3(self):
        self.pars_second['par_3'] = self.comboBox_13.currentIndex()

    def selectParsSecond4(self):
        self.pars_second['par_4'] = self.comboBox_16.currentIndex()

    def selectParsSecond5(self):
        self.pars_second['par_5'] = self.comboBox_18.currentIndex()

    def selectParsSecond6(self):
        self.pars_second['par_6'] = self.comboBox_15.currentIndex()

    def selectParsSecond7(self):
        self.pars_second['par_7'] = self.comboBox_19.currentIndex()

    def selectParsSecond8(self):
        self.pars_second['par_8'] = self.comboBox_24.currentIndex()

    def selectParsSecond9(self):
        self.pars_second['par_9'] = self.comboBox_22.currentIndex()

    def selectParsSecond10(self):
        self.pars_second['par_10'] = self.comboBox_20.currentIndex()

    def selectParsSecond11(self):
        self.pars_second['par_11'] = self.comboBox_21.currentIndex()

    def selectParsSecond12(self):
        self.pars_second['par_12'] = self.comboBox_29.currentIndex()

    def selectParsSecond13(self):
        self.pars_second['par_13'] = self.comboBox_28.currentIndex()

    def selectParsSecond14(self):
        self.pars_second['par_14'] = self.comboBox_26.currentIndex()

    def selectParsSecond15(self):
        self.pars_second['par_15'] = self.comboBox_30.currentIndex()

    def selectParsSecond16(self):
        self.pars_second['par_16'] = self.comboBox_31.currentIndex()

    def selectParsSecond17(self):
        self.pars_second['par_17'] = self.comboBox_27.currentIndex()

    # навигация по приложению
    def checkTabIndex(self):
        if (self.tabWidget.currentIndex() == 7):
                self.getResult()

    def nextTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)

    def prevTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    # подсчет результатов
    def getResult(self):
        size = self.spinBox.value()

        sf = 0
        for i in range(len(self.SF)):
            sf += self.SF[i][self.pars_sf['par_' + str(i + 1)]]
        e = self.B + 0.01 * sf

        eaf_1 = 1
        for i in range(len(self.pars_first)):
            eaf_1 *= self.MT_FIRST[i][self.pars_first['par_' + str(i + 1)]]

        eaf_2 = 1
        for i in range(len(self.pars_second)):
            eaf_2 *= self.MT_SECOND[i][self.pars_second['par_' + str(i + 1)]]
        
        # трудоёмкость
        pm_1 = math.ceil(eaf_1 * self.A_1 * size ** e)
        self.label_40.setText(str(pm_1))

        pm_2 = math.ceil(eaf_2 * self.A_2 * size ** e)
        self.label_59.setText(str(pm_2))
        
        # Время
        sced_i_1 = len(self.MT_FIRST) - 1
        sced_1 = self.MT_FIRST[sced_i_1][self.pars_first['par_' + str(sced_i_1 + 1)]]

        sced_i_2 = len(self.MT_SECOND) - 1
        sced_2 = self.MT_SECOND[sced_i_2][self.pars_second['par_' + str(sced_i_2 + 1)]]
        
        # трудоёмкость без sced 
        eaf_1 = 1
        for i in range(len(self.pars_first) - 1):
            eaf_1 *= self.MT_FIRST[i][self.pars_first['par_' + str(i + 1)]]

        eaf_2 = 1
        for i in range(len(self.pars_second) - 1):
            eaf_2 *= self.MT_SECOND[i][self.pars_second['par_' + str(i + 1)]]
        
        pm_1 = math.ceil(eaf_1 * self.A_1 * size ** e)
        self.label_40.setText(str(pm_1))

        pm_2 = math.ceil(eaf_2 * self.A_2 * size ** e)
        self.label_59.setText(str(pm_2))

        # Время разработки
        tm_1 = round(sced_1 * self.C * pm_1 ** (self.D + 0.2 * (e - self.B)), 2)
        self.label_57.setText(str(tm_1))
        
        tm_2 = round(sced_2 * self.C * pm_2 ** (self.D + 0.2 * (e - self.B)), 2)
        self.label_53.setText(str(tm_2))

    def goMainWindow(self):
        self.mainWindow = cocomo_welcome.CocomoWelcome()
        self.mainWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Cocomo2()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cocomo-license.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(445, 313)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 425, 262))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Лицензионное соглашение"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-weight:600; color:#333333;\">ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ на программное обеспечение</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">Настоящее лицензионное соглашение (далее &quot;соглашение&quot;) является юридическим документом, заключаемым между___________________________________(физическим или юридическим лицом, далее &quot;Пользователь&quot;) и _______________________________________  (далее &quot;Автор&quot;) относительно указанного выше программного продукта (далее &quot;программа&quot; или &quot;программное обеспечение&quot;), включающего в себя программное обеспечение, записанное на соответствующих носителях или на Web-сайте &quot;Автора&quot;, любые печатные материалы и любую &quot;встроенную&quot; или электронную документацию. Устанавливая, копируя или иным образом используя программу, Вы тем самым принимаете на себя условия настоящего соглашения. Если Вы не принимаете условий данного соглашения, то Вы не имеете права использовать данную программу и ее следует незамедлительно вернуть обратно продавцу и получить обратно уплаченные деньги.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">ЛИЦЕНЗИЯ НА ПРОГРАММУ</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">Программа  защищена законами и международными соглашениями об авторских правах, а также другими законами и договорами, регулирующими отношения авторского права. Программа лицензируется, а не продается.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">1. ОБЪЕМ ЛИЦЕНЗИИ.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">Настоящее соглашение дает вам нижеследующие права:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">1.1. Использование программы. Разрешается установка одновременно на одном компьютере программы или любой предыдущей версии. Основному пользователю компьютера, на котором установлена эта копия, разрешается также создание еще одной копии исключительно для своей работы на переносном компьютере.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">1.2. Хранение и использование в сети. Разрешается хранение, установка и запуск копии программы с общедоступного устройства хранения данных (например, сервера сети). При этом для каждого компьютера, на котором установлена или запущена с сервера сети данная программа, необходимо приобрести отдельную лицензию. Лицензия на программу не допускает совместного или одновременного использования программы на разных компьютерах в количестве более указанного в п. 1.1.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2. ОПИСАНИЕ ПРОЧИХ ПРАВ И ОГРАНИЧЕНИЙ.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.1. Ограничения на вскрытие технологии, декомпиляцию и дизассемблирование. Не разрешается осуществлять вскрытие технологии, декомпиляцию и дизассемблирование программы, за исключением и только в той степени, в которой такие действия явно разрешены действующим законодательством, несмотря на наличие в соглашении данного ограничения.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.2. Разделение программы. Программа лицензируется как единое целое. Ее нельзя разделять на составляющие части для использования на нескольких компьютерах.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.3. Прокат. Не разрешается предоставлять программу в прокат или во временное пользование.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.4. Услуги по технической поддержке. Автор оказывает услуги по технической поддержке программных продуктов (далее &quot;услуги по технической поддержке&quot;). Обращение к Автору за технической поддержкой осуществляется по e-mail: _____________ , по телефону: ____________ или ICQ __________. Любые дополнительные программы и исходные тексты, переданные вам в результате оказания услуг по технической поддержке, должны рассматриваться как составная часть программы и подпадают, таким образом, под действие ограничений и условий данного соглашения. Технические данные, которые сообщаются службе технической поддержки в ходе обращения, могут быть использованы Автором для внутренних целей, включая техническую поддержку программных продуктов и разработку программного обеспечения. Автор не будет использовать данные сведения в форме, раскрывающей ваши личные сведения.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.5. Передача программы. Разрешается навсегда уступить все свои права по настоящему соглашению только вместе с продажей или передачей компьютера при условии, что Вы не сохраняете никаких копий, передаете всю программу (включая все составные части, носители и печатные материалы, любые обновления, настоящее соглашение и сертификаты подлинности, если таковые имеются), а получатель соглашается на условия данного соглашения. Если программа является обновлением (&quot;upgrade&quot;), то любая передача должна включать в себя все предыдущие версии программы.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">2.6. Прекращение действия соглашения. Без ущерба для любых других своих прав Автор может прекратить действие настоящего соглашения при несоблюдении условий и ограничений данного соглашения, что обяжет вас уничтожить все имеющиеся копии и составляющие части программы.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">3. АВТОРСКОЕ ПРАВО.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">3.1. Все права собственности и авторские права на программу (в том числе любые включенные в нее управляющие программы (applets), фотографии, анимации, видео- и звукозаписи, музыку и текст), компоненты ActiveX, сопровождающие ее печатные материалы и любые копии программы принадлежат Автору. Все права Автора на программу защищены законами и международными соглашениями об авторских правах, а также другими законами и договорами, регулирующими отношения авторского права. Следовательно, с программой необходимо обращаться, как с любым другим объектом авторского права, с тем лишь исключением, что программу разрешается установить на один компьютер и сохранить оригинал при условии, что он будет использоваться только как архив или резервная копия. Копирование сопровождающих программу печатных материалов запрещено.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">4. РАЗЛИЧНЫЕ НОСИТЕЛИ ПРОГРАММ. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">4.1. Программа может поставляться на нескольких видах носителей, а также по сети Internet исключительно с Web-сайта &quot;Автора&quot;. Независимо от их вида и емкости разрешается использовать только носители одного вида, который соответствует именно вашему компьютеру или серверу сети. Не разрешается производить установку с прочих носителей на другие компьютеры, предоставлять носители в прокат или во временное пользование или уступать их для использования в иных целях, за исключением случая полной передачи программного обеспечения, описанного выше.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; color:#333333;\">  </span></p></body></html>"))
        self.pushButton.setText(_translate("mainWindow", "Принять"))

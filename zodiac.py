from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import date

QResource.registerResource('res.qrc')

zodiac = 'Aries'

def get_zodiac_sign(date_of_birth: date) -> str:
    zodiac_signs = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini',
                    'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
    zodiac_dates = [(date(2000,1,1), date(2000,1,20)),  # Capricorn
                    (date(2000,1,21), date(2000,2,19)),  # Aquarius
                    (date(2000,2,20), date(2000,3,20)),  # Pisces
                    (date(2000,3,21), date(2000,4,20)),  # Aries
                    (date(2000,4,21), date(2000,5,21)),  # Taurus
                    (date(2000,5,22), date(2000,6,21)),  # Gemini
                    (date(2000,6,22), date(2000,7,22)),  # Cancer
                    (date(2000,7,23), date(2000,8,22)),  # Leo
                    (date(2000,8,23), date(2000,9,23)),  # Virgo
                    (date(2000,9,24), date(2000,10,23)), # Libra
                    (date(2000,10,24), date(2000,11,22)),# Scorpio
                    (date(2000,11,23), date(2000,12,21))]# Sagittarius

    for i in range(12):
        if zodiac_dates[i][0].month <= date_of_birth.month <= zodiac_dates[i][1].month:
            if zodiac_dates[i][0].month == date_of_birth.month:
                if zodiac_dates[i][0].day <= date_of_birth.day:
                    return zodiac_signs[i]
                else:
                    return zodiac_signs[i-1]
            else:
                return zodiac_signs[i]
    return "Invalid date"

class Ui_Zodiac(object):
    def openNext(self):
        self.Form = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def setupUi(self, Zodiac):
        Zodiac.setObjectName("Zodiac")
        Zodiac.resize(541, 526)
        self.centralwidget = QtWidgets.QWidget(Zodiac)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 51))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 311, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 20, 161, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 521, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openNext())
        self.pushButton.setGeometry(QtCore.QRect(430, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        Zodiac.setCentralWidget(self.centralwidget)

        self.retranslateUi(Zodiac)
        QtCore.QMetaObject.connectSlotsByName(Zodiac)

    def retranslateUi(self, Zodiac):
        _translate = QtCore.QCoreApplication.translate
        Zodiac.setWindowTitle(_translate("Zodiac", "MainWindow"))
        self.label.setText(_translate("Zodiac", "Enter your Birth Date"))
        self.label_2.setText(_translate("Zodiac", "You are a...Aries."))
        self.textBrowser.setHtml(_translate("Zodiac", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"aries.png\" /></p></body></html>"))
        self.pushButton.setText(_translate("Zodiac", "Continue"))

class Ui_Dialog(object):
    def openNext(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_SWOT()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 479)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 430, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 451, 31))
        self.label.setObjectName("label")
        self.one_sa = QtWidgets.QRadioButton(Dialog)
        self.one_sa.setGeometry(QtCore.QRect(30, 60, 131, 20))
        self.one_sa.setObjectName("one_sa")
        self.one_a = QtWidgets.QRadioButton(Dialog)
        self.one_a.setGeometry(QtCore.QRect(160, 60, 95, 20))
        self.one_a.setObjectName("one_a")
        self.one_d = QtWidgets.QRadioButton(Dialog)
        self.one_d.setGeometry(QtCore.QRect(390, 60, 95, 20))
        self.one_d.setObjectName("one_d")
        self.one_sd = QtWidgets.QRadioButton(Dialog)
        self.one_sd.setGeometry(QtCore.QRect(520, 60, 131, 20))
        self.one_sd.setObjectName("one_sd")
        self.one_n = QtWidgets.QRadioButton(Dialog)
        self.one_n.setGeometry(QtCore.QRect(260, 60, 121, 20))
        self.one_n.setObjectName("one_n")
        self.two_n = QtWidgets.QRadioButton(Dialog)
        self.two_n.setGeometry(QtCore.QRect(260, 140, 121, 20))
        self.two_n.setObjectName("two_n")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 451, 31))
        self.label_2.setObjectName("label_2")
        self.two_d = QtWidgets.QRadioButton(Dialog)
        self.two_d.setGeometry(QtCore.QRect(390, 140, 95, 20))
        self.two_d.setObjectName("two_d")
        self.two_sa = QtWidgets.QRadioButton(Dialog)
        self.two_sa.setGeometry(QtCore.QRect(30, 140, 131, 20))
        self.two_sa.setObjectName("two_sa")
        self.two_sd = QtWidgets.QRadioButton(Dialog)
        self.two_sd.setGeometry(QtCore.QRect(520, 140, 131, 20))
        self.two_sd.setObjectName("two_sd")
        self.two_a = QtWidgets.QRadioButton(Dialog)
        self.two_a.setGeometry(QtCore.QRect(160, 140, 95, 20))
        self.two_a.setObjectName("two_a")
        self.two_d_2 = QtWidgets.QRadioButton(Dialog)
        self.two_d_2.setGeometry(QtCore.QRect(390, 220, 95, 20))
        self.two_d_2.setObjectName("two_d_2")
        self.two_sd_2 = QtWidgets.QRadioButton(Dialog)
        self.two_sd_2.setGeometry(QtCore.QRect(520, 220, 131, 20))
        self.two_sd_2.setObjectName("two_sd_2")
        self.two_n_2 = QtWidgets.QRadioButton(Dialog)
        self.two_n_2.setGeometry(QtCore.QRect(260, 220, 121, 20))
        self.two_n_2.setObjectName("two_n_2")
        self.two_sa_2 = QtWidgets.QRadioButton(Dialog)
        self.two_sa_2.setGeometry(QtCore.QRect(30, 220, 131, 20))
        self.two_sa_2.setObjectName("two_sa_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 451, 31))
        self.label_3.setObjectName("label_3")
        self.two_a_2 = QtWidgets.QRadioButton(Dialog)
        self.two_a_2.setGeometry(QtCore.QRect(160, 220, 95, 20))
        self.two_a_2.setObjectName("two_a_2")
        self.two_sd_3 = QtWidgets.QRadioButton(Dialog)
        self.two_sd_3.setGeometry(QtCore.QRect(520, 300, 131, 20))
        self.two_sd_3.setObjectName("two_sd_3")
        self.two_n_3 = QtWidgets.QRadioButton(Dialog)
        self.two_n_3.setGeometry(QtCore.QRect(260, 300, 121, 20))
        self.two_n_3.setObjectName("two_n_3")
        self.two_d_3 = QtWidgets.QRadioButton(Dialog)
        self.two_d_3.setGeometry(QtCore.QRect(390, 300, 95, 20))
        self.two_d_3.setObjectName("two_d_3")
        self.two_a_3 = QtWidgets.QRadioButton(Dialog)
        self.two_a_3.setGeometry(QtCore.QRect(160, 300, 95, 20))
        self.two_a_3.setObjectName("two_a_3")
        self.two_sa_3 = QtWidgets.QRadioButton(Dialog)
        self.two_sa_3.setGeometry(QtCore.QRect(30, 300, 131, 20))
        self.two_sa_3.setObjectName("two_sa_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 451, 31))
        self.label_4.setObjectName("label_4")
        self.two_n_4 = QtWidgets.QRadioButton(Dialog)
        self.two_n_4.setGeometry(QtCore.QRect(260, 380, 121, 20))
        self.two_n_4.setObjectName("two_n_4")
        self.two_a_4 = QtWidgets.QRadioButton(Dialog)
        self.two_a_4.setGeometry(QtCore.QRect(160, 380, 95, 20))
        self.two_a_4.setObjectName("two_a_4")
        self.two_sa_4 = QtWidgets.QRadioButton(Dialog)
        self.two_sa_4.setGeometry(QtCore.QRect(30, 380, 131, 20))
        self.two_sa_4.setObjectName("two_sa_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 340, 451, 31))
        self.label_5.setObjectName("label_5")
        self.two_sd_4 = QtWidgets.QRadioButton(Dialog)
        self.two_sd_4.setGeometry(QtCore.QRect(520, 380, 131, 20))
        self.two_sd_4.setObjectName("two_sd_4")
        self.two_d_4 = QtWidgets.QRadioButton(Dialog)
        self.two_d_4.setGeometry(QtCore.QRect(390, 380, 95, 20))
        self.two_d_4.setObjectName("two_d_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.openNext) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "I am a natural leader and enjoy taking charge in group settings."))
        self.one_sa.setText(_translate("Dialog", "Strongly Agree"))
        self.one_a.setText(_translate("Dialog", "Agree"))
        self.one_d.setText(_translate("Dialog", "Disagree"))
        self.one_sd.setText(_translate("Dialog", "Strongly Disagree"))
        self.one_n.setText(_translate("Dialog", "Neutral"))
        self.two_n.setText(_translate("Dialog", "Neutral"))
        self.label_2.setText(_translate("Dialog", "I enjoy taking risks and trying new things, even if it means making mistakes."))
        self.two_d.setText(_translate("Dialog", "Disagree"))
        self.two_sa.setText(_translate("Dialog", "Strongly Agree"))
        self.two_sd.setText(_translate("Dialog", "Strongly Disagree"))
        self.two_a.setText(_translate("Dialog", "Agree"))
        self.two_d_2.setText(_translate("Dialog", "Disagree"))
        self.two_sd_2.setText(_translate("Dialog", "Strongly Disagree"))
        self.two_n_2.setText(_translate("Dialog", "Neutral"))
        self.two_sa_2.setText(_translate("Dialog", "Strongly Agree"))
        self.label_3.setText(_translate("Dialog", "I tend to act on my impulses and make decisions quickly."))
        self.two_a_2.setText(_translate("Dialog", "Agree"))
        self.two_sd_3.setText(_translate("Dialog", "Strongly Disagree"))
        self.two_n_3.setText(_translate("Dialog", "Neutral"))
        self.two_d_3.setText(_translate("Dialog", "Disagree"))
        self.two_a_3.setText(_translate("Dialog", "Agree"))
        self.two_sa_3.setText(_translate("Dialog", "Strongly Agree"))
        self.label_4.setText(_translate("Dialog", "I am competitive and enjoy being challenged."))
        self.two_n_4.setText(_translate("Dialog", "Neutral"))
        self.two_a_4.setText(_translate("Dialog", "Agree"))
        self.two_sa_4.setText(_translate("Dialog", "Strongly Agree"))
        self.label_5.setText(_translate("Dialog", "I have a strong sense of self and am confident in my abilities."))
        self.two_sd_4.setText(_translate("Dialog", "Strongly Disagree"))
        self.two_d_4.setText(_translate("Dialog", "Disagree"))

class Ui_SWOT(object):
    def openNext(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def setupUi(self, SWOT):
        SWOT.setObjectName("SWOT")
        SWOT.resize(610, 552)
        self.label = QtWidgets.QLabel(SWOT)
        self.label.setGeometry(QtCore.QRect(30, 30, 271, 211))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SWOT)
        self.label_2.setGeometry(QtCore.QRect(320, 30, 271, 211))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SWOT)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 271, 251))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SWOT)
        self.label_4.setGeometry(QtCore.QRect(320, 270, 271, 211))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(SWOT, clicked = lambda: self.openNext())
        self.pushButton.setGeometry(QtCore.QRect(490, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SWOT)
        QtCore.QMetaObject.connectSlotsByName(SWOT)

    def retranslateUi(self, SWOT):
        _translate = QtCore.QCoreApplication.translate
        SWOT.setWindowTitle(_translate("SWOT", "Form"))
        self.label.setText(_translate("SWOT", "Strengths:\n"
"\n"
"- Aries is known for their strong willpower and determination.\n"
"- They are natural leaders who are confident and assertive.\n"
"- Aries are energetic and enthusiastic, which makes them great at initiating new projects.\n"
"- They are not afraid of taking risks and are always up for a challenge.\n"
"- Aries are passionate and driven, which makes them great at pursuing their goals."))
        self.label_2.setText(_translate("SWOT", "Weaknesses:\n"
"\n"
"- Aries can be impulsive and quick-tempered, which can lead to rash decisions.\n"
"- They can be selfish and overly competitive, which can strain their relationships with others.\n"
"- Aries can struggle with patience and tend to want immediate results.\n"
"- They may have a tendency to overlook details in their haste to get things done.\n"
"- Aries can become easily bored with routine tasks and may struggle with following through on projects."))
        self.label_3.setText(_translate("SWOT", "Opportunities:\n"
"\n"
"- Aries can take advantage of their natural leadership skills to advance their careers and take on leadership positions.\n"
"- They can use their passion and energy to pursue new hobbies and interests.\n"
"- Aries can focus on developing patience and attention to detail, which can help them succeed in projects that require these skills.\n"
"- They can use their competitive nature to motivate themselves and improve their skills.\n"
"- Aries can explore opportunities for adventure and travel, which aligns with their adventurous nature."))
        self.label_4.setText(_translate("SWOT", "Threats:\n"
"\n"
"- Aries can be prone to burnout due to their high energy levels and tendency to take on too much.\n"
"- They may struggle to work collaboratively with others, which can hinder their progress.\n"
"- Aries may face challenges in situations where they are not in control or are required to follow someone else\'s lead.\n"
"- They can be perceived as aggressive or intimidating, which can negatively impact their relationships with others.\n"
"- Aries may struggle with adapting to change, which can limit their opportunities for growth and development."))
        self.pushButton.setText(_translate("SWOT", "Continue"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 420)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 491, 331))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 370, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: Form.accept)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 370, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Most compatible sign: Sagitarrius"))
        self.label_2.setText(_translate("Form", "You may find yourself feeling particularly bold and confident today, Aries. Your natural leadership skills will be in full force, and you\'ll have the energy and drive to take on any challenge that comes your way. This is a great time to start new projects, take risks, and pursue your goals with passion and enthusiasm.\n"
"\n"
"However, be mindful of your tendency to be impulsive and act before thinking things through. Take a moment to consider the consequences of your actions before making any big moves. This will help you avoid any unnecessary mistakes or setbacks.\n"
"\n"
"In matters of the heart, you may be feeling especially passionate and romantic. This is a great time to express your feelings to that special someone and let them know how much they mean to you. But make sure to communicate clearly and listen to their needs as well.\n"
"\n"
"Overall, this is a powerful and exciting time for you, Aries. Embrace the opportunities that come your way and trust in your instincts to guide you towards success."))
        self.pushButton.setText(_translate("Form", "Finish"))
        self.pushButton_2.setText(_translate("Form", "Share"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Zodiac = QtWidgets.QMainWindow()
    ui = Ui_Zodiac()
    ui.setupUi(Zodiac)
    Zodiac.show()
    sys.exit(app.exec_())
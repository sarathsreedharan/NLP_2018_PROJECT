# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sat Apr 14 20:00:30 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(1066, 837)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.location_label = QtGui.QLabel(Frame)
        self.location_label.setGeometry(QtCore.QRect(10, 140, 83, 22))
        self.location_label.setObjectName(_fromUtf8("location_label"))
        self.cards_label = QtGui.QLabel(Frame)
        self.cards_label.setGeometry(QtCore.QRect(20, 230, 83, 22))
        self.cards_label.setObjectName(_fromUtf8("cards_label"))
        self.location2_text = QtGui.QPlainTextEdit(Frame)
        self.location2_text.setGeometry(QtCore.QRect(359, 130, 256, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location2_text.sizePolicy().hasHeightForWidth())
        self.location2_text.setSizePolicy(sizePolicy)
        self.location2_text.setBaseSize(QtCore.QSize(1000, 1000))
        self.location2_text.setObjectName(_fromUtf8("location2_text"))
        self.player2_cards = QtGui.QListWidget(Frame)
        self.player2_cards.setGeometry(QtCore.QRect(360, 180, 256, 111))
        self.player2_cards.setObjectName(_fromUtf8("player2_cards"))
        self.location3_text = QtGui.QPlainTextEdit(Frame)
        self.location3_text.setGeometry(QtCore.QRect(619, 130, 256, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location3_text.sizePolicy().hasHeightForWidth())
        self.location3_text.setSizePolicy(sizePolicy)
        self.location3_text.setBaseSize(QtCore.QSize(1000, 1000))
        self.location3_text.setObjectName(_fromUtf8("location3_text"))
        self.player3_cards = QtGui.QListWidget(Frame)
        self.player3_cards.setGeometry(QtCore.QRect(620, 180, 256, 111))
        self.player3_cards.setObjectName(_fromUtf8("player3_cards"))
        self.player1_label = QtGui.QLabel(Frame)
        self.player1_label.setGeometry(QtCore.QRect(180, 90, 83, 22))
        self.player1_label.setObjectName(_fromUtf8("player1_label"))
        self.player2_label = QtGui.QLabel(Frame)
        self.player2_label.setGeometry(QtCore.QRect(440, 90, 83, 22))
        self.player2_label.setObjectName(_fromUtf8("player2_label"))
        self.player3_label = QtGui.QLabel(Frame)
        self.player3_label.setGeometry(QtCore.QRect(710, 90, 83, 22))
        self.player3_label.setObjectName(_fromUtf8("player3_label"))
        self.graph_box = QtGui.QListWidget(Frame)
        self.graph_box.setGeometry(QtCore.QRect(100, 360, 511, 401))
        self.graph_box.setObjectName(_fromUtf8("graph_box"))
        self.plan_output = QtGui.QListWidget(Frame)
        self.plan_output.setGeometry(QtCore.QRect(620, 360, 251, 401))
        self.plan_output.setObjectName(_fromUtf8("plan_output"))
        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(820, 770, 211, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.location1_text = QtGui.QPlainTextEdit(Frame)
        self.location1_text.setGeometry(QtCore.QRect(99, 130, 256, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location1_text.sizePolicy().hasHeightForWidth())
        self.location1_text.setSizePolicy(sizePolicy)
        self.location1_text.setBaseSize(QtCore.QSize(1000, 1000))
        self.location1_text.setObjectName(_fromUtf8("location1_text"))
        self.player1_cards = QtGui.QListWidget(Frame)
        self.player1_cards.setGeometry(QtCore.QRect(100, 180, 256, 111))
        self.player1_cards.setObjectName(_fromUtf8("player1_cards"))
        self.addCard1 = QtGui.QPlainTextEdit(Frame)
        self.addCard1.setGeometry(QtCore.QRect(150, 300, 161, 41))
        self.addCard1.setObjectName(_fromUtf8("addCard1"))
        self.pushButton_2 = QtGui.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 300, 41, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 300, 41, 32))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.addCard2 = QtGui.QPlainTextEdit(Frame)
        self.addCard2.setGeometry(QtCore.QRect(410, 300, 161, 41))
        self.addCard2.setObjectName(_fromUtf8("addCard2"))
        self.pushButton_4 = QtGui.QPushButton(Frame)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 300, 41, 32))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 300, 41, 32))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.addCard3 = QtGui.QPlainTextEdit(Frame)
        self.addCard3.setGeometry(QtCore.QRect(670, 300, 161, 41))
        self.addCard3.setObjectName(_fromUtf8("addCard3"))
        self.pushButton_6 = QtGui.QPushButton(Frame)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 300, 41, 32))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Frame)
        self.pushButton_7.setGeometry(QtCore.QRect(840, 300, 41, 32))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.addCard3.setPlainText("HWER")
        print (self.addCard3.toPlainText())


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.location_label.setText(_translate("Frame", "Location", None))
        self.cards_label.setText(_translate("Frame", "Cards", None))
        self.player1_label.setText(_translate("Frame", "Player 1", None))
        self.player2_label.setText(_translate("Frame", "Player 2", None))
        self.player3_label.setText(_translate("Frame", "Player 3", None))
        self.pushButton.setText(_translate("Frame", "PushButton", None))
        self.pushButton_2.setText(_translate("Frame", "+", None))
        self.pushButton_3.setText(_translate("Frame", "---", None))
        self.pushButton_4.setText(_translate("Frame", "---", None))
        self.pushButton_5.setText(_translate("Frame", "+", None))
        self.pushButton_6.setText(_translate("Frame", "---", None))
        self.pushButton_7.setText(_translate("Frame", "+", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())


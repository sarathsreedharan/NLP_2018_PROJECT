# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sun Apr 15 22:45:58 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, SIGNAL
import Data

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
    def setupUi(self, Frame, model, backend):
        self.model = model
        self.Frame = Frame
        self.backend = backend
        self.Frame.setObjectName(_fromUtf8("self.Frame"))
        self.Frame.resize(1066, 837)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy)
        self.Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.location_label = QtGui.QLabel(self.Frame)
        self.location_label.setGeometry(QtCore.QRect(10, 140, 83, 22))
        self.location_label.setObjectName(_fromUtf8("location_label"))

        self.cards_label = QtGui.QLabel(self.Frame)
        self.cards_label.setGeometry(QtCore.QRect(20, 230, 83, 22))
        self.cards_label.setObjectName(_fromUtf8("cards_label"))

        self.graph_box = QtGui.QPlainTextEdit(self.Frame)
        self.graph_box.setGeometry(QtCore.QRect(100, 360, 511, 401))
        self.graph_box.setObjectName(_fromUtf8("graph_box"))

        self.plan_output = QtGui.QPlainTextEdit(self.Frame)
        self.plan_output.setGeometry(QtCore.QRect(620, 360, 251, 401))
        self.plan_output.setObjectName(_fromUtf8("plan_output"))

        self.assistButton = QtGui.QPushButton(self.Frame)
        self.assistButton.setGeometry(QtCore.QRect(820, 770, 211, 51))
        self.assistButton.setObjectName(_fromUtf8("pushButton"))

        self.executeButton = QtGui.QPushButton(Frame)
        self.executeButton.setGeometry(QtCore.QRect(900, 510, 141, 51))
        self.executeButton.setObjectName(_fromUtf8("executeButton"))

        self.updateButton = QtGui.QPushButton(Frame)
        self.updateButton.setGeometry(QtCore.QRect(900, 210, 141, 51))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))

        self.explainButton = QtGui.QPushButton(Frame)
        self.explainButton.setGeometry(QtCore.QRect(900, 580, 141, 51))
        self.explainButton.setObjectName(_fromUtf8("explainButton"))

        self.textInput = QtGui.QPlainTextEdit(Frame)
        self.textInput.setGeometry(QtCore.QRect(330, 780, 481, 41))
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.textInput.setPlainText("How can player1 to to delhi?")

        self.my_question_label = QtGui.QLabel(Frame)
        self.my_question_label.setGeometry(QtCore.QRect(202, 790, 121, 22))
        self.my_question_label.setObjectName(_fromUtf8("my_question_label"))


        QObject.connect(self.assistButton, SIGNAL("clicked()"), lambda obj={"func": "get_assistance", "args": 'plan'}: self.onClicked(obj))
        QObject.connect(self.executeButton, SIGNAL("clicked()"), lambda obj={"func": "execute_plan", "args": ''}: self.onClicked(obj))
        QObject.connect(self.updateButton, SIGNAL("clicked()"), lambda obj={"func": "update_locations", "args": ''}: self.onClicked(obj))
        QObject.connect(self.explainButton, SIGNAL("clicked()"), lambda obj={"func": "get_assistance", "args": 'explain'}: self.onClicked(obj))

        self.createPlayerLabels(3)
        self.createComboBoxes(3)
        self.createCardDecks(3)

        self.retranslateUi(self.Frame)

        self.cityList = []

        self.doRepaint(model)

        QtCore.QMetaObject.connectSlotsByName(self.Frame)

    def createPlayerLabels(self, playerCount):
        self.labels = []
        labelGeometires = [QtCore.QRect(180, 90, 83, 22), QtCore.QRect(440, 90, 83, 22), QtCore.QRect(710, 90, 83, 22)]
        for i in range(playerCount):
            label = QtGui.QLabel(self.Frame)
            label.setGeometry(labelGeometires[i])
            self.labels.append(label)

    def createComboBoxes(self, playerCount):
        comboBoxGeometries = [QtCore.QRect(100, 130, 251, 41), QtCore.QRect(360, 130, 251, 41),
                              QtCore.QRect(620, 130, 251, 41)]
        self.comboBoxes = []
        for i in range(playerCount):
            comboBox = QtGui.QComboBox(self.Frame)
            comboBox.setGeometry(comboBoxGeometries[i])
            # QObject.connect(comboBox, SIGNAL('currentIndexChanged(QString)'), lambda obj={"func":"change_location", "args":comboBox}: self.onClicked(obj))
            self.comboBoxes.append(comboBox)

    def createCardDecks(self, playerCount):
        self.cardDecks = []

        playerCardGeometries = [
            {"box": QtCore.QRect(100, 180, 256, 111), "buttonLeft": QtCore.QRect(110, 300, 41, 32),
             "buttonRight": QtCore.QRect(310, 300, 41, 32), "addCard": QtCore.QRect(150, 300, 161, 41)},
            {"box": QtCore.QRect(360, 180, 256, 111), "buttonLeft": QtCore.QRect(370, 300, 41, 32),
             "buttonRight": QtCore.QRect(570, 300, 41, 32), "addCard": QtCore.QRect(410, 300, 161, 41)},
            {"box": QtCore.QRect(620, 180, 256, 111), "buttonLeft": QtCore.QRect(620, 300, 41, 32),
             "buttonRight": QtCore.QRect(840, 300, 41, 32), "addCard": QtCore.QRect(670, 300, 161, 41)}
        ]

        for i in range(playerCount):
            cardDeck = QtGui.QListWidget(self.Frame)
            cardDeck.setGeometry(playerCardGeometries[i]['box'])
            pushButtonLeft = QtGui.QPushButton(self.Frame)
            pushButtonLeft.setGeometry(playerCardGeometries[i]['buttonLeft'])
            pushButtonLeft.setText("-")
            QObject.connect(pushButtonLeft, SIGNAL("clicked()"), lambda obj={"func":"remove_selected_cards", "args":i}: self.onClicked(obj))

            pushButtonRight = QtGui.QPushButton(self.Frame)
            pushButtonRight.setGeometry(playerCardGeometries[i]['buttonRight'])
            pushButtonRight.setText('+')
            QObject.connect(pushButtonRight, SIGNAL("clicked()"), lambda obj={"func":"add_card", "args":i}: self.onClicked(obj))


            addCard = QtGui.QPlainTextEdit(self.Frame)
            addCard.setGeometry(playerCardGeometries[i]['addCard'])
            addCard.toPlainText()
            entry = {"cardDeck":cardDeck, "cardToAddText":addCard }

            self.cardDecks.append(entry)

    def onClicked(self, obj):
        func = getattr(self, obj['func'])
        func(obj['args'])

    def doRepaint(self,model):
        #TODO populate UI from model after every change
        self.cityList = []
        for city in model.getCityNames():
            self.cityList.append(city.upper())

        for i, player in enumerate(model.model['players']):

            self.comboBoxes[i].clear()
            self.comboBoxes[i].addItems(self.cityList)
            self.comboBoxes[i].setCurrentIndex(self.cityList.index(player['city'].upper()))

            self.cardDecks[i]['cardDeck'].clear()
            for card in player['cards']:
                self.cardDecks[i]['cardDeck'].addItem(card.upper())
                self.labels[i].setText(player['name'])

    def onASROut(self, text):
        self.plan_output.appendPlainText(text)

    def onPlanningDone(self, plan):
        self.plan_output.appendPlainText(plan)


    def get_assistance(self,args):
        query_type = args
        if self.textInput.toPlainText() is None:
            self.backend.get_assistance(query_type, self.onASROut, self.onPlanningDone)
        else:
            question_text = str(self.textInput.toPlainText())
            self.backend.get_assistance(query_type, None, self.onPlanningDone,question_text)


    def execute_plan(self,args):
        self.backend.executePlan()
        self.doRepaint(self.model)


    def update_locations(self,args):
        for i,comboBox in enumerate(self.comboBoxes):
            newcity = str(comboBox.currentText())
            self.model.setPlayerLocation(i, newcity)
        self.doRepaint(self.model)

    def change_location(self,comboBox):
        print comboBox.currentText()

    def remove_selected_cards(self, playerNo):
        selectedList = self.cardDecks[playerNo]['cardDeck'].selectedItems()
        for item in selectedList:
            print("Remove {} card from player {}".format(item.text(),playerNo))
            self.model.removeCardFromPlayer(playerNo, str(item.text()))
        self.doRepaint(self.model)


    def add_card(self, playerNo):
        newcard = self.cardDecks[playerNo]['cardToAddText'].toPlainText()
        self.cardDecks[playerNo]['cardToAddText'].clear()
        self.model.addCardToPlayer(playerNo,str(newcard))
        self.doRepaint(self.model)


    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.location_label.setText(_translate("Frame", "Location", None))
        self.cards_label.setText(_translate("Frame", "Cards", None))
        self.assistButton.setText(_translate("Frame", "Assist Me!", None))
        self.executeButton.setText(_translate("Frame", "Execute", None))
        self.updateButton.setText(_translate("Frame", "Update Locations", None))
        self.explainButton.setText(_translate("Frame", "Explain Plan", None))
        self.my_question_label.setText(_translate("Frame", "My Question :", None))





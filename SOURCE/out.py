# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'design.ui'
# #
# # Created: Sun Apr 15 22:45:58 2018
# #      by: PyQt4 UI code generator 4.10.4
# #
# # WARNING! All changes made in this file will be lost!
#
# from PyQt4 import QtCore, QtGui
# from PyQt4.QtCore import QObject, SIGNAL
# import Data
#
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#
#
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#
#
# class Ui_Frame(object):
#     def setupUi(self, Frame, model):
#         Frame.setObjectName(_fromUtf8("Frame"))
#         Frame.resize(1066, 837)
#         sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
#         Frame.setSizePolicy(sizePolicy)
#         Frame.setFrameShape(QtGui.QFrame.StyledPanel)
#         Frame.setFrameShadow(QtGui.QFrame.Raised)
#         self.location_label = QtGui.QLabel(Frame)
#         self.location_label.setGeometry(QtCore.QRect(10, 140, 83, 22))
#         self.location_label.setObjectName(_fromUtf8("location_label"))
#
#         self.cards_label = QtGui.QLabel(Frame)
#         self.cards_label.setGeometry(QtCore.QRect(20, 230, 83, 22))
#         self.cards_label.setObjectName(_fromUtf8("cards_label"))
#
#         self.graph_box = QtGui.QListWidget(Frame)
#         self.graph_box.setGeometry(QtCore.QRect(100, 360, 511, 401))
#         self.graph_box.setObjectName(_fromUtf8("graph_box"))
#
#         self.plan_output = QtGui.QListWidget(Frame)
#         self.plan_output.setGeometry(QtCore.QRect(620, 360, 251, 401))
#         self.plan_output.setObjectName(_fromUtf8("plan_output"))
#
#         self.pushButton = QtGui.QPushButton(Frame)
#         self.pushButton.setGeometry(QtCore.QRect(820, 770, 211, 51))
#         self.pushButton.setObjectName(_fromUtf8("pushButton"))
#
#         self.createPlayerLabels(3)
#         self.createComboBoxes(3, model['cities'])
#         self.createCardDecks(3)
#
#         self.retranslateUi(Frame)
#
#         self.cityList = []
#
#         QtCore.QMetaObject.connectSlotsByName(Frame)
#
#     def createPlayerLabels(self, playerCount):
#         self.labels = []
#         labelGeometires = [QtCore.QRect(180, 90, 83, 22), QtCore.QRect(440, 90, 83, 22), QtCore.QRect(710, 90, 83, 22)]
#         for i in range(playerCount):
#             label = QtGui.QLabel(Frame)
#             label.setGeometry(labelGeometires[i])
#             self.labels.append(label)
#
#     def createComboBoxes(self, playerCount, cities):
#         comboBoxGeometries = [QtCore.QRect(100, 130, 251, 41), QtCore.QRect(360, 130, 251, 41),
#                               QtCore.QRect(620, 130, 251, 41)]
#
#         city_list = []
#         for city in cities:
#             city_list.append(city['city_name'])
#         self.comboBoxes = []
#         for i in range(playerCount):
#             comboBox = QtGui.QComboBox(Frame)
#             comboBox.addItems(city_list)
#             comboBox.setGeometry(comboBoxGeometries[i])
#             self.comboBoxes.append(comboBox)
#
#     def createCardDecks(self, playerCount):
#         cardDecks = []
#
#         playerCardGeometries = [
#             {"box": QtCore.QRect(100, 180, 256, 111), "buttonLeft": QtCore.QRect(110, 300, 41, 32),
#              "buttonRight": QtCore.QRect(310, 300, 41, 32), "addCard": QtCore.QRect(150, 300, 161, 41)},
#             {"box": QtCore.QRect(360, 180, 256, 111), "buttonLeft": QtCore.QRect(370, 300, 41, 32),
#              "buttonRight": QtCore.QRect(570, 300, 41, 32), "addCard": QtCore.QRect(410, 300, 161, 41)},
#             {"box": QtCore.QRect(620, 180, 256, 111), "buttonLeft": QtCore.QRect(620, 300, 41, 32),
#              "buttonRight": QtCore.QRect(840, 300, 41, 32), "addCard": QtCore.QRect(670, 300, 161, 41)}
#         ]
#
#         for i in range(playerCount):
#             cardDeck = QtGui.QListWidget(Frame)
#             cardDeck.setGeometry(playerCardGeometries[i]['box'])
#             pushButtonLeft = QtGui.QPushButton(Frame)
#             pushButtonLeft.setGeometry(playerCardGeometries[i]['buttonLeft'])
#             pushButtonLeft.setText("-")
#             QObject.connect(pushButtonLeft, SIGNAL("clicked()"), lambda obj={"func":"remove_selected_cards", "args":str(i)}: self.onClicked(obj))
#
#             pushButtonRight = QtGui.QPushButton(Frame)
#             pushButtonRight.setGeometry(playerCardGeometries[i]['buttonRight'])
#             pushButtonRight.setText('+')
#             QObject.connect(pushButtonRight, SIGNAL("clicked()"), lambda obj={"func":"add_card", "args":str(i)}: self.onClicked(obj))
#
#
#             addCard = QtGui.QPlainTextEdit(Frame)
#             addCard.setGeometry(playerCardGeometries[i]['addCard'])
#
#             cardDecks.append(cardDeck)
#
#     def onClicked(self,obj):
#         self.cityList.pop()
#         func = getattr(self,obj['func'])
#         func(obj['args'])
#
#     def doRepaint(self,model):
#         #TODO populate UI from model after every change
#         self.cityList = []
#         for city in model['cities']:
#             self.cityList.append(city['city_name'])
#
#         for i, player in enumerate(model['players']):
#             self.comboBoxes[i].clear()
#             self.comboBoxes[i].addItems(self.cityList)
#             self.comboBoxes[i].setCurrentIndex(self.cityList.index(player['city']))
#
#
#
#     def remove_selected_cards(self, player):
#         print "Called"+ str(player)
#
#     def add_card(self, player):
#         print "Called add_card"+ str(player)
#
#     def retranslateUi(self, Frame):
#         Frame.setWindowTitle(_translate("Frame", "Frame", None))
#         self.location_label.setText(_translate("Frame", "Location", None))
#         self.cards_label.setText(_translate("Frame", "Cards", None))
#         self.pushButton.setText(_translate("Frame", "PushButton", None))
#
#
# if __name__ == "__main__":
#     import sys
#
#     players = [
#         {'name': "player1", "city": "London", "cards": ['Delhi', 'Mumbai']},
#         {'name': "player2", "city": "Delhi", "cards": ['London', 'Atlanta']},
#         {'name': "player3", "city": "Arizona", "cards": ['Egypt', 'Johannesburg']},
#     ]
#
#     cities = [
#         {"city_name": "London", "disease_count": 3, "research_station_count": 0},
#         {"city_name": "Delhi", "disease_count": 1, "research_station_count": 0},
#         {"city_name": "Arizona", "disease_count": 2, "research_station_count": 0}
#     ]
#
#     game_variables = {"research_station_count": 0, "total_disease_count": 3}
#
#     model = {'players': players, 'cities': cities, 'game_variables': game_variables}
#
#
#     app = QtGui.QApplication(sys.argv)
#     Frame = QtGui.QFrame()
#     ui = Ui_Frame()
#     ui.setupUi(Frame, model)
#     ui.doRepaint(model)
#
#     Frame.show()
#     sys.exit(app.exec_())
#

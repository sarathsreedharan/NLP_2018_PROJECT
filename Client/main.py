import Data
from PyQt4 import QtCore, QtGui
import GUI
import sys


def main():
    modelObj = Data.modelObj;
    players = [
        {'name': "player1", "city": "London", "cards": ['Delhi', 'Mumbai']},
        {'name': "player2", "city": "Delhi", "cards": ['London', 'Atlanta']},
        {'name': "player3", "city": "Arizona", "cards": ['Arizona', 'Johannesburg']},
    ]

    cities = [
        {"city_name": "Delhi", "disease_count": 3, "research_station_count": 0},
        {"city_name": "London", "disease_count": 1, "research_station_count": 0},
        {"city_name": "Arizona", "disease_count": 2, "research_station_count": 0}
    ]

    game_variables = {"research_station_count": 0, "total_disease_count": 3}

    newmodel = {'players': players, 'cities': cities, 'game_variables': game_variables}

    modelObj.initModel(newmodel)
    modelObj.show()

    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = GUI.Ui_Frame()
    ui.setupUi(Frame, modelObj.model)
    ui.doRepaint(modelObj.model)

    Frame.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()




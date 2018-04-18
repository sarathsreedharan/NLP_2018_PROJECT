import Data
from PyQt4 import QtCore, QtGui
import GUI
import sys
from Backend import Backend

def main():
    modelObj = Data.modelObj;
    players = [
        {'name': "player1", "city": "london", "cards": ['delhi', 'mumbai']},
        {'name': "player2", "city": "delhi", "cards": ['london', 'atlanta']},
        {'name': "player3", "city": "arizona", "cards": ['arizona', 'johannesburg']},
    ]

    cities = [
        {"city_name": "delhi", "disease_count": 3, "research_station_count": 0},
        {"city_name": "london", "disease_count": 1, "research_station_count": 0},
        {"city_name": "arizona", "disease_count": 2, "research_station_count": 0},
        {"city_name": "mumbai", "disease_count": 2, "research_station_count": 0},
        {"city_name": "johannesburg", "disease_count": 2, "research_station_count": 0}

    ]

    game_variables = {"research_station_count": 0, "total_disease_count": 3}

    newmodel = {'players': players, 'cities': cities, 'game_variables': game_variables}

    modelObj.initModel(newmodel)
    backend = Backend()


    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = GUI.Ui_Frame()
    ui.setupUi(Frame, modelObj, backend)
    ui.doRepaint(modelObj)



    Frame.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()




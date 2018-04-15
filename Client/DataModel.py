import Util as util

class Model(object):
    def __init__(self):
        self.model = {'players': [], 'cities': [], 'config': {}}
        self.playerNameNumberMap = {}

    def __setPlayerName(self, playerNo, name):
        self.model['players'][playerNo]['name'] = name

    def __setPlayerLocation(self, playerNo, newcity):
        self.model['players'][playerNo]['city'] = newcity

    def __setPlayerCards(self,playerNo,card_list):
        self.model['players'][playerNo]['cards'] = card_list

    def __removeCardFromPlayer(self,playerNo,card):
        card_list = self.model['players'][playerNo]['cards']
        card_list.remove(card)





    def setPlayerLocation(self, playerName, newcity):
        playerNo = self.playerNameNumberMap[playerName]
        self.__setPlayerLocation(playerNo, newcity)

    def setPlayerCards(self, playerName, card_list):
        playerNo = self.playerNameNumberMap[playerName]
        self.__setPlayerCards(playerNo, card_list)

    def removeCardFromPlayer(self, playerName,card):
        playerNo = self.playerNameNumberMap[playerName]
        self.__removeCardFromPlayer(playerNo, card)

    def addResearchStation(self, city_name):
        for city in self.model['cities']:
            if util.isEqualStr(city['city_name'], city_name):
                city['research_station_count'] = city['research_station_count'] + 1

    def setCityDiseaseCount(self, city_name, newcount):
        for city in self.model['cities']:
            if util.isEqualStr(city['city_name'], city_name):
                city['disease_count'] = newcount



def main():
    players = [
        {'name': "player1", "city": "London", "cards": ['Delhi', 'Mumbai']},
        {'name': "player2", "city": "Delhi", "cards": ['London', 'Atlanta']},
        {'name': "player3", "city": "Arizona", "cards": ['Egypt', 'Johannesburg']},
    ]

    cities = [
        {"city_name": "Delhi", "disease_count": 3, "research_station_count": 0},
        {"city_name": "Mumbai", "disease_count": 1, "research_station_count": 0},
        {"city_name": "Arizona", "disease_count": 2, "research_station_count": 0}
    ]

    game_variables = {"research_station_count": 0, "total_disease_count": 3}

    model = {'players': players, 'cities': cities, 'game_variables': game_variables}


if __name__ == "__main__":
    main()
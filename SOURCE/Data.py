import Util as util
import pprint
import PredicateUtils

class Model(object):
    def __init__(self):
        self.model = {'players': [], 'cities': [], 'config': {}}
        self.playerNameNumberMap = {}

    def initModel(self, model):
        self.model = model
        for index,player in enumerate(self.model['players']):
            self.playerNameNumberMap[player['name']] = index

    def show(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint (self.model)

    def getPredicates(self):
        return PredicateUtils.getBoardModelPredicates(self.model)

    def setPlayerName(self, playerNo, name):
        self.model['players'][playerNo]['name'] = name

    def setPlayerLocation(self, playerNo, newcity):
        self.model['players'][playerNo]['city'] = newcity

    def setPlayerCards(self,playerNo,card_list):
        self.model['players'][playerNo]['cards'] = card_list

    def removeCardFromPlayer(self,playerNo,card):
        card = card.lower()
        card_list = self.model['players'][playerNo]['cards']
        card_list.remove(card)

    def addCardToPlayer(self,playerNo,card):
        card = card.lower()
        if(card != ''):
            card_list = self.model['players'][playerNo]['cards']
            card_list.append(card)






    def setPlayerLocationByName(self, playerName, newcity):
        playerNo = self.playerNameNumberMap[playerName]
        self.__setPlayerLocation(playerNo, newcity)

    def setPlayerCardsByName(self, playerName, card_list):
        playerNo = self.playerNameNumberMap[playerName]
        self.__setPlayerCards(playerNo, card_list)

    def removeCardFromPlayerByName(self, playerName,card):
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

    def getCityNames(self):
        cities = []
        for city in self.model['cities']:
            cities.append(city['city_name'])
        return  cities

modelObj = Model()




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
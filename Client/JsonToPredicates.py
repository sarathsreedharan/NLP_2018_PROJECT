def getPlayerLocationPredicate(player):
    #(in_city p1 london)

    template = '(in_city %(player)s %(city)s)'
    return template % dict(player=player['name'], city=player['location'])

def getPlayerHasCardPredicates(player):
    #(has_city_card p1 delhi)
    template = '(has_city_card %(player)s %(card)s)'

    predicates = []
    for card in player['cards']:
        predicates.append(template % dict(player=player['name'], card=card))

    return  predicates

def getGameVariablePredicate(game_vars):

    template = '(= (research_station_count) %(research_station_count)s)\n' \
               '(= (total_disease_count) %(total_disease_count)s)'

    return template % dict(research_station_count=game_vars['research_station_count'], total_disease_count=game_vars['total_disease_count'])


def getCityDiseaseCountPredicates(city_disease_count):
    template = '(= (total_per_city_count %(city_name)s) %(disease_count)s)'

    predicates = []
    for city in city_disease_count:
        predicates.append(template % dict(city_name=city['city_name'], disease_count=city['disease_count']))

    return predicates


def getBoardModelPredicates(model):
    strs = []

    strs.append(getGameVariablePredicate(model['game_variables']))
    strs.extend(getCityDiseaseCountPredicates(model['city_disease_count']))

    for player in model['players']:
        strs.append(getPlayerLocationPredicate(player))
        strs.extend(getPlayerHasCardPredicates(player))

    for s in strs:
        print s


if __name__ == "__main__":
    players=[
                {'name':"player1", "location":"London", "cards":['Delhi', 'Mumbai']},
                {'name': "player2", "location": "Delhi", "cards": ['London', 'Atlanta']},
                {'name': "player3", "location": "Arizona", "cards": ['Egypt', 'Johannesburg']},
            ]

    city_disease_count = [
                            {"city_name":"Delhi", "disease_count":3},
                            {"city_name": "Mumbai", "disease_count": 1},
                            {"city_name": "Arizona", "disease_count": 2}
                          ]

    game_variables = { "research_station_count":0, "total_disease_count":3}

    model = {'players':players,'city_disease_count':city_disease_count,'game_variables':game_variables}

    getBoardModelPredicates(model)


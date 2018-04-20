def extractNameAndParametersFromAction(action):
    actionList = action.replace('(', '') \
        .replace(')', '') \
        .split(' ')
    return actionList[0], actionList[1:]

def getPlayerLocationPredicate(player):
    #(in_city p1 london)

    template = '(in_city %(name)s %(city)s)'
    return template % player

def getPlayerHasCardPredicates(player):
    #(has_city_card p1 delhi)
    template = '(has_city_card %(player)s %(card)s)'

    predicates = []
    for card in player['cards']:
        predicates.append(template % dict(player=player['name'], card=card))

    return predicates

def getGameVariablePredicate(game_vars):

    template = '(= (research_station_count) %(research_station_count)s)' \
               '(= (total_disease_count) %(total_disease_count)s)'

    return template % game_vars


def getCityDiseaseCountPredicates(cities):

    template = '(= (total_per_city_count %(city_name)s) %(disease_count)s)'

    predicates = []
    for city in cities:
        predicates.append(template % city)

    return predicates


def getBoardModelPredicates(model):
    strs = []

    strs.append(getGameVariablePredicate(model['game_variables']))
    strs.extend(getCityDiseaseCountPredicates(model['cities']))

    for player in model['players']:
        strs.append(getPlayerLocationPredicate(player))
        strs.extend(getPlayerHasCardPredicates(player))


    return set(strs)


if __name__ == "__main__":

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

    print getBoardModelPredicates(model)


import DataModel
import Executor


def main():
    players = [
        {'name': "player1", "city": "London", "cards": ['delhi', 'mumbai']},
        {'name': "player2", "city": "Delhi", "cards": ['london', 'atlanta']},
        {'name': "player3", "city": "Arizona", "cards": ['egypt', 'johannesburg']},
    ]

    cities = [
        {"city_name": "delhi", "disease_count": 3, "research_station_count": 0},
        {"city_name": "mumbai", "disease_count": 1, "research_station_count": 0},
        {"city_name": "arizona", "disease_count": 2, "research_station_count": 0}
    ]

    game_variables = {"research_station_count": 0, "total_disease_count": 3}

    model = {'players': players, 'cities': cities, 'game_variables': game_variables}


    data_model = DataModel.Model()
    data_model.initModel(model)
    #data_model.setPlayerLocation('player1','Bangalore')


    plan = ['(fly_directly player1 london delhi)','(build_research_station_new player1 delhi)']

    planExecutor = Executor.PlanExecutor(data_model)
    planExecutor.execute(plan)

    data_model.show()
    pass


if __name__ == "__main__":
    main()

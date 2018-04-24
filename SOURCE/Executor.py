import PredicateUtils

class PlanExecutor(object):
    def __init__(self, data_model):
        self.data_model = data_model



    def undefinedActionMethod(self):
        print ("Cannot Execute: Action is undefined")

    def execute(self, plan):
        for action in plan:
            action_name, action_params = PredicateUtils.extractNameAndParametersFromAction(action)
            func = getattr(self, action_name, self.undefinedActionMethod)
            func(action_params)


    def build_research_station_new(self, params):
        player = params[0]
        city = params[1]
        self.data_model.addResearchStation(city)

    def fly_directly(self, params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        self.data_model.removeCardFromPlayerByName(player, toCity)
        self.data_model.setPlayerLocationByName(player, toCity)

    def fly_by_charter(self,params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        self.data_model.removeCardFromPlayerByName(player, fromCity)
        self.data_model.setPlayerLocationByName(player, toCity)
        pass

    def fly_by_shuttle(self,params):
        player = params[0]
        fromCity = params[1]
        toCity = params[2]
        self.data_model.setPlayerLocationByName(player, toCity)
        pass

    def treat_disease(self,params):
        pass

    def treat_cured_disease_begin(self,params):
        pass

    def treat_cured_disease_end(self,params):
        pass

    def share_knowledge(self,params):
        player1 = params[0]
        player2 = params[1]
        city = params[2]
        self.data_model.removeCardFromPlayerByName(player1, city)
        self.data_model.addCardToPlayerByName(player2, city)
        pass

    def cure_disease(self,params):
        pass

class PlanExecutor(object):
    def __init__(self, data_model):
        self.data_model = data_model

    def __extractNameAndParameters(self, action):
        actionList= action.replace('(', '')\
            .replace(')', '')\
            .split(' ')
        return actionList[0], actionList[1:]

    def undefinedActionMethod(self):
        print ("Cannot Execute: Action is undefined")

    def execute(self,plan):
        for action in plan:
            action_name, action_params = self.__extractNameAndParameters(action)
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
        self.data_model.removeCardFromPlayer(player, toCity)
        self.data_model.setPlayerLocation(player, toCity)

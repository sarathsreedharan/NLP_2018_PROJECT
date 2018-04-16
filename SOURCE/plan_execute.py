
PREC_TYPES = ['exist','equal','greater', 'less']
ADD_TYPES = ['proposition']

DOMAIN_MAP = {
        "validate_pieces":{'parameters':[], 'precondition':{'exist':['(has_board)']}, 'adds':{'proposition':['(integrity_check)']}, 'deletes':{'proposition':[]}},
        "game_over_check":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "drive":{'parameters':['?p','?c1','?c2'], 'precondition':{'exist':['(in_city ?p ?c1)','(connected ?c1 ?c2)']}, 'adds':{'proposition':['(in_city ?p ?c2)']}, 'deletes':{'proposition':['(in_city ?p ?c1)']}},
        "fly_directly":{'parameters':['?p','?c1','?c2'], 'precondition':{'exist':['(in_city ?p ?c1)','(has_city_card ?p ?c2)']}, 'adds':{'proposition':['(in_city ?p ?c2)']}, 'deletes':{'proposition':['(in_city ?p ?c1)','(has_city_card ?p ?c2)']}},
        "fly_by_charter":{'parameters':['?p','?c1','?c2'], 'precondition':{'exist':['(in_city ?p ?c1)','(has_city_card ?p ?c2)']}, 'adds':{'proposition':['(in_city ?p ?c2)']}, 'deletes':{'proposition':['(in_city ?p ?c1)','(has_city_card ?p ?c2)']}},
        "fly_by_shuttle":{'parameters':['?p','?c1','?c2'], 'precondition':{'exist':['(in_city ?p ?c1)','(has_research_station ?c1)','(has_research_station ?c2)']}, 'adds':{'proposition':['(in_city ?p ?c2)']}, 'deletes':{'proposition':['(in_city ?p ?c1)']}},
        "build_research_station_new":{'parameters':['?p','?c1'], 'precondition':{'exist':['(in_city ?p ?c1)']}, 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "treat_disease":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "treat_cured_disease_begin":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "treat_cured_disease_end":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "share_knowledge":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}},
        "cure_disease":{'parameters':[], 'precondition':[], 'adds':{'proposition':[]}, 'deletes':{'proposition':[]}}
        }




def execute_plan(curr_state, plan):
    new_state = curr_state
    for act_raw in plan:
        act = act_raw.replace('(','').replace(')','')
        act_parts = act.split(' ')
        act_name = act_parts[0].lower()
        act_args =  act_parts[1:]
        par_map = {}
        for ind in range(len(DOMAIN_MAP[act_name]['parameters'])):
            par_map[DOMAIN_MAP[act_name]['parameters'][ind]] = act_args[ind]

        add_effects_props = set()

        for prop in DOMAIN_MAP[act_name]['adds']['proposition']:
            new_prop = prop
            for k in par_map.keys():
               new_prop = new_prop.replace(k, par_map[k])
            add_effects_props.add(new_prop)

    
        del_effects_props = set()

        for prop in DOMAIN_MAP[act_name]['deletes']['proposition']:
            new_prop = prop
            for k in par_map.keys():
               new_prop = new_prop.replace(k, par_map[k])
            del_effects_props.add(new_prop)

        new_state = new_state|add_effects_props
        new_state = new_state - del_effects_props
    return new_state
         

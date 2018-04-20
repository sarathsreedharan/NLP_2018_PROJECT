#!/usr/bin/env python

'''
Topic   :: Help with PDDL stuff
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

import re, os


'''
Global :: global variables
'''

__DOMAIN_SOURCE__ = '../../domain/domain_template.pddl'

__GROUND_CMD__    = "./ground.sh {} {} > stdout.txt"
__FD_PLAN_CMD__   = "./fdplan.sh {} {}"
__VAL_PLAN_CMD__  = "./valplan.sh {} {} {}"



def get_problem_state_preds(problem_lines, section_prefix):
    start_line = False
    init_state = []
    for line in problem_lines:
        if section_prefix in line:
            start_line = True
        elif start_line:
            if line.strip() == ')':
                start_line = False
            elif "(and" not in line:
                init_state.append('@'.join(line.split(' ')))
    return init_state


'''
Method :: write domain file from given state
'''

def write_domain_file_from_state(state, domain_source):

    predicateList = set()
    actionList    = {}
    init_state_list = []
    goal_state_list =[]

    for item in state:
        if "state" not in item:
            regex_probe   = re.compile("(.*)-has-(parameters|precondition|add-effect|delete-effect)-(.*)$").search(item)
            actionName    = regex_probe.group(1)
            _condition    = regex_probe.group(2)
            predicateName = regex_probe.group(3)

            predicateList.add(predicateName)

            if actionName not in actionList: actionList[actionName] = {'parameters':"", 'precondition' : [], 'add-effect' : [], 'delete-effect' : []}
            if _condition == 'parameters':
                actionList[actionName][_condition] = predicateName
            else:
                actionList[actionName][_condition].append(predicateName) 
        else:
            regex_probe   = re.compile("has-(initial|goal)-state-(.*)$").search(item)
            state_type = regex_probe.group(1)
            pred = regex_probe.group(2)
            if state_type == 'initial':
                init_state_list.append(' '.join(pred.split('@')))
            else:
                goal_state_list.append(' '.join(pred.split('@')))

    temp_domainFileName = 'temp.pddl'
    temp_problemFileName = 'temp_prob.pddl'

    with open(domain_source, 'r') as template_domain_file:
        template_domain = template_domain_file.read()



    with open(temp_domainFileName, 'w') as temp_domain_file:

        predicateString = '\n'.join(['( {} )'.format(item) for item in predicateList])
        actionString    = '\n'.join(['(:action {}\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n{}\n)\n)\n;new_act'\
                                     .format(key, actionList[key]['parameters'],'\n'.join(['{}'.format(p) for p in actionList[key]['precondition']]), \
                                             '{}\n{}'.format('\n'.join([' {} '.format(p) for p in actionList[key]['add-effect']]), \
                                                             '\n'.join(['(not {} )'.format(p) for p in actionList[key]['delete-effect']]))) for key in actionList.keys()])
        
        temp_domain_file.write(template_domain.format(actionString))

    return temp_domainFileName
        

'''
Method :: read state from given domain file
'''

def read_state_from_domain_file(domainFileName):

    def PDDLaction(description):
        action_name            = re.search('\(:action(.*?)[\s+]*:', description).group(1).strip()
        try:
            parameters     = re.search(':parameters[\s+]*\((.*?)\)[\s+]*:', description).group(1)
        except:
            parameters     = ""
        try:
#            preconditions  = {re.search('\(((?!not).*?)\)', item).group(1).strip() : not 'not ' in item \
#                                 for item in re.findall('(\(not[\s+]*\(.*?\)[\s+]*\)|\(.*?\))', re.search(':precondition[\s+]*\(and(.*?)\)[\s+]*:', description).group(1))}
            prec_scr = re.search(':precondition[\s+]*\(and[\s+]*(.*?)\)[\s+]*:effect', description).group(1).strip()[1:-1]
            preconditions  = ["("+i+")" for i in prec_scr.split(') (')]
        except:
            preconditions  = []
        try:
            #all_effects = [item for item in re.findall('(\(not[\s+]*\(.*?\)[\s+]*\)|\(increase[\s+]*\(.*?\)[\s+]*\(.*?\)[\s+]*\)|\(.*?\))', re.search(':effect[\s+]*\(and(.*?)\)[\s+]*(\(:action|\)[\s+]*$)', description).group(1))]
#            all_effects = [item for item in re.findall('(\(not[\s+]*\(.*?\)[\s+]*\)|\(increase[\s+]*\(.*?\)[\s+]*\(.*?\)[\s+]*\)|\(.*?\))', re.search(':effect[\s+]*\(and(.*?)\)[\s+]*;;new_act', description).group(1))]
            all_effects = re.search(':effect[\s+]*\(and[\s+]*(.*?)\)[\s+]*\)[\s+]*;new_act$', description).group(1)[1:-1]
            add_effects = []
            del_effects = []
            for i in all_effects.split(') ('):
                if "not" in i:
                    del_effects.append(i.replace("not ",""))#re.search('not[\s+]*(.*)',i).group(1)[0])
                else:
                    add_effects.append('('+i+')')
        except Exception as exc:
            print ("Error, Exc", exc)
        #print "action_dict",[action_name, parameters, preconditions, add_effects, del_effects]
        return [action_name, parameters, preconditions, add_effects, del_effects]
    
    ''''''

    with open(domainFileName, 'r') as domain_file:
        action_dict = {item.split(' ')[1] : PDDLaction(item) for item in re.findall('\(:action.*?\)[\s+]*\)[\s+]*;new_act', re.sub('[\s+]', ' ', domain_file.read()))}
    ''''''
    #print "action_dict",action_dict
    state = []
    for key in action_dict.keys():
        actionName        = action_dict[key][0]
        state.append('{}-has-parameters-{}'.format(actionName, action_dict[key][1]))
        for precondition in action_dict[key][2]:
            state.append('{}-has-precondition-{}'.format(actionName, precondition))
           
        for effect in action_dict[key][3]:
            state.append('{}-has-add-effect-{}'.format(actionName, effect))
        for effect in action_dict[key][4]:
            state.append('{}-has-delete-effect-{}'.format(actionName, effect))
    return state




'''
Method :: compute plan from domain and problem files
'''

def get_plan(domainFileName, problemFileName):
    output = os.popen(__FD_PLAN_CMD__.format(domainFileName, problemFileName)).read().strip()
        
    #plan   = [item.strip().replace('_', ' ') for item in output.split('\n')] if output != '' else []
    plan   = [item.strip() for item in output.split('\n')] if output != '' else []
    cost   = len(plan)

    return [plan, cost]


''' 
Method :: ground PDDL domain and problem files
'''

def ground(domainFileName, problemFileName):

    output = os.system('./clean.sh')
    print "ab",__GROUND_CMD__.format(domainFileName, problemFileName)
    output = os.system(__GROUND_CMD__.format(domainFileName, problemFileName))


''' 
Method :: validate plan given PDDL domain and problem files
'''

#def validate_plan(domainFileName, problemFileName, planFileName):

#    output = os.system(__VAL_PLAN_CMD__.format(domainFileName, problemFileName, planFileName))
#    return eval(output)

def validate_plan(domainFileName, problemFileName, planFileName):
    output = os.popen(__VAL_PLAN_CMD__.format(domainFileName, problemFileName, planFileName)).read().strip()
    return eval(output)



if __name__ == '__main__':
    pass

    ''' debug list '''
    #print validate_plan('../domain/fetchworld-base-m.pddl', '../domain/problem1.pddl', 'sas_plan')
    #state = read_state_from_domain_file('../domain/fetchworld-base-m.pddl')
    #write_domain_file_from_state(state)

#!/usr/bin/env python

from PDDLhelp import *
from Search   import astarSearch
import copy, argparse, os, sys

'''
Class :: Environment Definition
'''

class Problem:

    def __init__(self, robotModelFile, humanModelFile, problemFile, humanProblemFile, domainTemplate, problemTemplate, robotPlanFile, foil_file):

        print "Setting up MMP..."

        self.domainTemplate = domainTemplate
        self.problemTemplate = problemTemplate

        with open(foil_file) as f_fd:
            self.foil = f_fd.read().strip().split('\n')

        self.robotPlanFile   = robotPlanFile
        with open(robotPlanFile, 'r') as plan_file:
            temp      = [x for x in plan_file.read().strip().split('\n') if x[0] != '!']
            self.plan = temp #[:-1]
            self.cost = len(self.plan)#int(temp[-1].split(' ')[3].strip())
        ground(robotModelFile, problemFile)
        self.groundedRobotPlanFile   = '../domains/cache_grounded_plan.dat'


        with open(self.groundedRobotPlanFile, 'w') as plan_file:
            plan_file.write('\n'.join(['{}'.format(item) for item in self.plan]) + '\n; cost = {} (unit cost)'.format(self.cost))

        self.foil_file = '../domains/foil_plan.dat'

        with open(self.foil_file, 'w') as plan_file:
            plan_file.write('\n'.join(['{}'.format(item) for item in self.foil]) + '\n')

        self.ground_state = read_state_from_domain_file('tr-domain.pddl')
        
        ground(humanModelFile, humanProblemFile)

        try:    self.initialState = read_state_from_domain_file('tr-domain.pddl')
        except: self.initialState = []

        
    def getStartState(self):
        return self.initialState

    def isGoal(self, state):
        temp_problem = 'tr-problem.pddl'
        temp_domain = write_domain_file_from_state(state, self.domainTemplate)
        print ("Here????")
        feasibility_flag = validate_plan(temp_domain, temp_problem, self.groundedRobotPlanFile)
        if not feasibility_flag:
            return False
        foil_flag = validate_plan(temp_domain, temp_problem, self.foil_file)
        print ("Here foil fla",foil_flag)
        return (not foil_flag) and feasibility_flag

    
    def heuristic(self, state):
        return 0.0

    
    def getSuccessors(self, node):

        listOfSuccessors = []

        state            = set(node[0])
        ground_state     = set(self.ground_state)

        add_set          = ground_state.difference(state)
        del_set          = state.difference(ground_state)

        for item in add_set:
            new_state    = copy.deepcopy(state)
            new_state.add(item)
            listOfSuccessors.append([list(new_state), item])

        for item in del_set:
            new_state    = copy.deepcopy(state)
            new_state.remove(item)
            listOfSuccessors.append([list(new_state), item])
            
        return listOfSuccessors
        

'''
main method
'''

def main():
    
    parser = argparse.ArgumentParser(description = '''This is the Problem class. Explanations for Multi-Model Planning.''',
                                     epilog      = '''Usage >> ./Problem.py -m ../domain/fetchworld-tuck-m.pddl -n ../domain/fetchworld-base-m.pddl -f ../domain/problem1.pddl ''')
     
    parser.add_argument('-m', '--model',   type=str, help="Domain file with real PDDL model of robot.")
    parser.add_argument('-n', '--nmodel',  type=str, help="Domain file with human model of the robot.")
    parser.add_argument('-d', '--domain_template',   type=str, help="Domain template for the current MMP.")
    parser.add_argument('-q', '--problem_template',   type=str, help="Problem template for the current MMP.")
    parser.add_argument('-p', '--problem', type=str, help="Problem file.")
    parser.add_argument('-t', '--humanProblem', type=str, help="human Problem file.")
    parser.add_argument('-f', '--foil',    type=str, help="Plan file.")
    parser.add_argument('-r', '--plan',    type=str, help="Plan file.")
 
    args   = parser.parse_args()

    if not sys.argv[1:]:
        print parser.print_help()

    else:
        
        problem_instance = Problem(args.model, args.nmodel, args.problem, args.humanProblem, args.domain_template, args.problem_template, args.plan, args.foil)
        plan             = astarSearch(problem_instance)
        
        explanation      = ''
        for item in plan:
            explanation += "Explanation >> {}\n".format(item)

        print explanation.strip()
        with open('exp.dat', 'w') as explanation_file:
            explanation_file.write(explanation.strip())
        

if __name__ == '__main__':
    main()

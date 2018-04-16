from plan_execute import *
import os
import tempfile

__PLAN_CMD__ = "./run_lprgp.sh {} {} {}"
__READ_BEST_PLAN__ = "./find_and_read_best_plan.sh {}"

class PLAN_QUERY:
    def __init__(self, domain_file, prob_templ):
        self.domain_file = domain_file
        with open(prob_templ) as p_fd:
            self.prob_templ_str = p_fd.read()
        self.workspace = tempfile.mkdtemp()
#        print ("workspace", self.workspace)

    def update_curr_state(self, output_plan):
        #TODO
        self.curr_state =  execute_plan(self.curr_state, output_plan)

    def run_planner(self, prob_file, plan_dest):
#        print ("CMD:", __PLAN_CMD__.format(self.domain_file, prob_file, plan_dest))
        output = os.popen(__PLAN_CMD__.format(self.domain_file, prob_file, plan_dest)).read().strip()

        if not eval(output):
            return []

        output_plan =  os.popen(__READ_BEST_PLAN__.format(plan_dest)).read().strip().split('\n')
        self.update_curr_state(output_plan)
        return output_plan

    def translate2PDDL(self, curr_str):
        #query_str = ""
        #curr_part = ""
        #for i in range(len(curr_str)):
        #    if curr_str[i] == '(':
        #        query_str += " " + curr_part
        #    elif:
        #        query_str += curr_str[i]
        new_str = curr_str.replace("atend(", "(at end ")
        new_str = new_str.replace("incity(", "(in_city ")
        new_str = new_str.replace(",", "")
        return new_str

    def make_problem_file(self, init_state, goal_constr):
        prob_str = self.prob_templ_str.format("\n".join(init_state), goal_constr)
        with open(self.workspace+"/prob.pddl", "w") as p_fd:
            p_fd.write(prob_str)


    def query_goal(self, curr_state, goal_str):
        self.curr_state = curr_state
        clean_str = self.translate2PDDL(goal_str)
        self.make_problem_file(self.curr_state, clean_str)

        best_plan =  self.run_planner(self.workspace+"/prob.pddl", self.workspace+"/plans")

        return (pq.curr_state, best_plan)


if __name__ == '__main__':
    with open('/media/data_mount/mycode/NLP_PROJ_FILES/PLAN_QUERY_INTERFACE/domains/test_init_state') as init_fd:
        init = set([i.strip() for i in init_fd.readlines()])
    domain_file = "/media/data_mount/mycode/NLP_PROJ_FILES/PLAN_QUERY_INTERFACE/domains/domain.pddl"
    prob_templ = "/media/data_mount/mycode/NLP_PROJ_FILES/PLAN_QUERY_INTERFACE/domains/prob_templ.pddl"
    pq = PLAN_QUERY(domain_file, prob_templ)#, init)
    print (pq.query_goal(init, "atend(incity(p1, delhi))"))
#    print (pq.curr_state)




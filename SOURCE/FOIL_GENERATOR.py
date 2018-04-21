import os
import tempfile

__PLAN_CMD__ = "./run_lprgp.sh {} {} {}"
__READ_BEST_PLAN__ = "./find_and_read_best_plan.sh {}"
__DOMAIN_FILE_LOC__ = "../src/PLAN_QUERY_INTERFACE/domains/domain.pddl"
__DOMAIN_FILE_LOC__ = "../src/PLAN_QUERY_INTERFACE/domains/human_domain.pddl"
__PROB_TEMPL_LOC__ = "../src/PLAN_QUERY_INTERFACE/domains/prob_templ.pddl"

class FOIL_GENERATOR:
    def __init__(self, domain_file = __DOMAIN_FILE_LOC__, prob_templ = __PROB_TEMPL_LOC__):
        with open(domain_file) as d_fd:
             dom_str = d_fd.read()
        #self.domain_file = domain_file
        with open(prob_templ) as p_fd:
            self.prob_templ_str = p_fd.read()
        self.workspace = tempfile.mkdtemp()
        self.domain_file = self.workspace + "/domain.pddl"
        with open(self.domain_file, 'w') as d_fd:
                d_fd.write(dom_str)


    def update_curr_state(self, output_plan):
        #TODO
        self.curr_state =  execute_plan(self.curr_state, output_plan)

    def run_planner(self, prob_file, plan_dest):
        print ("CMD:", __PLAN_CMD__.format(self.domain_file, prob_file, plan_dest))
        output = os.popen(__PLAN_CMD__.format(self.domain_file, prob_file, plan_dest)).read().strip()

        if not eval(output):
            return []

        output_plan =  os.popen(__READ_BEST_PLAN__.format(plan_dest)).read().strip().split('\n')
        return output_plan

    def translate2PDDL(self, curr_str):
        new_str = curr_str.replace("atend(", "(at end ")
        new_str = new_str.replace("always(", "(always ")
        new_str = new_str.replace("not(", "(not ")
        new_str = new_str.replace("incity(", "(in_city ")
        new_str = new_str.replace(",", " ")
        return new_str

    def make_problem_file(self, init_state, goal_constr):
        prob_str = self.prob_templ_str.format("\n".join(init_state), goal_constr)
        with open(self.workspace+"/prob.pddl", "w") as p_fd:
            p_fd.write(prob_str)


    def query_goal(self, init_state, goal_str):
        clean_str = self.translate2PDDL(goal_str)
        self.make_problem_file(init_state, clean_str)

        best_plan =  self.run_planner(self.workspace+"/prob.pddl", self.workspace+"/plans")

        return best_plan


if __name__ == '__main__':
    with open('/tmp/init_state') as init_fd:
        init = set([i.strip() for i in init_fd.readlines()])
    domain_file = "/media/data_mount/mycode/NLP_PROJ_FILES/FOIL_GENERATOR_INTERFACE/domains/domain.pddl"
    prob_templ = "/media/data_mount/mycode/NLP_PROJ_FILES/FOIL_GENERATOR_INTERFACE/domains/prob_templ.pddl"
    pq = FOIL_GENERATOR()
    print (pq.query_goal(init, "atend(incity(player1,Delhi))"))#"always(not(incity(player1,Delhi)))"))


#!/bin/bash
../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/src/Problem.py  -m ../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/domain.pddl -n ../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/human_domain.pddl -d ../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/domain_templ.pddl -q ../src/EXPLANATION_QUERY_INTERFACE/mmp_foil/domains/prob_templ.pddl -p /tmp/curr_problem.pddl -f /tmp/curr_foil.sol -r /tmp/curr_plan.sol

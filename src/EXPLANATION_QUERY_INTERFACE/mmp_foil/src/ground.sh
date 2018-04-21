#/usr/bin/env bash

# path to pr2plan #
#PR2PLAN_PATH=$(locate pr2plan | head -n 1)

# ground domain and problem input using pr2plan #
echo "a $1"
echo "b $2"
rm -f /tmp/*-domain.pddl /tmp/*-problem.pddl 
cp $1 /tmp/tr-domain.pddl
cp $2 /tmp/tr-problem.pddl

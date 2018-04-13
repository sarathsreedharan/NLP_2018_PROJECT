PLAN=$1

best_plan_file=`ls ${PLAN}.*|sort|tail -n 1`

cat ${best_plan_file}|grep -v ";"|awk -F: '{print $2}'|sed 's/ \[.*//'|sed 's/^ //'

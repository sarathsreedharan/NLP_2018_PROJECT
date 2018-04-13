#!/bin/bash
domain=$1
problem=$2
plan=$3

if [ -z "${plan}" ]
then
    echo "False"
    return 1
else
    rm -rf ${plan}*
fi


pushd /media/data_mount/mycode/NLP_PROJ_FILES/LPRPGP/pref-sat-lprpgp/ > /dev/null
./plan $domain $problem $plan #> /dev/null
popd > /dev/null

if [ -f ${plan}.1 ]
then
    echo "True"
else
    echo "False"
fi


CONFIG=$1
shift
java -Djava.util.logging.config.file=logging.properties -Dgui=false -Xmx1000m $@ -cp /home/midhun/Documents/NLP/NLP_2018_PROJECT/NL2KR/NL2KR.jar:lib/* nl2kr.scripts.NL2KR_TTest $CONFIG

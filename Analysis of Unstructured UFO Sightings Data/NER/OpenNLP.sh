#Create a directory for keeping all the models.
#Choose any convenient path but make sure to use absolute path
export NER_RES=./bin

PATH_PREFIX="$NER_RES/org/apache/tika/parser/ner/opennlp"
URL_PREFIX="http://opennlp.sourceforge.net/models-1.5"

mkdir -p $PATH_PREFIX

# using three entity types from the above table for demonstration
#wget "$URL_PREFIX/en-ner-person.bin" -O $PATH_PREFIX/ner-person.bin
#wget "$URL_PREFIX/en-ner-location.bin" -O $PATH_PREFIX/ner-location.bin
#wget "$URL_PREFIX/en-ner-organization.bin" -O $PATH_PREFIX/ner-organization.bin

export TIKA_APP="C:/Users/trpcw/.m2/repository/org/apache/tika/tika-app/1.17/tika-app-1.17.jar"
echo $1
java -cp "$NER_RES;$TIKA_APP;" org.apache.tika.cli.TikaCLI --config=tika-config.xml -m
#http://people.apache.org/committer-index.html

# Are there any metadata keys starting with "NER_" ?
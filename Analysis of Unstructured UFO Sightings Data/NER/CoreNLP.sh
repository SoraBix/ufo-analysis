CORE_NLP_JAR="C:/workspace/csci599/hw2/extra/lib/tika-ner-corenlp-addon-1.0-SNAPSHOT-jar-with-dependencies.jar"

TIKA_APP="C:/Users/trpcw/.m2/repository/org/apache/tika/tika-app/1.17/tika-app-1.17.jar"
#"$PWD/lib/tika-app-1.17.jar"
# To use 3class NER model  (Default is 7 class model)

 java  -Dner.corenlp.model=edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz \
       -Dner.impl.class=org.apache.tika.parser.ner.corenlp.CoreNLPNERecogniser \
       -classpath "$TIKA_APP;$CORE_NLP_JAR;" org.apache.tika.cli.TikaCLI \
       --config=tika-config.xml -m 

# Observe metadata keys starting with NER_ 
NLTK_RES="C:/workspace/csci599/hw2/extra"
TIKA_APP="C:/Users/trpcw/.m2/repository/org/apache/tika/tika-app/1.17/tika-app-1.17.jar"
#"$PWD/lib/tika-app-1.17.jar"
# To use 3class NER model  (Default is 7 class model)

 java  -Dner.corenlp.model=edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz \
       -Dner.impl.class=org.apache.tika.parser.ner.nltk.NLTKNERecogniser \
       -classpath "$TIKA_APP;$NLTK_RES;" org.apache.tika.cli.TikaCLI \
       --config=tika-config.xml -m 

# Observe metadata keys starting with NER_ 
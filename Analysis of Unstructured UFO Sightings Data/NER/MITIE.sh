C_PATH="$PWD/../../../.."
MITIE_RES="$C_PATH/workspace/csci599/tika/mitie-resources"
TIKA_APP="$C_PATH/Users/trpcw/.m2/repository/org/apache/tika/tika-app/1.17/tika-app-1.17.jar"
MITIE_APP="$MITIE_RES/MITIE/mitielib/javamitie.jar"
MITIE_MODEL="$MITIE_RES/MITIE/MITIE-models/english/ner_model.dat"
#"$PWD/lib/tika-app-1.17.jar"
# To use 3class NER model  (Default is 7 class model)
#set the system property to use GrobidNERecogniser class
  java -Dner.impl.class=org.apache.tika.parser.ner.mitie.MITIENERecogniser \
  -Dner.mitie.model=$MITIE_MODEL \
  -classpath "$MITIE_APP:$TIKA_APP" org.apache.tika.cli.TikaCLI \
  --config=tika-config.xml -m
# Observe metadata keys starting with NER_ 
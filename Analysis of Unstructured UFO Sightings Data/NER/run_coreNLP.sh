DIR="$PWD/../description"
OUTPUT_DIR="$PWD/output_core_nlp"
mkdir -p $OUTPUT_DIR
for file in "$DIR"/*
do
  FILENAME=$(basename $file)
  (cat "$file" | ([ $(wc -c) != 0 ] && (cat "$file" | sh CoreNLP.sh) || echo "")) | grep NER > $OUTPUT_DIR"/"$FILENAME
done
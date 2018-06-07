DIR="$PWD/../description"
OUTPUT_DIR="$PWD/output_nltk"
mkdir -p $OUTPUT_DIR
for file in "$DIR"/*
do
  FILENAME=$(basename $file)
  (cat "$file" | ([ $(wc -c) != 0 ] && (cat "$file" | sh NLTK.sh) || echo "")) | grep NER_UNITS > $OUTPUT_DIR"/"$FILENAME
done
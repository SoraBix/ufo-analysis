DIR="$PWD/../description"
OUTPUT_DIR="$PWD/output_mitie"
mkdir -p $OUTPUT_DIR
for file in "$DIR"/*
do
  FILENAME=$(basename $file)
  (cat "$file" | ([ $(wc -c) != 0 ] && (cat "$file" | sed 's/&.*;//' | sh MITIE.sh) || echo "")) | grep NER > $OUTPUT_DIR"/"$FILENAME
done
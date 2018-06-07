DIR="$PWD/../description"
OUTPUT_DIR="$PWD/output_grobid"
mkdir -p $OUTPUT_DIR
for file in "$DIR"/*
do
  FILENAME=$(basename $file)
  (cat "$file" | ([ $(wc -c) != 0 ] && (cat "$file" | sh Grobid.sh) || echo "")) | grep NER > $OUTPUT_DIR"/"$FILENAME
done
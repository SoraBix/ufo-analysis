DIR="$PWD/../description"
OUTPUT_DIR="$PWD/output"
mkdir -p $OUTPUT_DIR
for file in "$DIR"/*
do
  FILENAME=$(basename $file)
  FIRSTCHAR=${FILENAME:0:1}
  if [ "$FIRSTCHAR" = 0 ] || [ "$FIRSTCHAR" = 1 ] || [ "$FIRSTCHAR" = 2 ];
  then
    continue
  fi
  cat "$file" | sh OpenNLP.sh | grep NER_ > $OUTPUT_DIR"/"$FILENAME
done
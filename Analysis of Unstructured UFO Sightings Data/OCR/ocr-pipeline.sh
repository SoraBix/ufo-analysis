#!/bin/bash

export FILENAME=$1

#tika parser variables
#PARSER_JAR="{path/to}/ufo-pdf-parser-1.0-SNAPSHOT.jar"
#TIKA_APP="{path/to}/tika-app-1.17.jar"
PARSER_JAR="/home/yifan/CSCI599/ufo-pdf-parser-1.0-SNAPSHOT.jar"
TIKA_APP="/home/yifan/CSCI599/tika-app-1.17.jar"
PDF_CONTENT_OUTPUT_DIR="./pdfoutput"

filename_no_path=$(basename "$FILENAME")
extension="${filename_no_path##*.}"
filename_no_extension="${filename_no_path%.*}"
echo "Processing $FILENAME: extension $extension: filename no extension: $filename_no_extension"

mkdir -p $filename_no_extension
mkdir -p $filename_no_extension/tiff
mkdir -p $filename_no_extension/outtxt
pdfseparate "$FILENAME" "$filename_no_extension"/%d.pdf


#for f in $( ls $filename_no_extension | grep pdf ); do
for f in $( ls $filename_no_extension | grep '\.pdf' ); do
    the_file=$(basename $f)
    the_file_ext="${the_file##*.}"
    the_file_noext="${the_file%.*}"
    convert -density 300 $filename_no_extension/$the_file -depth 8 -alpha Off $filename_no_extension/tiff/$the_file_noext.tif
    
    # added tika parser pipeline
    java -DpdfContentOutputDir=$filename_no_extension"/"$PDF_CONTENT_OUTPUT_DIR -classpath "$TIKA_APP:$PARSER_JAR" org.apache.tika.cli.TikaCLI --config=tika-config.xml $filename_no_extension/$the_file

    #tesseract $filename_no_extension/tiff/$the_file_noext.tif $filename_no_extension/outtxt/$the_file_noext
done

# added text cleaning and extacting of tesseract output pipeline
java -jar text_extract.jar $filename_no_extension/outtxt v2_dataset_added_desc.tsv

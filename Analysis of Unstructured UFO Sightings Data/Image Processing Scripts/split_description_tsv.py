import csv
import pickle
import copy
import json
import datetime
import ast
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def load_sighting_tsv():
  input_file = 'dataset/UK_UFO_data_with_v2_dataset_added_desc.tsv'
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    next(tsv);
    sightings = []
    i = 0
    for row in tsv:
      try:
        sightings.append({
          'description': row[3],
          'line': i
        })
      except:
        pass
      i += 1
  return sightings

def write_output(file_name, description):
  output_file = 'description/{}.txt'.format(file_name)
  with open(output_file,'w') as fout:
    fout.write(description)

def main():
  sightings = load_sighting_tsv()
  for sighting in sightings:
    if int(sighting['line']) < 7730: continue
    filename = sighting['line']
    write_output(filename, sighting['description'])

if __name__ == "__main__":
	main()


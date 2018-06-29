import argparse
import csv
import json

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', help='input tsv file', required=True)
  parser.add_argument('--output', help='output file', required=True)
  parser.add_argument('--skip', help='features to skips', type=(lambda s: s.split(',')), default=[])
  args = parser.parse_args()

  sightings_json = load_sighting_tsv(args.input, args.skip)
  
  write_json(args.output, sightings_json)
def load_sighting_tsv(input_file, skips):
  sightings = []
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    headers = []
    i = 0
    for row in tsv:
      sighting = {}
      for j in range(len(row)):
        if i == 0:
          headers.append(row[j])
        else:
          try:
            if headers[j] in skips: continue
            sighting[headers[j]] = row[j]
          except Exception as e:
            print e
            pass
      if i > 0:      
        sightings.append(sighting)
      i += 1
  return sightings

def write_json(output_file, result):
  with open(output_file, 'w') as outfile:
    json.dump(result, outfile)

if __name__ == "__main__":
	main()

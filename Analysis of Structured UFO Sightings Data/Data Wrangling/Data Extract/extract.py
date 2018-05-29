

import argparse
import csv
import json

def switcher(feature):
  switcher = {
    'dist_to_airport': lambda x: int(float(x)/5),
    'dist_to_military_base': lambda x: int(float(x)/5),
    'county.population': lambda x: int(float(x)/100000),
    'military_area': lambda x: int(float(x)/500),
  }
  # Get the function from switcher dictionary
  return switcher.get(feature, lambda x:x)

def read_input(input_file, features):
  sighteds = []
  with open(input_file, 'r') as json_file:
    sighteds = json.load(json_file)
  
  results = []
  for sighted_obj in sighteds:
    tmp = {}
    try:
      for feature in features:
        feature_split = feature.split('.')
        obj = sighted_obj
        is_found = False
        last_key = None
        for key in feature_split:
          if key in obj:
            obj = obj[key]
            last_key = key
            is_found = True
        if is_found:
          tmp[last_key] = switcher(feature)(obj)
      results.append(tmp)
    except Exception as e:
      print e
      pass
      
  return results

def write_output(output_dir, results):
  for i in range(0, len(results)):
    with open(output_dir+'/'+results[i]['sighted_at']+str(i)+'.json','w') as outfile:
      json.dump(results[i], outfile)

def arg_as_list(s):
  return s.split(',')
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', help='input tsv file', required=True)
  parser.add_argument('--outputDir', help='output dir', required=True)
  parser.add_argument('--features', help='features to extract', type=(lambda s: s.split(',')), default=[])
  args = parser.parse_args()
  results = read_input(args.input, args.features)
  write_output(args.outputDir, results)

if __name__ == "__main__":
	main()


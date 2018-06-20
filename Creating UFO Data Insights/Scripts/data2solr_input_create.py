import json
import copy
import hashlib
def create_update_json_word(json_data):
  update_data = []
  i = 0
  for row in json_data:
    tmp = { 
      #'id': '%s-%s-%s' % (row['sighted_at'], row['reported_at'], hashlib.md5(row['location'] + row['shape']+row['airport_type']).hexdigest()),
      'id': i,
      'county.countyName': "",
      "county.state": "", 
      "county.countyID": "", 
      "county.population": 0,
      "weather.dusty": False, 
      "weather.foggy": False, 
      "weather.rainy": False, 
      "weather.windy": False, 
      "weather.snowy": True
    }
    i += 1
    for key in row.keys():
      tmp[key] = row[key]
    update_data.append(tmp)
  return update_data

def load_json(input_file):
  with open(input_file) as jin:
    json_data = json.load(jin)
  return json_data

def write_json(output_file, result):
  with open(output_file, 'w') as jout:
    json.dump(result, jout)

def main():
  json_data = load_json('dataset/v2_dataset.json')
  update_data = create_update_json_word(json_data)
  write_json('dataset/solr_create_data.json', update_data)

if __name__ == "__main__":
	main()
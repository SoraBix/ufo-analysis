import json
import csv
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def load_json():
  json_file = 'dataset/output_with_population.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  return json_obj

def load_csv():
  input_file = 'dataset/fips_codes.csv'
  with open(input_file, 'r') as csvfile:
    lines = list(csv.reader(csvfile))
    #lines = f.read().splitlines()
    topic = lines[0]
    data = lines[1:]
  fips_code_obj = {}
  for d in data:
    fips_code_obj[d[0] +';' +d[5]] = d[1]+''+d[2]
  return fips_code_obj

def write_output(result):
  output_file = 'dataset/output_with_population.json'
  with open(output_file,'w') as fout:
    json.dump(result, fout)

def find_fips_code(sighting, fips_code_obj):
  county = sighting['county']['countyName']
  state = sighting['county']['state']
  key = state + ';' + county
  if key in fips_code_obj:
    return fips_code_obj[key]
  return None
def main():
  sighting_json = load_json()
  fips_code_obj = load_csv()
  result_json = {}
  for sighting in sighting_json:
    fips_code = find_fips_code(sighting, fips_code_obj)
    if fips_code not in result_json:
      result_json[fips_code] = 1
    else:
      result_json[fips_code] = result_json[fips_code] + 1
  write_output(result_json)

if __name__ == "__main__":
	main()


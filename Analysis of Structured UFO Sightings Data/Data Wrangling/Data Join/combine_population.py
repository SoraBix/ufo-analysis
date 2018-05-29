import json
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
  json_file = 'dataset/output.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  return json_obj

def load_population():
  json_file = 'dataset/population.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  population_json = {}
  for population_yr in json_obj:
    population_json[population_yr['year']] = population_yr['county']
  return population_json

def write_output(result):
  output_file = 'dataset/output_with_population.json'
  with open(output_file,'w') as fout:
    json.dump(result, fout)

def find_closest_county(sighting, population_json):
  year = sighting['sighted_at'][0:4]
  if year in population_json:
    min_county = None
    s_lat = sighting['latitude']
    s_lng = sighting['longitude']
    min_dist = float('inf')
    for county in population_json[year]:
      try:
        c_lat = county['latitude']
        c_lng = county['longitude']
        dist = haversine(s_lng, s_lat, c_lng, c_lat)
        if dist < min_dist:
          min_dist = dist
          min_county = county
      except:
        pass
    # if the distance is more than 300km, we can't say that it is belong to that county
    return min_county if min_dist < 300 else None
  return None

def main():
  sighting_json = load_json()
  population_json = load_population()
  result_json = []
  for sighting in sighting_json:
    county = find_closest_county(sighting, population_json)
    if county is None: continue
    sighting['county'] = {
      'countyID': county['countyID'],
      'state': county['state'],
      'countyName': county['countyName'],
      'population': county['population']
    }
    result_json.append(sighting)
  write_output(result_json)

if __name__ == "__main__":
	main()


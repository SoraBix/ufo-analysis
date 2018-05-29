import csv
import pickle
import copy
import json
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def find_min_distance_to_military_base(militaries, sighting_jsons):
  for data in sighting_jsons:
    sighted_coord = (data['latitude'], data['longitude'])
    min_dist = float("inf")
    min_mil = 'none'
    for mil in militaries:
      airport_coord = (mil['lng'],mil['lat'])
      dist = great_circle(sighted_coord, airport_coord).miles
      if dist < min_dist: 
        min_dist = dist
        min_mil = mil
    data['dist_to_military_base'] = min_dist
    data['military_component'] = min_mil['component']
    data['military_site'] = min_mil['site']
    data['military_area'] = min_mil['shapeSTArea']
  return sighting_jsons

def load_military_base():
  input_file = 'dataset/MilitaryBase.json'
  with open(input_file, 'r') as jsonfile:
    militaries = json.load(jsonfile)
  return militaries

def write_output(result):
  output_file = 'dataset/output_with_military_base.json'
  with open(output_file,'w') as tsvout:
    json.dump(result, tsvout)

def load_json():
  input_file = 'dataset/output_with_airport.json'
  with open(input_file, 'r') as jsonfile:
    output = json.load(jsonfile)
  return output

def main():
  result_json = load_json()
  militaries = load_military_base()
  result_json = find_min_distance_to_military_base(militaries, result_json)
  write_output(result_json)

if __name__ == "__main__":
	main()


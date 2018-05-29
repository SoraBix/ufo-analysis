import csv
import pickle
import copy
import json
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def load_dataset():
  sightings = []
  input_file = 'dataset/ufo_awesome.tsv'
  with open(input_file, 'r') as tsvfile:
    lines = list(csv.reader(tsvfile, delimiter = '\t'))
    sightings = [line[0:5] for line in lines]

  
  return sightings
  
def find_min_distance_to_airport(airport_codes_obj, sightings):
  counter = 0
  cache_dist_file = 'cache_dist.json'
  cache_coord_file = 'cache_coord.json'
  cord_to_dist_cache = {}
  output_arr = []
  header = ['sighted_at','reported_at','location','shape','duration','latitude','longitude','airport_type','airport_name','dist_to_airport']
  try:	
    with open(cache_dist_file, 'rb') as fin:
      dist_hash = pickle.load(fin)
    print 1
  except Exception as e:
    print e,2
    dist_hash = {}
  try:
    with open(cache_coord_file, 'rb') as fin:
      coord_hash = pickle.load(fin)
  except Exception as e:
    print e,3
    coord_hash = {}
  # with open(cache_dist_file,'w') as fout:
  #     pickle.dump(dist_hash, fout, pickle.HIGHEST_PROTOCOL)
  try:
    geolocator = Nominatim()
    
    for data in sightings:
      counter = counter + 1
      print counter
      if counter in dist_hash:
        min_dist = dist_hash[counter]['min_dist']
        min_airport = dist_hash[counter]['min_airport']
        cord_to_dist_cache[data[2]] = dist_hash[counter]
        sighted_at = coord_hash[data[2]]
      else:
        if data[2] in cord_to_dist_cache:
          min_dist = cord_to_dist_cache[data[2]]['min_dist']
          min_airport = cord_to_dist_cache[data[2]]['min_airport']
        else:
          if data[2] in coord_hash:
            sighted_at = coord_hash[data[2]]
          else:
            print data[2]
            sighted_at = geolocator.geocode(data[2], timeout=15)
            coord_hash[data[2]] = sighted_at

          if sighted_at is None: continue
          sighted_coord = (sighted_at.latitude, sighted_at.longitude)
          min_dist = float("inf")
          min_airtport = 'none'
          for airport in airport_codes_obj['data']:
            airport_coord = (airport[3].split(',')[1],airport[3].split(',')[0])
            dist = great_circle(sighted_coord, airport_coord).miles
            if dist < min_dist: 
              min_dist = dist
              min_airport = airport[0]
        dist_hash[counter] = {
          'min_dist':min_dist,
          'min_airport': min_airport
        }
      airport = airport_codes_obj['airport_map'][min_airport]
      tmp_obj = {
        'sighted_at': data[0],
        'reported_at': data[1],
        'location': data[2],
        'shape': data[3],
        'duration': data[4],
        'latitude': sighted_at.latitude,
        'longitude': sighted_at.longitude,
        'airport_type': airport[1],
        'airport_name': airport[2],
        'dist_to_airport': min_dist
      }
      output_arr.append(tmp_obj)
  finally:
    print 'done'
    with open(cache_dist_file,'wb') as fout:
      pickle.dump(dist_hash, fout, pickle.HIGHEST_PROTOCOL)
    with open(cache_coord_file,'wb') as fout:
      pickle.dump(coord_hash, fout, pickle.HIGHEST_PROTOCOL)
  return output_arr
  
def load_airport_codes():
  input_file = 'dataset/airport-codes.csv'
  with open(input_file, 'r') as csvfile:
    lines = list(csv.reader(csvfile))
    #lines = f.read().splitlines()
    topic = lines[0]
    data = lines[1:]
    airport_map = {}
    for o in data:
      airport_map[o[0]] = o
  return {
    'topic': topic,
    'data': data,
    'airport_map': airport_map
  }


def write_output(result):
  output_file = 'dataset/output_with_airport.json'
  with open(output_file,'w') as tsvout:
    # writer = csv.writer(tsvout, delimiter = '\t',  lineterminator='\n')
    # writer.writerows(output_arr)
    json.dump(result, tsvout)

def main():
  airport_codes_obj = load_airport_codes()
  sightings = load_dataset()
  result_json = find_min_distance_to_airport(airport_codes_obj, sightings)
  write_output(result_json)

if __name__ == "__main__":
	main()


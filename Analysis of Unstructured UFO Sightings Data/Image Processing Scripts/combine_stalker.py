import csv
import pickle
import copy
import json
import datetime
import ast
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def find_min_distance_to_stalker_report(stalkers, sightings, sentence_map, object_map):
  results = []
  for data in sightings:
    sighted_coord = (data['latitude'], data['longitude'])
    min_dist = float("inf")
    min_stk = None
    for stk in [x for x in stalkers if x['occurred'] == data['sighted_at']]:
      stk_coord = (stk['latitude'],stk['longitude'])
      dist = great_circle(sighted_coord, stk_coord).miles
      if dist < min_dist: 
        min_dist = dist
        min_stk = stk
    if min_stk is None or min_dist > 500: continue
    #print min_dist, data,  min_stk
    data['dist_to_stalker'] = min_dist
    data['stalker_id'] = min_stk['id']
    data['objects'] = object_map[min_stk['id']] if min_stk['id'] in object_map else None
    data['sentence'] = sentence_map[min_stk['id']][0] if min_stk['id'] in sentence_map else None
    results.append(data)
  return results

def load_stalker_tsv():
  input_file = 'dataset/stalker_reports.tsv'
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    next(tsv, None) 
    stalkers = []
    for row in tsv:
      try:
        stalkers.append({
          'latitude': row[5],
          'longitude': row[6],
          'occurred': datetime.datetime.fromtimestamp(int(row[7])/1000.0).strftime('%Y%m%d'),
          'id': row[3]
        })
      except: 
        pass
  return stalkers

def write_output(result):
  output_file = 'dataset/output_with_stalker.json'
  with open(output_file,'w') as tsvout:
    json.dump(result, tsvout)
def write_output_tsv(result):
  output_file = 'dataset/output_with_stalker.tsv'
  #stalker_id	sentence	reported_at	dist_to_stalker	longitude	objects	latitude	sighted_at
  with open(output_file, 'w') as output_file:
    output_file.writelines("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format('sighted_at','reported_at','longitude','latitude','dist_to_stalker','stalker_id','objects','sentence'))
    for c in result:
      output_file.writelines("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(c['sighted_at'],c['reported_at'],c['longitude'],c['latitude'],c['dist_to_stalker'],c['stalker_id'],c['objects'],c['sentence']))


def load_sighting_tsv():
  input_file = 'dataset/v2_dataset_added_desc.tsv'
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    next(tsv, None) 
    sightings = []
    for row in tsv:
      sightings.append({
        'latitude': row[6],
        'longitude': row[8],
        'sighted_at': row[14],
        'reported_at': row[12]
      })
  return sightings

def load_sentences_id():
  input_file = 'dataset/sentences.tsv'
  sentence_map = {}
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    next(tsv, None) 
    for row in tsv:
      sentence_map[row[0]] = ast.literal_eval(row[1])
  return sentence_map

def load_objects_id():
  input_file = 'dataset/objects.tsv'
  object_map = {}
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    next(tsv, None) 
    for row in tsv:
      object_map[row[0]] = row[1]
  return object_map

def main():
  sightings = load_sighting_tsv()
  stalkers = load_stalker_tsv()
  sentence_map = load_sentences_id()
  object_map = load_objects_id()
  #print stalkers[0]
  #print sightings[0]
  result_json = find_min_distance_to_stalker_report(stalkers, sightings, sentence_map, object_map)
  write_output(result_json)
  write_output_tsv(result_json)

if __name__ == "__main__":
	main()


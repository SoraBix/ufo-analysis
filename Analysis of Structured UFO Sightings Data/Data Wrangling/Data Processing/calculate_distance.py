import json
import csv
def load_json():
  json_file = 'dataset/output_with_weather.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  return json_obj

def write_output(output_file, result):
  output_file = 'dataset/' + output_file
  with open(output_file,'w') as fout:
    json.dump(result, fout)

def find_dist(sighting):
  dist_airport = sighting['dist_to_airport']
  dist_military = sighting['dist_to_military_base']
  return dist_airport, dist_military

def main():
  sighting_json = load_json()
  count_airport = {}
  count_military = {}
  for sighting in sighting_json:
    dist_airport, dist_military = find_dist(sighting)
    group_airport = int(dist_airport/5)
    if group_airport > 6: group_airport = 6
    if group_airport not in count_airport: count_airport[group_airport] = 0
    count_airport[group_airport] +=1

    group_military = int(dist_military/10)
    if group_military > 19: group_military = 19
    if group_military not in count_military: count_military[group_military] = 0
    count_military[group_military] +=1
  write_output('distance_airport.json',count_airport)
  write_output('distance_military.json',count_military)

if __name__ == "__main__":
	main()


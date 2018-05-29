import json
import csv
def load_json():
  json_file = 'dataset/output_with_weather.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  return json_obj

def write_output(result):
  output_file = 'dataset/population_group.json'
  with open(output_file,'w') as fout:
    json.dump(result, fout)

def find_population(sighting):
  population = sighting['county']['population']
  return population

step_size = 50000
def get_population_group(population):
  return int(population / step_size)
def main():
  sighting_json = load_json()
  result_json = {}
  for sighting in sighting_json:
    population = find_population(sighting)
    group = get_population_group(population)
    if group not in result_json:
      result_json[group] = {
        'population': str(group * step_size) + '-' + str((group+1)* step_size) ,
        'count':1
      }
    else:
      result_json[group]['count'] = result_json[group]['count'] + 1
  write_output(result_json)

if __name__ == "__main__":
	main()


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

def find_weather_type(sighting):
  weather = sighting['weather']
  w_types = []
  for weather_type in ['foggy', 'rainy', 'windy', 'snowy', 'dusty']:
    if weather[weather_type]: w_types.append(weather_type)
  
  return w_types

def main():
  sighting_json = load_json()
  count = {'foggy':0, 'rainy':0, 'windy':0, 'snowy':0, 'dusty':0}
  for sighting in sighting_json:
    weather_types = find_weather_type(sighting)
    for w_type in weather_types:
      count[w_type] +=1
  write_output('weather_calc.json',count)

if __name__ == "__main__":
	main()


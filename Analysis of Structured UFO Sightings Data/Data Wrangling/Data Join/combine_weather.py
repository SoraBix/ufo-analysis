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
  json_file = 'dataset/output_with_military_base.json'
  with open(json_file, 'r') as f:
    json_obj = json.load(f)
  return json_obj

def load_weather():
  weather_json = {}
  json_files = [
    'dataset/weather_1990.json',
    'dataset/weather_1991.json',
    'dataset/weather_1992.json',
    'dataset/weather_1993.json',
    'dataset/weather_1994.json',
    'dataset/weather_1995.json',
    'dataset/weather_1996.json',
    'dataset/weather_1997.json',
    'dataset/weather_1998.json',
    'dataset/weather_1999.json'
  ]
  for json_file in json_files:
    with open(json_file, 'r') as f:
      json_obj = json.load(f)
    
    for weather in json_obj:
      for key in weather:
        weather_json[key] = weather[key]
      
  return weather_json

def write_output(result):
  output_file = 'dataset/output_with_weather.json'
  with open(output_file,'w') as fout:
    json.dump(result, fout)

def find_closest_weather_station(sighting, weather_json):
  date = sighting['sighted_at']
  min_w_station = None
  if date in weather_json:
    s_lat = sighting['latitude']
    s_lng = sighting['longitude']
    min_dist = float('inf')
    for weather_station in weather_json[date]:
      if 'Dusty' in weather_station['weather'] and \
         'Snowy' in weather_station['weather'] and \
         'Rainy' in weather_station['weather'] and \
         'Windy' in weather_station['weather'] and \
         'Foggy' in weather_station['weather']:
        w_lat = weather_station['Latitude']
        w_lng = weather_station['Longitude']
        dist = haversine(s_lng, s_lat, w_lng, w_lat)
        if dist < min_dist:
          min_dist = dist
          min_w_station = weather_station
  return min_w_station

def main():
  # load input json
  sighting_json = load_json()
  # load weather json
  weather_json = load_weather()

  result_json = []
  for sighting in sighting_json:
    weather_station = find_closest_weather_station(sighting, weather_json)
    if weather_station is None: continue
    sighting['weather'] = {
      'dusty':weather_station['weather']['Dusty'],
      'snowy':weather_station['weather']['Snowy'],
      'rainy':weather_station['weather']['Rainy'],
      'windy':weather_station['weather']['Windy'],
      'foggy':weather_station['weather']['Foggy']
    }
    result_json.append(sighting)
  write_output(result_json)

if __name__ == "__main__":
	main()


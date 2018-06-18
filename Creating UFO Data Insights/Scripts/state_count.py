import json
import copy
def count_state(json_data):
  default_each = {
      '1990': 0,
      '1991': 0,
      '1992': 0,
      '1993': 0,
      '1994': 0,
      '1995': 0,
      '1996': 0,
      '1997': 0,
      '1998': 0,
      '1999': 0
    }
  state_count = {}
  for row in json_data:
    state = row['county']['state']
    year = row['sighted_at'][0:4]
    if state not in state_count:
      state_count[state] = copy.copy(default_each)
    state_count[state][year] += 1
  return state_count

def format_output(input):
  output = []
  for state in input.keys():
    output.append({
      "state": state,
      '1990': input[state]['1990'],
      '1991': input[state]['1991'],
      '1992': input[state]['1992'],
      '1993': input[state]['1993'],
      '1994': input[state]['1994'],
      '1995': input[state]['1995'],
      '1996': input[state]['1996'],
      '1997': input[state]['1997'],
      '1998': input[state]['1998'],
      '1999': input[state]['1999']
    })
  return output
def load_json(input_file):
  with open(input_file) as jin:
    json_data = json.load(jin)
  return json_data

def write_json(output_file, result):
  with open(output_file, 'w') as jout:
    json.dump(result, jout)

def main():
  json_data = load_json('dataset/v1_dataset_with_county_weather.json')
  state_count = count_state(json_data)
  formatted = format_output(state_count)
  write_json('dataset/state_count.json', formatted)

if __name__ == "__main__":
	main()
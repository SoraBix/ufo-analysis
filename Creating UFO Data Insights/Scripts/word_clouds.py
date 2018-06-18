import json

def count_word(json_data):
  count_ner = {
      'ner_location': {},
      'ner_organization': {},
      'ner_person': {},
      'ner_date': {},
      'ner_time': {},
      'ner_measurements': {},
      'ner_misc': {},
      'ner_units': {}
    }
  categories = count_ner.keys()
  for row in json_data:
    for category in categories:
      words = [x.strip() for x in row[category].split(',')]
      for word in words:
        if len(word) == 0: continue
        if word not in count_ner[category]:
          count_ner[category][word] = 0
        count_ner[category][word] += 1
  return count_ner

def load_json(input_file):
  with open(input_file) as jin:
    json_data = json.load(jin)
  return json_data

def write_json(output_file, result):
  with open(output_file, 'w') as jout:
    json.dump(result, jout)

def main():
  json_data = load_json('dataset/v2_dataset.json')
  ner_count = count_word(json_data)
  write_json('dataset/ner_word_clouds.json', ner_count)

if __name__ == "__main__":
	main()
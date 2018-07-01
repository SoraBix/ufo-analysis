import json
import copy
import ast
def create_update_json_word(json_data):
  update_data = []

  for row in json_data:
    tmp = {}
    for key in row.keys():
      target_key = key
      if key == 'filename':
        target_key = 'id'
        tmp[target_key] = ('/images/%s' % row[key])
      elif key == 'objects':
        tmp[target_key] = { "set": ast.literal_eval(row[key])}
        
      else:
        tmp[target_key] = { "set": row[key]}
    if len(tmp["objects"]["set"]) == 0: continue
    update_data.append(tmp)
  return update_data

def load_json(input_file):
  with open(input_file) as jin:
    json_data = json.load(jin)
  return json_data

def write_json(output_file, result):
  with open(output_file, 'w') as jout:
    json.dump(result, jout)

def main():
  json_data = load_json('dataset/image_objects.json')
  update_data = create_update_json_word(json_data)
  write_json('dataset/solr_update_image_objects.json', update_data)

if __name__ == "__main__":
	main()
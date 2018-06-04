import csv
from os import listdir
from os.path import isfile, join, basename
keys = [('NER_LOCATION','ner_location'),
  ('NER_ORGANIZATION','ner_organization'),
  ('NER_PERSON','ner_person'),
  ('NER_DATE','ner_date'),
  ('NER_TIME','ner_time'),
  ('NER_MEASUREMENTS', 'ner_measurements'),
  ('NER_MISC','ner_misc'),
  ('NER_UNITS','ner_units')
]

def main():
  v2 = load_v2_sighting_tsv()
  ner_openNLP = load_nerfiles('./extra/output/')
  ner_coreNLP = load_nerfiles('./extra/output_core_nlp/')
  ner_mitie = load_nerfiles('./extra/output_mitie/')
  ner_nltk = load_nerfiles('./extra/output_nltk/')
  ner_grobid = load_nerfiles('./extra/output_grobid/')
  ner_combine = {}
  for line_no in ner_coreNLP:
    ner_combine[line_no] = {
      'ner_location': set(),
      'ner_organization': set(),
      'ner_person': set(),
      'ner_date': set(),
      'ner_time': set(),
      'ner_measurements': set(),
      'ner_misc': set(),
      'ner_units': set()
    }
    for ner in [ner_openNLP, ner_coreNLP, ner_mitie, ner_nltk, ner_grobid]:
      for label in keys:
        try:
          ner_combine[line_no][label[1]] = ner_combine[line_no][label[1]].union(ner[line_no][label[1]])
        except:
          pass

  line = 0
  for data in v2:
    ner = ner_combine[str(line)]
    for key in ner:
      data[key] = ','.join(ner[key])
    line += 1
  write_tsv(v2)
  #print ner
  # for data in v2:
  #   data['description'] = ''
  #   data_original = [x for x in original if x['location'] == data['location'] and \
  #   x['reported_at'] == data['reported_at'] and \
  #   x['sighted_at'] == data['sighted_at']]
  #   if len(data_original) > 0:
  #     data['description'] = data_original[0]['description']
  #     #print data['description']
  # write_tsv(v2)

def load_v2_sighting_tsv():
  sightings = []
  input_file = 'dataset/v2_dataset_added_desc.tsv'
  with open(input_file, 'rb') as tsvfile:
    tsv = csv.reader(tsvfile, delimiter='\t')
    headers = []
    i = 0
    for row in tsv:
      sighting = {}
      for j in range(len(row)):
        if i == 0:
          headers.append(row[j])
        else:
          try:
            sighting[headers[j]] = row[j]
          except Exception as e:
            print e
            pass
      if i > 0:      
        sightings.append(sighting)
      i += 1
  return sightings
def load_nerfiles(output_dir):
 
  onlyfiles = [f for f in listdir(output_dir) if isfile(join(output_dir, f))]
  ners = {}
  for infile in onlyfiles:
    ner = {
      'ner_location': set(),
      'ner_organization': set(),
      'ner_person': set(),
      'ner_date': set(),
      'ner_time': set(),
      'ner_measurements': set(),
      'ner_misc': set(),
      'ner_units': set()
    }
    line_no = infile.split('.')[0]
    with open(output_dir + '/' + infile) as f:
      lines = f.read().splitlines()
      for line in lines:
        for label in keys:
          if line.find(label[0] + "") >= 0:
            ner[label[1]].add(line[len(label[0])+2:].strip())
    ners[line_no] = ner
  return ners



def write_tsv(result):
  output_file = 'dataset/v2_dataset_added_desc_ner.tsv'
  with open(output_file, 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(result[0].keys()), delimiter='\t', lineterminator='\n')
    dw.writeheader()
    dw.writerows(result)
if __name__ == "__main__":
	main()

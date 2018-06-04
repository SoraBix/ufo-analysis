from os import listdir
from os.path import isfile, join
import requests
import csv

def main():
  url = 'http://localhost:8764/inception/v3/caption/image'
  path = 'images'
  image_files = [f for f in listdir(path) if isfile(join(path, f))]
  captions_map = {}
  count = 0
  for image_file in image_files:
    print image_file
    id = image_file[0:image_file.index("_submit")]
    if id not in captions_map: captions_map[id] = set()
    payload = file('{}/{}'.format(path,image_file),'rb').read()
    retries = 0
    while retries < 3:
      try:
        r = requests.post(url, data=payload)
        data = r.json()  
        for sentence in [x['sentence'] for x in data['captions']]:
          captions_map[id].add(sentence.strip())
        break
      except:
        retries += 1
    count += 1
    #if count > 25: break
  reports = []
  for key, value in captions_map.iteritems():
    reports.append({
      'id': key,
      'sentences': [x.encode('utf-8') for x in value]
    })
  write_tsv('sentences.tsv', reports)

def write_tsv(file_name, content):
  with open(file_name, 'w') as output_file:
    output_file.writelines("{}\t{}\n".format('id','sentences'))
    for c in content:
      output_file.writelines("{}\t{}\n".format(c['id'],c['sentences']))

if __name__ == "__main__":
	main()
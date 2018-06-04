from os import listdir
from os.path import isfile, join
import requests
import csv

def main():
  url = 'http://localhost:8764/inception/v4/classify/image'
  path = 'images'
  image_files = [f for f in listdir(path) if isfile(join(path, f))]
  objects_map = {}
  count = 0
  for image_file in image_files:
    print image_file
    id = image_file[0:image_file.index("_submit")]
    if id not in objects_map: objects_map[id] = set()
    payload = file('{}/{}'.format(path,image_file),'rb').read()
    retries = 0
    while retries < 3:
      try:
        r = requests.post(url, data=payload)
        data = r.json() 
        for classname in data['classnames']:
          objects_map[id].add(classname.strip())
        break
      except:
        retries += 1
    count += 1
    #if count > 5: break
  reports = []
  for key, value in objects_map.iteritems():
    reports.append({
      'id': key,
      'objects': [x.encode('utf-8') for x in value]
    })
  write_tsv('objects.tsv', reports)

def write_tsv(file_name, content):
  with open(file_name, 'w') as output_file:
    output_file.writelines("{}\t{}\n".format('id','objects'))
    for c in content:
      output_file.writelines("{}\t{}\n".format(c['id'],c['objects']))

if __name__ == "__main__":
	main()
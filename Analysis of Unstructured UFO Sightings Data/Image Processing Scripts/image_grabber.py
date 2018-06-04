import urllib2
import requests
import json
import csv
import time
def main():
  page = 0
  size = 25
  reports = []
  while True:
    time.sleep(3)
    url = 'http://ufostalker.com:8080/eventsByTag?tag=photo&page={}&size={}'.format(page, size)
    print url
    attempts = 0
    contents = []
    while attempts < 3:
        try:
            response = urllib2.urlopen(url, timeout = 5)
            resp = response.read()
            resp_json = json.loads(resp)
            contents = resp_json['content']
            for content in contents:
              id = content['id']
              urls = [] if content['urls'] is None else content['urls']
              reports.append({
                'id': content['id'],
                'description': ("" if content['detailedDescription'] is None else content['detailedDescription']).encode('utf-8').strip(),
                'latitude': content['latitude'],
                'longitude': content['longitude'],
                'city': ("" if content['city'] is None else content['city']).encode('utf-8').strip(),
                'country': ("" if content['country'] is None else content['country']).encode('utf-8').strip(),
                'occurred': content['occurred'],
                'images': [url[url.rfind('/')+1:] for url in urls if url.endswith(('.jpg','.jpeg','.png','.gif','.bmp'))]
              })
              if id >= 2838: continue
              #if id > 83679: continue
              for image_url in [url for url in urls if url.lower().endswith(('.jpg','.jpeg','.png','.gif','.bmp'))]:
                try:
                  image_content = get_image(image_url)
                  file_name = image_url[image_url.rfind('/')+1:]
                  write_file(file_name, image_content)
                except:
                  pass
              #image_urls = content['urls']
              #latitude = content['latitude']
            break
        except urllib2.URLError as e:
            attempts += 1
            print e
            print type(e)
    if len(contents) == 0: break
    page += 1
  write_tsv('stalker_reports.tsv', reports)

def get_image(url):
  attempts = 0
  while attempts < 3:
    try:
      resp = requests.get(url)
      return resp.content
    except urllib2.URLError as e:
      attempts += 1
      print e
      print type(e)

def write_file(file_name, content):
  f = open( file_name, 'wb' )
  f.write( content )
  f.close()
def write_tsv(file_name, content):
  with open(file_name, 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(content[0].keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(content)

if __name__ == "__main__":
	main()
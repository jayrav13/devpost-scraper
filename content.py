from lxml import html
import os
import sys
import json
import grequests

urls = []
count = 1

for filename in os.listdir('./data'):
	if filename.startswith('data-') and filename.endswith('.json'):

		with open('./data/' + filename) as f:
			try:
				local = json.load(f)

			except:
				print "ERROR: " + filename
				continue

		urls.extend([elem['url'] for elem in local])

		f.close()

print "Pulled " + str(len(urls)) + " urls."

import requests

def collect_data():
	global count
	while True:
		url = q.get()

		try:
			r = requests.get(url)
			details = open('./content/' + str(count) + '.json', 'w')
			details.write(json.dumps({"text": r.text, "url": url}) + "\n")
			details.close()
			count += 1
			print count, r.status_code, url
		except:
			print count, r.status_code, url

from Queue import Queue
from threading import Thread
import json

concurrent = 8

q = Queue(concurrent)

for i in range(0, concurrent):
	t = Thread(target=collect_data)
	t.daemon = True
	t.start()

try:
	for url in urls:
		q.put(url)

	q.join()

except KeyboardInterrupt:
	sys.exit(1)


# Imports
from lxml import html
import json
import sys
import os
import gc

# Prepare array for all 
content = []
count = 0

# Iterate through all of the content files.
for filename in os.listdir('./content'):
	count += 1
	try:
		data = open('./content/' + filename)
		load = json.load(data)

		content.append({"url": load['url'], "filename": filename})
		if count % 100 == 0:
			print count
		data.close()
	except:
		pass

print len(content)

projects = []
success = 0

for filename in os.listdir('./data'):
	data = open('./data/' + filename)
	load = json.load(data)

	for elem in load:
		project = [c for c in content if c['url'].strip() == elem['url'].strip()]

		if len(project) == 1:

			details = open('./content/' + project[0]['filename'])
			details = json.load(details)

			tree = html.document_fromstring(details['text'])
			c = tree.xpath('//div[@id="app-details-left"]')
			if(len(c) == 1):
				elem['description'] = c[0].text_content()
				projects.append(elem)
				success += 1
				print "SUCCESS: " + elem['url']

			else:
				print "FAILED: " + elem['url']

	data.close()

f = open('data.json', 'w')
f.write(json.dumps(projects, indent=4, sort_keys=True))
f.close()
print len(projects)


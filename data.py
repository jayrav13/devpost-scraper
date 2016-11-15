# Imports
from lxml import html
import requests
import json

# Set a counter for While loop
counter = 0

while True:

    counter += 1
    page = requests.get('https://devpost.com/software/search?query=&page=' + str(counter)).json()["software"]
    if(len(page) == 0):
        break

    f = open('data/data-' + str(counter) + '.json', 'a+', 0)
    f.write(json.dumps(page) + '\n')
    f.close()

    print(str(counter) + " project blocks.")


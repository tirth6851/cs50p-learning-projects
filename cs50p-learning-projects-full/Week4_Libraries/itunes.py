import requests
import sys
import json

if len(sys.argv) != 2:
  sys.exit()

respose = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])



o=respose.json()
for i in o["results"]:
  print(i["trackName"])



"""
print(json.dumps(respose.json(), indent=2))

"""

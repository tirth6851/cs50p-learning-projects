import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

respose = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(respose.json())


'''
test
'''
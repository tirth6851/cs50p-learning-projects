import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

requests.get("hhttps://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
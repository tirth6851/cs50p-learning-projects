import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

respose = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
<<<<<<< Updated upstream
print(respose.json())
=======
print(respose.json())
>>>>>>> Stashed changes

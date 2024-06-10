import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])





"""
import sys

#Check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguments")

# Print name Tags    
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
"""






"""
import statistics
print(statistics.mean([100, 90]))
"""

"""
import random
#from random import choice

cards = ["jack", "queen", "king"]
random.shuffle(cards) 
for card in cards:
    print(card)
"""
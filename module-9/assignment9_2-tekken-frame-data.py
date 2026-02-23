# This program uses an api to grab data from a database of moves
# from the fighting game "Tekken 8", specifically from the
# character "Bryan Fury".


import requests
import json

# Function that neatly displays data retrieved from the next block
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Retrieves data from api
response = requests.get('https://tekkendocs.com/api/t8/bryan/framedata')


print(response.status_code)
jprint(response.json())

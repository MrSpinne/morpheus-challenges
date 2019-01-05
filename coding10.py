# Get a string from chal_url and post converted float to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/10/"
sol_url = "https://cc.the-morpheus.de/solutions/10/"

g = requests.get(chal_url).text
p = requests.post(sol_url, json.dumps({"token": float(g)})).text

print(float(g)) # Print solution
print(p) # Print code "TMT{K84m4dvgwKpU8B6nrBeKNfZb}"

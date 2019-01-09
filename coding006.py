# Get number from chal_url and post binary version to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/6/"
sol_url = "https://cc.the-morpheus.de/solutions/6/"

g = int(requests.get(chal_url).text)
b = ""
while g >= 1:
    b = str(int(g % 2)) + b # Attach every new bit calculated to beginning
    g = int(g // 2)

p = requests.post(sol_url, json.dumps({"token": b})).text

print(b) # Print solution
print(p) # Print code "TMT{O6gjviTFP0f1Uv25chkI}"

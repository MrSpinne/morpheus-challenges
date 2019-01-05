# Get number from chal_url and post binary version to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/6/"
sol_url = "https://cc.the-morpheus.de/solutions/6/"

g = int(requests.get(chal_url).text)
bin = ""
while g >= 1:
    bin = str(int(g % 2)) + bin
    g = int(g // 2)

p = requests.post(sol_url, json.dumps({"token": bin})).text

print(bin) # Print solution
print(p) # Print code "TMT{O6gjviTFP0f1Uv25chkI}"

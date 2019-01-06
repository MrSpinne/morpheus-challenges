# Get a string from chal_url and post if brackets are set correctly to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/11/"
sol_url = "https://cc.the-morpheus.de/solutions/11/"

g = requests.get(chal_url).text
opened = 0
for char in g:
    if char == "(":
        opened += 1
    elif char == ")":
        opened -= 1
        if opened < 0:
            break

p = requests.post(sol_url, json.dumps({"token": opened == 0})).text

print(opened == 0) # Print solution
print(p) # Print code "TMT{t2VdCXazxCHu11K37BeS}"

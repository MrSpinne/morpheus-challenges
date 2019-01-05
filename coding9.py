# Same as coding7.py but now the nearest indices

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/9/"
sol_url = "https://cc.the-morpheus.de/solutions/9/"

g = requests.get(chal_url).json()
possible_indices = {}
for index1, num1 in enumerate(g["list"]):
    for index2, num2 in enumerate(g["list"]):
        if index1 != index2 and num1 + num2 == g["k"] and index2 - index1 > 0:
            possible_indices[index2 - index1] = [index1, index2]

indices = possible_indices[min(possible_indices.keys())]
p = requests.post(sol_url, json.dumps({"token": indices})).text

print(indices) # Print solution
print(p) # Print code "TMT{5umm3d17upr16h7d1dn7y4}"

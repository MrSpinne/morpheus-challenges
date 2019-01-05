# Same as coding7.py but now with 4 indices needed

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/8/"
sol_url = "https://cc.the-morpheus.de/solutions/8/"

g = requests.get(chal_url).json()
indices = []
for index1, num1 in enumerate(g["list"]):
    for index2, num2 in enumerate(g["list"]):
        for index3, num3 in enumerate(g["list"]):
            for index4, num4 in enumerate(g["list"]):
                if index1 != index2 != index3 != index4 and num1 + num2 + num3 + num4 == g["k"]:
                    indices = [index1, index2, index3, index4]
                    break
            if len(indices) != 0:
                break
        if len(indices) != 0:
            break
    if len(indices) != 0:
        break

p = requests.post(sol_url, json.dumps({"token": indices})).text

print(indices) # Print solution
print(p) # Print code "TMT{HAwxLryQhiLh3eGh0pbx}"

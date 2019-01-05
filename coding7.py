# Get smallest indices of numbers from list from chal_url with the sum of k and post these indices to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/7/"
sol_url = "https://cc.the-morpheus.de/solutions/7/"

g = requests.get(chal_url).json()
indices = []
for index1, num1 in enumerate(g["list"]):
    for index2, num2 in enumerate(g["list"]):
        if index1 != index2 and num1 + num2 == g["k"]: # Both indices can't be the same
            indices = [index1, index2]
            break
    if len(indices) != 0:
        break

p = requests.post(sol_url, json.dumps({"token": indices})).text

print(indices) # Print solution
print(p) # Print code "Success: TMT{izRWIGQW5BsTv5R0JogU}"

# Get a list from chal_url, rotate it k-times and post the rotated list to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/4/"
sol_url = "https://cc.the-morpheus.de/solutions/4/"

g = requests.get(chal_url).json()
list = g["list"]
for i in range(g["k"]):
    list.insert(0, list.pop(-1)) # Remove last element of list and insert it at first the position
p = requests.post(sol_url, json.dumps({"token": list})).text

print(list) # Print solution
print(p) # Print code "Success: TMT{ckcagjB0E9fPjW2p6gxz}"

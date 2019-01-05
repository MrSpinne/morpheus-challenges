# Get the k-biggest number from a list from chal_url and post it to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/3/"
sol_url = "https://cc.the-morpheus.de/solutions/3/"

g = requests.get(chal_url).json()
g["list"].sort()
num = g["list"][-g["k"]]
p = requests.post(sol_url, json.dumps({"token": num})).text

print(num) 	# Print solution
print(p) 	# Print code "Success: TMT{S0SpkHzubAmCu7H3r5wR}"

# Get index of number "k" from "list" from chal_url and post it to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/2/"
sol_url = "https://cc.the-morpheus.de/solutions/2/"

g = requests.get(chal_url).json()
num = g["k"]
index = g["list"].index(num)
p = requests.post(sol_url, json.dumps({"token": index})).text

print(index) 	# Print solution
print(p)		# Print code "Success: TMT{AlwiUi8lp8du3iFTs8kc}"

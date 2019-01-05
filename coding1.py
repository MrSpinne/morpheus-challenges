import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/1/"
sol_url = "https://cc.the-morpheus.de/solutions/1/"

g = requests.get(chal_url).text
p = requests.post(sol_url, json.dumps({"token": g})).text

print(g) # Print solution
print(p) # Print code "Success: TMT{WBVjoml6PjsOu3yzFvr3}"

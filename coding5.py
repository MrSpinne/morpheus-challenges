# Get a string from chal_url and post it's evaluation to sol_url

import requests
import json

chal_url = "https://cc.the-morpheus.de/challenges/5/"
sol_url = "https://cc.the-morpheus.de/solutions/5/"

g = requests.get(chal_url).text
task = []
symbol = ""

# Convert string into list (e.g. "22 + 34" -> ["22", "+", "34"]
for char in g + " ":
    if char != " ":             # Add every char of number (or operand) to symbol
        symbol += char
    else:
        if symbol != "":        # Symbol ended, add it to list and continue (reset symbol) 
            task.append(symbol)
        symbol = ""

# Evaluate until there's just one value left
while len(task) != 1:
    for index, symbol in enumerate(task):
        if symbol == "+":
            task.insert(index + 1, float(task[index - 2]) + float(task[index - 1])) # Calculate result of the 2 numbers before operand
            del task[index] # Delete operand
            del task[index - 1] # Delete 2. number
            del task[index - 2] # Delete 1. number
            break # Break to update indices
        elif symbol == "-":
            task.insert(index + 1, float(task[index - 2]) - float(task[index - 1]))
            del task[index]
            del task[index - 1]
            del task[index - 2]
            break
        elif symbol == "*":
            task.insert(index + 1, float(task[index - 2]) * float(task[index - 1]))
            del task[index]
            del task[index - 1]
            del task[index - 2]
            break
        elif symbol == "/":
            task.insert(index + 1, float(task[index - 2]) / float(task[index - 1]))
            del task[index]
            del task[index - 1]
            del task[index - 2]
            break

p = requests.post(sol_url, json.dumps({"token": int(task[0])})).text

print(int(task[0])) # Print solution
print(p) # Print code "Success: TMT{cLVgwaS4j3JJorwe1GCw}"

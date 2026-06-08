import json

# ----------- This code is to convert JSON to python txt ---------------

# some json data
x = '{"Name": "Sathvk", "Age": 22, "City": "BLY"}'

# parse x
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print()



# ----------- This code is to convert python txt to JSON ------------

# python txt (dict)
a = {
    "name": "Sathvik Dixit",
    "age": 22,
    "City": "Bangalore"
}

# converting into json
b = json.dumps(a)

# result in JSON formate
print(b)
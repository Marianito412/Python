import json

with open("test.json") as json_file:
    beta = json.load(json_file)
beta = str(beta).replace("'", '"')
data = json.loads(beta)
for course in data["Classes"]:
    print(course["name"])
    print("_______________________________")
with open("new_test.json", "w") as f:
    json.dump(data, f, indent=2)


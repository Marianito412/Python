import json

with open("test.json") as json_file:
    beta = json.load(json_file)
    print(beta)
    for course in beta:
        print(course["name"] + "        " + )
        print("_______________________________")
    with open("new_test.json", "w") as f:
        json.dump(beta, f, indent=2)


import json

data = json.load(open("population_group(old).json"))

output = []

for key in data:
	output.append({"id" : int(key), "count" : data[key]["count"]})

with open("population_group.json", "w") as outfile:
    json.dump(output, outfile)
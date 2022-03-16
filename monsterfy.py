import csv
import json

ms = []

with open('monsters.csv', newline='') as csvfile:
		mreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		skip = True
		for row in mreader:
			if skip:
				skip = False
			else:
				ms.append("'"+row[0]+"'")

monster_string = "var MONSTERS = [" + ", ".join(ms) + "];"



for m in ms:
	print(m)


with open('monsters.js', 'w') as f:
    f.write(monster_string)
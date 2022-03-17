import csv
import json

ms = []
# ms[0] will be the string to construct the variable
# ms[1] will be an array of types

typeslist = []
# all types in everything

typeslist_pretty = []
# prettified

typescount = {}

with open('monsters.csv', newline='') as csvfile:
		mreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		skip = True
		for row in mreader:
			if skip:
				skip = False
			else:
				adder = '["'+row[0]+'",['
				types = row[1].split('/')
				types2 = []
				for t in types:
					types2.append('"'+t+'"')
					if t not in typeslist:
						typeslist.append(t)
						typeslist_pretty.append('"'+t+'"')
						typescount[t] = 0
					typescount[t] += 1
				adder += ",".join(types2)
				adder += "]]"
				ms.append(adder)

monster_string = "var MONSTERS = [" + ", ".join(ms) + "];\n" + "var ALLTYPES = [" + ",".join(typeslist_pretty)+"];"
# build a string to write a variable to file
# so hacky



for t in typescount:
	print(t+": "+str(typescount[t]))


with open('monsters.js', 'w') as f:
    f.write(monster_string)
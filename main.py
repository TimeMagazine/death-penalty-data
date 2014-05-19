#!/usr/bin/env python

import sys
import os.path
import ColumnMap
import Mapping
import Execution
from collections import defaultdict
import pprint, json, csv

def writeOutput(AllExecutions):
	if "--json" in sys.argv:
		writeJSON(AllExecutions)
	elif "--summary" in sys.argv:
		writeCSVList(AllExecutions)
	else:
		writeCSV(AllExecutions)

def prettyprint(AllExecutions):
	pprint.pprint(AllExecutions)

def writeJSON(AllExecutions):
	with open("data.json", "w") as outfile:
	    json.dump(AllExecutions, outfile, indent=4)
	print "Wrote JSON file"

def writeCSV(AllExecutions):
	spamWriter = csv.writer(open('data.csv', 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	spamWriter.writerow(AllExecutions[1].keys())
	for execution in AllExecutions:
		spamWriter.writerow(execution.values())
	print "Wrote CSV file"


def writeCSVList(AllExecutions):
	spamWriter = csv.writer(open('data.csv', 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	#spamWriter.writerow(AllExecutions[1].keys())
	for execution in AllExecutions:
		spamWriter.writerow(execution)
	print "Wrote CSV file"


Maps = ColumnMap.Maps
CrimeMappings = Mapping.CrimeMappings
AllExecutions = []

#1608-2002
epsyfile = "08451-0001-Data.txt"
if not os.path.isfile(epsyfile):
	epsyfile = raw_input ('Enter EPSY file name: ')
if not os.path.isfile(epsyfile):
	print "Couldn't find file"
	sys.exit()

with open(epsyfile) as asciidata:
 for penalty in asciidata:
 	current_execution = Execution.Execution()
 	for column in Maps:
 		value = penalty[column['begin']:column['end']+1]
 		if value.isdigit():
 			if column['expand'] == True:
	 			value = int(value)
 				if value == 0:
 					attribute = 0
	 			else:
		 			attribute = CrimeMappings[column['name']][value]

		 	else:
		 		attribute = value
		else:
			attribute = value.strip()
		setattr(current_execution,column['name'],attribute)
	AllExecutions.append(current_execution.getExecution())

print "found %d total executions in the data" % len(AllExecutions)

if "--states" in sys.argv:
	AllExecutions = [ex for ex in AllExecutions if ex["JurisdictionOfExecution"] == "State"]
	print "reduced to %d executions carried out by states" % len(AllExecutions)

if "--summary" in sys.argv:	
	data = defaultdict(lambda: defaultdict(int))
	total = defaultdict(int)

	for ex in AllExecutions:
		data[ex['DateYear']][ex['StateOfExecution']] += 1
		total[ex['StateOfExecution']] += 1

	headers = sorted(total.keys())
	output = [["year"] + headers]
	for y in range(1700, 2003):
		datum = [y]
		for state in headers:		
			datum.append(0 if state not in data[str(y)] else data[str(y)][state])
		output.append(datum)
	AllExecutions = output

writeOutput(AllExecutions)
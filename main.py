import ColumnMap
import Mapping
import Execution
import pprint
import json
import csv

def prettyprint(AllExecutions):
	pprint.pprint(AllExecutions)

def wrteJSON(AllExecutions):
	with open("data-json.json", "w") as outfile:
	    json.dump(AllExecutions, outfile, indent=4)

def writeCSV(AllExecutions):
	spamWriter = csv.writer(open('data.csv', 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	spamWriter.writerow(AllExecutions[1].keys())
	for execution in AllExecutions:
		spamWriter.writerow(execution.values())

Maps = ColumnMap.Maps
CrimeMappings = Mapping.CrimeMappings
AllExecutions = []

with open('08451-0001-Data.txt') as asciidata:
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

writeCSV(AllExecutions)

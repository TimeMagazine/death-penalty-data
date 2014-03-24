import ColumnMap
import Mapping
import Execution

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
			attribute = value
		setattr(current_execution,column['name'],attribute)
	AllExecutions.append(current_execution.getExecution())

print AllExecutions
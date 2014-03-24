import ColumnMap
import Mapping

Maps = ColumnMap.Maps
CrimeMappings = Mapping.CrimeMappings

with open('08451-0001-Data.txt') as asciidata:
 for penalty in asciidata:
 	for column in Maps:
 		value = penalty[column['begin']:column['end']+1]
 		if value.isdigit():
 			if column['expand'] == True:
	 			value = int(value)
 				if value == 0:
 					print 'Missing Value'
	 			else:
		 			print column['name'] + " : " + CrimeMappings[column['name']][value]

		 	else:
		 		print column['name'] + " : " + value
		else:
			if value == '':
				print column['name'] + " : " + 'Missing Value'
			else:
				print column['name'] + " : " + value
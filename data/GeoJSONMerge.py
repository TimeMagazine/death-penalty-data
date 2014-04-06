import glob
master_file = open("master.json", "w")
master_file.write("{")
for file in glob.glob("/Applications/XAMPP/xamppfiles/htdocs/death-penalty/Maps/GeoJSON/*.geojson"):
	print file[65:72]
	current_file = open(file, 'r')
	current_file = current_file.read()
	master_file.write("\"" + file[65:72] + "\":")
	master_file.write(current_file)
	master_file.write(",")
master_file.write("}")
master_file.close()
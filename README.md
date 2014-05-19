death-penalty-data
==================

Convert the Espy file into clean CSV or JSON documents

##Data
Data for U.S. executions from 1608 through 2002 is provided by the ["ESPY file"](http://www.icpsr.umich.edu/icpsrweb/NACJD/studies/8451?archive=NACJD&q=espy&searchSource=revise), which is freely available for download from the Interuniversity Consortium for Political and Social Research. The license for this data prevents us form distributing the file through the repo, you will have to download this file manually and place it in the repo's root directory. The file in the uncompressed folder from ICPSR is named `08451-0001-Data.txt`.

##Running
After downloading the data, place the .txt file in the root directory and run the script and enter the file name of the EPSY file when prompted.

The script takes up to three arguments:

+ `--csv`: to retrieve a CSV file of the processed data

+ `--json`: to retrieve a JSON file with the processed data

+ `--states`: reduce list to executions carried out by the state. (Excludes federal and military executions)

+ `--summary`: instead of a list of individual executions, return aggregate data by state
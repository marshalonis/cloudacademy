import csv
import json
import sys

csvfile = open(sys.argv[1], 'r')
jsonfile = open(sys.argv[2], 'w')

fieldnames = ("resource","name","project","email")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dumps(row, jsonfile)
    #jsonfile.write('\n')
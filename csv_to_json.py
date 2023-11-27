import os
import csv
import json

def parse_csv(datafile):
    data = []
    with open(datafile,'rt') as infile:
        r = csv.DictReader(infile)
        for line in r:
            data.append(line)
        return data

def main():
    filename = input("Enter the filename (must be in same working dir): ")
    datafile = os.path.join("", filename)
    d = parse_csv(datafile)
    json_filename = filename.split('.')[0]+".json"
    json_object = json.dumps(d,indent=4, sort_keys=True)
    with open(json_filename,"w") as outfile:
        outfile.write(json_object)


main()

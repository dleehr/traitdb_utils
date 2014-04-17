#!/usr/bin/env python

import csv
import re

BASE_PATH = "/Users/dan/Data/TreeOfSex/csv/PlantsApril2014/"
PLANTS_FILE = BASE_PATH + "plantsTreeOfSex.csv"
OUTPUT_CSVFILE = BASE_PATH + "plantsTreeOfSex-copiedcolumns.csv"

COLUMNS_TO_DUPLICATE = {
    'source: Gametophytic chromosome number':
        ['source: Gametophytic chromosome number (minimum)', 'source: Gametophytic chromosome number (mean)',],
    'source: Sporophytic chromosome number':
        ['source: Sporophytic chromosome number (minimum)', 'source: Sporophytic chromosome number (mean)',],
    'source: Woodiness':
        ['source: Woodiness count'],
}

def get_source_fieldnames():
    return COLUMNS_TO_DUPLICATE.keys()

def get_dest_fieldnames():
    names = []
    for items in COLUMNS_TO_DUPLICATE.values():
        for i in items:
            names.append(i)
    return names

def main():
    with open(PLANTS_FILE, 'rb') as infile:
        reader = csv.DictReader(infile)
        with open(OUTPUT_CSVFILE, 'wb') as outfile:
            source_fieldnames = reader.fieldnames
            output_fieldnames = source_fieldnames + get_dest_fieldnames()
            writer = csv.DictWriter(outfile, output_fieldnames)
            writer.writeheader()
            for row_dict in reader:
                for k in row_dict.keys():
                    v = row_dict[k]
                    if k in get_source_fieldnames():
                        # make new values for each of the copied ones
                        for dest_fieldname in COLUMNS_TO_DUPLICATE[k]:
                            row_dict[dest_fieldname] = v
                writer.writerow(row_dict)

if __name__ == '__main__':
    main()

#!/usr/bin/env python

import csv
import re

BASE_PATH = "/Users/dan/Data/TreeOfSex/csv/PlantsApril2014/"
PLANTS_FILE = BASE_PATH + "plantsTreeOfSex.csv"
OUTPUT_CSVFILE = BASE_PATH + "plantsTreeOfSex-fixedquotes.csv"


def main():
    with open(PLANTS_FILE, 'rb') as infile:
        reader = csv.DictReader(infile)
        with open(OUTPUT_CSVFILE, 'wb') as outfile:
            writer = csv.DictWriter(outfile, reader.fieldnames)
            writer.writeheader()
            for row_dict in reader:
                for k in row_dict.keys():
                    v = row_dict[k]
                writer.writerow(row_dict)

if __name__ == '__main__':
    main()

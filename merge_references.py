#!/usr/bin/env python

import csv

BASE_PATH = "/Users/dan/Data/TreeOfSex/csv/PlantsApril2014/"
PLANTS_CSVFILE = BASE_PATH + "plantsTreeOfSex.csv"
REFERENCES_CSVFILE = BASE_PATH + "References_plants.csv"
OUTPUT_CSVFILE = BASE_PATH + "plantsTreeOfSex-with-references.csv"
SPLIT_DELIMITER = "|"
JOIN_DELIMITER = "; "

def read_references():
    references = {}
    with open(REFERENCES_CSVFILE, 'rb') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            references[row['Key']] = row['Reference']
    return references

def merge_references(row_dict, lookup_table):
    for column_name in row_dict.keys():
        if column_name.startswith("source: "):
            # Column is a source column
            if row_dict[column_name] is not None and row_dict[column_name] != '':
                replaced_references = replace_references(row_dict[column_name], lookup_table)
                row_dict[column_name] = replaced_references
    return row_dict

def replace_references(tokens='', lookup_table={}):
    replaced = []
    for token in tokens.split(SPLIT_DELIMITER):
        full_reference = lookup_reference(token, lookup_table)
        if full_reference:
            replaced.append(full_reference)
    return JOIN_DELIMITER.join(replaced)


def lookup_reference(token='', lookup_table={}):
    if token not in lookup_table:
        return token
    return lookup_table[token]

def main():
    lookup_table = read_references()
    with open(PLANTS_CSVFILE, 'rb') as infile:
        reader = csv.DictReader(infile)
        with open(OUTPUT_CSVFILE, 'wb') as outfile:
            writer = csv.DictWriter(outfile, reader.fieldnames)
            writer.writeheader()
            for row_dict in reader:
                merge_references(row_dict, lookup_table)
                writer.writerow(row_dict)

if __name__ == '__main__':
    main()
